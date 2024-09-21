import openai
import streamlit as st
from services.image_generation import generate_expert_portrait
from services.expert_selection import choose_expert

def extract_expert_name(description):
    # Look for the phrase "Dr." or "Professor" followed by the name in the description
    if "Dr." in description:
        return "Dr. " + description.split("Dr.")[1].split('.')[0].strip()
    elif "Professor" in description:
        return "Professor " + description.split("Professor")[1].split('.')[0].strip()
    else:
        # If no "Dr." or "Professor" found, return a default name
        return "Expert"

def display_expert_chat(hypothesis):
    # Show loader until the expert is selected
    with st.spinner("Looking for the expert for the chosen hypothesis..."):
        if 'expert_name' not in st.session_state:
            # Get the full bio of the expert
            expert_full_description = choose_expert(hypothesis)
            # Extract only the name with title (Dr./Prof.); remove any markdown syntax
            expert_name = extract_expert_name(expert_full_description).replace("**", "")
            # Store expert bio and name separately
            st.session_state['expert_name'] = expert_name
            st.session_state['expert_bio'] = expert_full_description

        expert_name = st.session_state['expert_name']
        expert_bio = st.session_state['expert_bio']

        # Check if portrait has been generated, if not, generate and store in session
        if 'expert_image_url' not in st.session_state:
            st.session_state['expert_image_url'] = generate_expert_portrait(expert_name)

    # Display the expert's image and bio side by side
    col1, col2 = st.columns([1, 3])  # Adjust column widths as needed

    with col1:
        if st.session_state['expert_image_url']:
            st.image(st.session_state['expert_image_url'], use_column_width=True)
            st.caption(f"A digital sketch of {expert_name} using OpenAI DALL·E API")
        else:
            st.write("Unable to generate the expert's portrait.")
    
    with col2:
        # Display expert's full bio alongside the image
        st.write(f"**Bio:** {expert_bio}")

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Text area for user input
    user_input = st.text_area("Your question", height=100, key="chat_input")
    
    if st.button("Ask"):
        if user_input:
            with st.spinner(f"Asking {expert_name}..."):
                try:
                    # Add user input to chat history
                    st.session_state['chat_history'].append({"role": "user", "content": user_input})

                    # Prepare the message history for the API
                    messages = [
                        {"role": "system", "content": f"You are {expert_name}, an expert in your field. Provide personalized concise insights in a human-like talking way on the hypothesis: {hypothesis}."}
                    ] + [
                        {"role": msg["role"], "content": msg["content"]} for msg in st.session_state['chat_history']
                    ]

                    # Generate expert response using OpenAI API
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=messages,
                        max_tokens=500,
                        temperature=0.5,
                    )
                    
                    # Extract and add expert's answer to chat history
                    answer = response['choices'][0]['message']['content'].strip()
                    st.session_state['chat_history'].append({"role": "assistant", "content": answer})
                
                except Exception as e:
                    st.error(f"Error while asking {expert_name}: {e}")

    # Display chat history in reverse order (recent first)
    st.write("### Chat History")
    for message in reversed(st.session_state['chat_history']):
        if message["role"] == "user":
            # Display user's message with a border instead of a background color
            st.markdown(f"""
                <div style="border: 2px solid #6C63FF; padding:10px; border-radius:10px; margin-bottom:10px;">
                    <strong>You:</strong> {message['content']}
                </div>
            """, unsafe_allow_html=True)
        else:
            # Display expert's message with a border instead of a background color
            st.markdown(f"""
                <div style="border: 2px solid #e0f7fa; padding:10px; border-radius:10px; margin-bottom:10px;">
                    <strong>{expert_name.replace("**", "")}:</strong> {message['content']}
                </div>
            """, unsafe_allow_html=True)

    # Button to clear the chat history
    if st.button("Clear Chat"):
        st.session_state['chat_history'] = []
