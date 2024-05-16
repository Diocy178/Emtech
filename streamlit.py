import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('/content/final_model.keras')

# Define class labels
class_labels = ['rainy', 'sunny', 'cloudy', 'snowy', 'foggy']  # Adjust based on your classes

# Function to preprocess the uploaded image
def preprocess_image(image):
    img = image.resize((224, 224))  # Resize the image to match the input size of the model
    img = np.asarray(img) / 255.0   # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Streamlit app
def main():
    st.title("Image Classifier")
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Preprocess and predict
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = class_labels[np.argmax(prediction)]

        st.write(f"Prediction: {predicted_class}")

if __name__ == '__main__':
    main()
