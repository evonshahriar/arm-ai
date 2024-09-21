import openai
import streamlit as st

# Function to generate an expert's portrait using OpenAI DALL·E
def generate_expert_portrait(expert_name):
    try:
        # Prompt for generating an expert's portrait
        prompt = f"A digital sketch of {expert_name} in a realistic style which should be a high-resolution pencil based sketch portrait ensuring the likeness is super accurate, capturing the facial features, expression, and overall appearance of the subject without mentioning any texts."
        
        # Call OpenAI DALL·E API for image generation
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256"  # Image size
        )

        # Return the image URL
        image_url = response['data'][0]['url']
        return image_url

    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None
