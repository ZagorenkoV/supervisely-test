from davis_preprocessor_class import DAVISDataPreprocessor
from keras.models import Model
from loading_images import path

path_to_inputs = path
path_to_outputs = 'C:\Projects\supervisely'

davis_data = DAVISDataPreprocessor(path_to_inputs, path_to_outputs)

# use with keras directly
Model.fit_generator(davis_data.generate_data())