import streamlit as st
import easyocr
from PIL import Image
import numpy as np

def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        # Determine the end of current chunk
        end = start + chunk_size

        # If not last chunk, extend it to include the overlap
        if end + overlap < len(text):
            end += overlap

        # Append current chunk
        chunks.append(text[start:end])

        # Move start pointer
        start += chunk_size

    return chunks


# Title
st.title('OCR Application using EasyOCR')

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert file to image
    image = Image.open(uploaded_file)

    # Display image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # OCR
    reader = easyocr.Reader(['en'])  #languages
    result = reader.readtext(np.array(image))

    # Combine OCR results to one string
    full_text = ' '.join([detection[1] for detection in result])

    # Chunk text
    chunks = chunk_text(full_text)

    # Display chunks
    st.subheader('OCR Result')
    for i, chunk in enumerate(chunks):
        st.write(chunk)
