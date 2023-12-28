Dataset **DiaMOS Plant** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/Y/4/6o/E6cAUYYljsLmrtobacnPTwga0zbpNg6fBcyBBq3sQzyu3Uf9YdVMrkH8k2pgsY91LWtF8QFrObGQIGWfjjMM4waHHU9f8aG6489FZ0UcQeEGin25zveAGqVY3Tou.tar)

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
