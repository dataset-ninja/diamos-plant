Dataset **DiaMOS Plant** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMzI1OF9EaWFNT1MgUGxhbnQvZGlhbW9zLXBsYW50LURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogImJ0TFZSYnZtNmZ0Zkdtd3BLcGdDMllOZFZYcVZmWGFTcHh4SllwNEtwRmc9In0=?response-content-disposition=attachment%3B%20filename%3D%22diamos-plant-DatasetNinja.tar%22)

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
