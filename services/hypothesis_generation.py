import openai
import streamlit as st

def generate_hypotheses(gaps_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in formulating research hypotheses. Propose specific and testable hypotheses based on the research gaps provided, in no more than 250 words."},
                {"role": "user", "content": f"Based on the following research gaps, propose specific and testable hypotheses:\n\n{gaps_text}"}
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        hypotheses = response['choices'][0]['message']['content'].strip()
        return hypotheses
    except Exception as e:
        st.error(f"Error during hypothesis generation: {e}")
        return "An error occurred during hypothesis generation."
