import streamlit as st
from services import paper_search

def display_related_papers(hypothesis):
    st.subheader("")

    # Check if related papers are already in session state
    if st.session_state['related_papers'] is None:
        with st.spinner('Searching CrossRef...'):
            st.session_state['related_papers'] = paper_search.search_crossref(hypothesis)

    # Display the related papers
    related_papers = st.session_state['related_papers']
    if related_papers:
        st.write("Found related papers:")
        for paper in related_papers:
            title = paper.get('title', ['No Title'])[0]
            doi = paper.get('DOI', None)

            # Display the title and DOI link
            if doi:
                st.write(f"- **{title}** ([DOI link](https://doi.org/{doi}))")
            else:
                st.write(f"- **{title}** (No DOI available)")
    else:
        st.write("No related papers found.")
