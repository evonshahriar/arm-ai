import streamlit as st
from services import text_extraction

def upload_file():
    # Moved the upload widget to the main page
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    return uploaded_file

def extract_content(uploaded_file):
    with st.spinner('Extracting text...'):
        if uploaded_file.type == "application/pdf":
            content = text_extraction.extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            content = text_extraction.extract_text_from_docx(uploaded_file)
        else:
            content = None
    return content
