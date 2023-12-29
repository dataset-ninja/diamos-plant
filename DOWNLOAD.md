Dataset **DiaMOS Plant** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/N/T/Dl/b3Ga2FuiPXHry8G3klWIwCCGX3fYkF4Hsq9Y0TGhkeAWK4gO8jcZcno0KxriCWvgCeXwmtFEcexxIHV8pNVjuqzTaFjkxvawz1bqOT5bzPwEx0AGVDMegdgvlmZ1.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='DiaMOS Plant', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Pear.zip](https://zenodo.org/records/5557313/files/Pear.zip?download=1)
- [Description_DIaMOS_Plant_dataset.pdf](https://zenodo.org/records/5557313/files/Description_DIaMOS_Plant_dataset.pdf?download=1)
