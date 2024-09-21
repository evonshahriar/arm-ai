import openai
import streamlit as st

# Function to dynamically determine the expert based on the hypothesis
def choose_expert(hypothesis):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a research assistant who selects the most suitable expert to answer questions on various academic fields based on a hypothesis."},
                {"role": "user", "content": f"Based on the following hypothesis, determine the most suitable well-known expert to simulate a conversation with:\n\n{hypothesis}"}
            ],
            max_tokens=500,
            temperature=0.5,
        )
        expert = response['choices'][0]['message']['content'].strip()
        return expert
    except Exception as e:
        st.error(f"Error choosing expert: {e}")
        return "Generic Expert"  # Default fallback in case of an error
