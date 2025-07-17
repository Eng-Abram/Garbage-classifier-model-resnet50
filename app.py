import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("ResNet50_model.h5")
class_names = ['Battery', 'Biological', 'Cardboard', 'Clothes', 'Glass', 'Metal', 'Paper', 'Plastic', 'Shoes', 'Trash']

def predict(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    processed_img = preprocess_input(img_array)
    prediction = model.predict(processed_img)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)
    return f"{predicted_class} ({confidence*100:.2f}%)"

gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Garbage Classifier"
).launch()