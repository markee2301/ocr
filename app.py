import streamlit as st
import easyocr
from PIL import Image
import io
import numpy as np

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

# Streamlit app title
st.title("IntelLibro Sample OCR")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Convert the file to an image
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")

    # Convert image to numpy array
    image_np = np.array(image)

    # Perform OCR on the image
    if st.button('Extract Text'):
        with st.spinner('Extracting text...'):
            # Use numpy array for EasyOCR
            results = reader.readtext(image_np, detail=0)
        st.success("Done!")
        st.write("Extracted Text:")
        for result in results:
            st.write(result)
