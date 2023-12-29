import csv
import glob
import os
import shutil
from urllib.parse import unquote, urlparse

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from PIL import Image
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
    mkdir,
)
from tqdm import tqdm

import src.settings as s

Image.MAX_IMAGE_PIXELS = None


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    dataset_path = "/home/alex/DATASETS/TODO/DiaMOS/Pear"
    batch_size = 10
    ds_name = "ds"
    annotations_path = "/home/alex/DATASETS/TODO/DiaMOS/Pear/annotation/YOLO/"
    tags_path = "/home/alex/DATASETS/TODO/DiaMOS/Pear/annotation/csv/diaMOSPlant.csv"

    incorrect_anns = "pear annotations like XXXX.txt may be no correct"

    def create_ann(image_path):
        labels = []
        tags = []
        class_folder = image_path.split("/")[-2]
        obj_class = folder_to_class[class_folder]
        tag_value = file_to_tag_value.get(get_file_name_with_ext(image_path))
        if tag_value is not None:
            tags = [sly.Tag(tag_meta, value=tag_value)]

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        if img_wight == 5184:
            source = sly.Tag(source_meta, value="DSLR camera")
        else:
            source = sly.Tag(source_meta, value="smartphone camera")

        tags.append(source)

        bbox_name = get_file_name(image_path) + ".txt"
        if bbox_name == "2865.txt":  # error in file
            return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)
        bbox_path = os.path.join(annotations_path, sub_folder, bbox_name)
        if file_exists(bbox_path):
            with open(bbox_path) as f:
                content = f.read().split("\n")

                for curr_data in content:
                    if len(curr_data) != 0:
                        curr_data = list(map(float, curr_data.split(" ")))
                        left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                        right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                        top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                        bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                        rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                        label = sly.Label(rectangle, obj_class)
                        labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    obj_class_pear = sly.ObjClass("pear", sly.Rectangle)
    obj_class_healthy = sly.ObjClass("healthy leaf", sly.Rectangle)
    obj_class_curl = sly.ObjClass("curl leaf", sly.Rectangle)
    obj_class_slug = sly.ObjClass("slug leaf", sly.Rectangle)
    obj_class_spot = sly.ObjClass("spot leaf", sly.Rectangle)

    source_meta = sly.TagMeta(
        "source",
        sly.TagValueType.ONEOF_STRING,
        possible_values=["smartphone camera", "DSLR camera"],
    )

    folder_to_class = {
        "fruits": obj_class_pear,
        "temp": obj_class_pear,
        "curl": obj_class_curl,
        "healthy": obj_class_healthy,
        "slug": obj_class_slug,
        "spot": obj_class_spot,
    }

    tag_meta = sly.TagMeta(
        "severity level",
        sly.TagValueType.ONEOF_STRING,
        possible_values=[
            "no risk (0%)",
            "very low risk (1-5%)",
            "low risk (6-20%)",
            "medium risk (21-25%)",
            "high risk (>50%)",
        ],
    )

    index_to_values = {
        0: "no risk (0%)",
        1: "very low risk (1-5%)",
        2: "low risk (6-20%)",
        3: "medium risk (21-25%)",
        4: "high risk (>50%)",
    }

    file_to_tag_value = {}
    with open(tags_path, "r") as file:
        csvreader = csv.reader(file)
        for idx, row in enumerate(csvreader):
            if idx == 0:
                continue
            curr_data = row[0].split(";")
            possible_values = curr_data[5:]
            if "1" in possible_values:
                index = possible_values.index("1")
            else:
                continue
            file_to_tag_value[curr_data[0]] = index_to_values[index]

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[
            obj_class_healthy,
            obj_class_pear,
            obj_class_curl,
            obj_class_slug,
            obj_class_spot,
        ],
        tag_metas=[tag_meta, source_meta],
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    ann_folders = next(os.walk(annotations_path))[1]

    for sub_folder in ann_folders:
        images_path = os.path.join(dataset_path, sub_folder)

        if sub_folder == "leaves":
            images_pathes = glob.glob(images_path + "/*/*.jpg")
        else:
            temp_path = os.path.join(dataset_path, "temp")
            mkdir(temp_path)
            images_names = [
                im_name for im_name in os.listdir(images_path) if not im_name.startswith(".")
            ]
            images_pathes = []
            for im_name in images_names:
                image_path = os.path.join(images_path, im_name)
                if get_file_size(image_path) > 20000000:
                    temp_image = Image.open(image_path)
                    new_path = os.path.join(temp_path, im_name)
                    temp_image.save(new_path)
                    images_pathes.append(new_path)
                else:
                    images_pathes.append(image_path)

        progress = sly.Progress("Create dataset {}".format(sub_folder), len(images_pathes))

        for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
            img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))

    return project
