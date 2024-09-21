import streamlit as st
from services import summarization

def display_summary(content):
    st.subheader("")
    if st.session_state['summary'] is None:
        with st.spinner('Generating summary...'):
            st.session_state['summary'] = summarization.summarize_text(content)
    st.write(st.session_state['summary'])
