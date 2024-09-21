import openai
import streamlit as st

def generate_workflow(hypothesis):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in designing experimental workflows. Create a concise and detailed experimental workflow to test the given hypothesis, in no more than 300 words."},
                {"role": "user", "content": f"Create a detailed experimental workflow to test the following hypothesis:\n\n{hypothesis}"}
            ],
            max_tokens=1000,
            temperature=0.5,
        )
        workflow = response['choices'][0]['message']['content'].strip()
        return workflow
    except Exception as e:
        st.error(f"Error during workflow generation: {e}")
        return "An error occurred during workflow generation."
