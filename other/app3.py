import streamlit as st
import easyocr
from pdf2image import convert_from_bytes
from PIL import Image
import numpy as np

def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end + overlap < len(text):
            end += overlap
        chunks.append(text[start:end])
        start += chunk_size
    return chunks

# Title
st.title('OCR Application for PDFs using EasyOCR')

# File uploader for PDFs
uploaded_file = st.file_uploader("Choose a PDF file...", type=["pdf"])

if uploaded_file is not None:
    # Convert PDF pages to images
    pdf_images = convert_from_bytes(uploaded_file.read())

    # Display images
    for i, image in enumerate(pdf_images):
        st.image(image, caption=f'Page {i+1}', use_column_width=True)

    # OCR
    reader = easyocr.Reader(['en'])  # Languages
    full_text = ""

    for img in pdf_images:
        result = reader.readtext(np.array(img))
        page_text = ' '.join([detection[1] for detection in result])
        full_text += page_text + "\n"

    # Chunk text
    chunks = chunk_text(full_text)

    # Display OCR results
    st.subheader('OCR Result')
    for i, chunk in enumerate(chunks):
        st.write(chunk)
