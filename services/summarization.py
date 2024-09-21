import openai
import streamlit as st

def summarize_text(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert at summarizing academic texts. Please summarize the text concisely, covering all key aspects in no more than 150 words."},
                {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
            ],
            max_tokens=1000,
            temperature=0.5,
        )
        summary = response['choices'][0]['message']['content'].strip()
        return summary
    except Exception as e:
        st.error(f"Error during summarization: {e}")
        return "An error occurred during summarization."