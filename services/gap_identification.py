import openai
import streamlit as st

def identify_gaps(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are skilled at identifying research gaps in academic texts. Provide a concise list of research gaps in no more than 200 words."},
                {"role": "user", "content": f"Based on the following text, identify potential research gaps:\n\n{text}"}
            ],
            max_tokens=1000,
            temperature=0.5,
        )
        gaps = response['choices'][0]['message']['content'].strip()
        return gaps
    except Exception as e:
        st.error(f"Error during gap identification: {e}")
        return "An error occurred during gap identification."
