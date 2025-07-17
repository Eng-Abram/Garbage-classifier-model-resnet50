# Garbage-classifier-model-resnet50
this notebook shows the process of building a DL classifier model that can classify up to ten different types of garbage

in this notebook you will go through the full process of preprocessing data, building, training, and deployment the model.

we used pathlib and os libraries to deal with directories, loading data, and splitting them into training and validation, and test data.
also we removed thecorrupted files from tha dataset using os library.

preprocessing data was firstly resizing it into a properiate size to help training the model will, after that we applied some augmentation to help the model to generalize the data and avoid overfitting.

we used a pretrained model which is ResNet50 in this project which gave a training accuracy of 99% and validation accuracy of 95% which is great metrics for such a model.

our future work will be upgrading the model to not just classify an image, but also segment its objects.
