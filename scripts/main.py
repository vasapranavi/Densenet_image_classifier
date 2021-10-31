import Image as IM
import keras
import tensorflow as tf
import numpy as np
from fastapi import FastAPI

'''Defining Model'''
def get_model():
    # Defining the model with pretrained weights
    model = tf.keras.applications.densenet.DenseNet121(
        include_top=True,
        weights="densenet121_weights_tf_dim_ordering_tf_kernels.h5",
        input_tensor=None,
        input_shape=None,
        pooling=None,
        classes=1000,
    )
    return model, model.input_shape[1:3]

'''Made changes on input'''
def modify_input(image_url, input_dimentions):
    # Loading image
    image = keras.preprocessing.image.load_img('resources/'+image_url, target_size=input_dimentions)
    # Making adjustments to the image
    doc = keras.preprocessing.image.img_to_array(image)
    doc = np.expand_dims(doc, axis=0)
    # Pre processing the input image
    tf.keras.applications.densenet.preprocess_input(
        doc, data_format=None
    )
    return doc

'''Got predictions'''
def get_predictions(model, doc):
    predictions = model.predict(doc)
    top_predictions = tf.keras.applications.densenet.decode_predictions(predictions)
    return top_predictions[0][0][1]

'''Get response'''
def get_prediction(image_path: IM):
    model, input_dimentions = get_model()
    doc = modify_input(image_path.name, input_dimentions)
    response = get_predictions(model, doc)
    return{'response':response}