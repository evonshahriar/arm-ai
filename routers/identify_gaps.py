import streamlit as st
from services import gap_identification

def display_gaps(content):
    st.subheader("")
    if st.session_state['gaps'] is None:
        with st.spinner('Identifying research gaps...'):
            st.session_state['gaps'] = gap_identification.identify_gaps(content)
    st.write(st.session_state['gaps'])
