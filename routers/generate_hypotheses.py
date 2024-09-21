import streamlit as st
from services import hypothesis_generation
import re  # Import regex to clean up markdown artifacts

# Function to clean markdown artifacts
def clean_markdown(text):
    return re.sub(r'\*\*', '', text)  # Removes ** from the text

def display_hypotheses(gaps):
    st.subheader("")

    if st.session_state['hypotheses'] is None:
        with st.spinner('Generating hypotheses...'):
            st.session_state['hypotheses'] = hypothesis_generation.generate_hypotheses(gaps)

    st.success("Hypotheses generated successfully!")

    # Clean up the generated hypotheses
    hypotheses = [clean_markdown(hyp.strip()) for hyp in st.session_state['hypotheses'].split('\n') if hyp.strip()]

    # Display the list of generated hypotheses (without ticks)
    with st.expander("View Generated Hypotheses"):
        for hyp in hypotheses:
            st.markdown(f"**{hyp}**")

    # Allow the user to select a hypothesis from the list (without displaying ticks in the list above)
    selected_hypothesis = st.selectbox("Select a Hypothesis to Generate Workflow", hypotheses)

    # Store the selected hypothesis in session state
    st.session_state['hypothesis'] = selected_hypothesis

    # Button to move forward and generate workflow
    if st.button("Crosscheck & Generate Workflow"):
        st.success(f"Hypothesis selected: {st.session_state['hypothesis']}")
        # Move to next step
        st.session_state['current_step'] = 5
