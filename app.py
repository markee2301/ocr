import streamlit as st
import easyocr
from PIL import Image
import numpy as np
from fpdf import FPDF

reader = easyocr.Reader(['en'])
st.title("IntelLibro Sample OCR")

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf_output = pdf.output(dest="S").encode("latin1")
    return pdf_output

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    # st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")

    # Convert image to numpy array
    image_np = np.array(image)

    # Perform OCR
    if st.button('Extract Text'):
        with st.spinner('Extracting text...'):
            # Use numpy array for EasyOCR
            results = reader.readtext(image_np, detail=0)
        st.success("Done!")
        extracted_text = ' '.join(results)
        st.write(extracted_text)

        # DL as PDF
        pdf = create_pdf(extracted_text)
        st.download_button(label="Download as PDF",
                           data=pdf,
                           file_name="extracted_text.pdf",
                           mime="application/pdf")
st.markdown("Compare STRING SIMILARITY percentage [here!](https://www.tools4noobs.com/online_tools/string_similarity/)", unsafe_allow_html=True)
