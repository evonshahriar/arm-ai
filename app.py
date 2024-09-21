import streamlit as st
import openai

# Import the option_menu from streamlit-option-menu
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="ARM",
    page_icon="🦾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to inject local CSS
def local_css(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Apply custom CSS
local_css("style.css")

# Initialize OpenAI API key
openai.api_key = st.secrets["openai"]["api_key"]

from routers import upload, summarize, identify_gaps, generate_hypotheses
from services import workflow_generation

def main():
    # Initialize session state variables
    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 0  # 0: Home, 1: Upload, 2: Summary, etc.
    if 'content' not in st.session_state:
        st.session_state['content'] = None
    if 'summary' not in st.session_state:
        st.session_state['summary'] = None
    if 'gaps' not in st.session_state:
        st.session_state['gaps'] = None
    if 'hypotheses' not in st.session_state:
        st.session_state['hypotheses'] = None
    if 'hypothesis' not in st.session_state:
        st.session_state['hypothesis'] = None
    if 'workflow' not in st.session_state:
        st.session_state['workflow'] = None
    if 'related_papers' not in st.session_state:
        st.session_state['related_papers'] = None

    # Display a banner image
    st.image("images/banner.png", use_column_width=True)

    steps = ["Home", "Upload Document", "Summary", "Research Gaps", "Hypotheses", "Workflow", "Related Papers", "Expert Chat"]

    # Sidebar for navigation using option_menu
    with st.sidebar:
        st.title("Navigation")
        selected_step = option_menu(
            menu_title=None,
            options=steps,
            icons=["house", "cloud-upload", "file-earmark-text", "binoculars", "lightbulb", "diagram-3", "journal", "chat"],
            menu_icon="cast",
            default_index=st.session_state['current_step'],
            orientation="vertical",
            styles={
                "container": {"padding": "5!important", "background-color": "#000000"},
                "icon": {"color": "#6C63FF", "font-size": "25px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "2px",
                    "--hover-color": "#000000",
                },
                "nav-link-selected": {"background-color": "#6C63FF", "color": "white"},
            }
        )
        st.session_state['current_step'] = steps.index(selected_step)

    # Navigation buttons (Updated for the new Expert Chat step)
    def nav_buttons():
        col1, col2, col3 = st.columns([1, 6, 1])
        with col1:
            if st.session_state['current_step'] > 0:
                if st.button("⬅️ Back"):
                    st.session_state['current_step'] -= 1
                    st.rerun()
        with col3:
            if st.session_state['current_step'] < len(steps) - 1:
                if st.button("Next ➡️"):
                    st.session_state['current_step'] += 1
                    st.rerun()

    # App logic based on current step
    # Home page layout
    if st.session_state['current_step'] == 0:
        st.title("🦾 ARM — AI Research Mentor")

        # Create two columns: one for text and one for the start button
        col1, col2 = st.columns([2.5, 1.5])


        with col1:
            st.markdown(
                """
                ### 
                **Improve your research process with AI Research Mentor (ARM).**  
                With **ARM**, you can:

                | #  | Feature                       | Description                                            |
                |----|-------------------------------|--------------------------------------------------------|
                | 1  | **Upload Documents**           | Quickly analyze your research documents.               |
                | 2  | **Get Summaries**              | Capture key insights from your documents.              |
                | 3  | **Identify Research Gaps**     | Find gaps in research to refine your focus.            |
                | 4  | **Generate Hypotheses**        | Develop research questions to guide your study.        |
                | 5  | **Create Workflows**           | Tailor workflows according to your hypothesis.         |
                | 6  | **Explore Related Papers**     | Broaden your understanding by exploring related work.  |
                | 7  | **Consult Experts**            | Get real-time advice on your hypothesis from experts.  |

                _Turn your ideas into impactful research with expert AI assistance. Let’s get started!_
                """
            )


        with col2:
            # Space above the button to center it vertically
            st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
            if st.button("🔎 Click to Get Started", key="start_button"):
                st.session_state['current_step'] = 1
                st.rerun()


    elif st.session_state['current_step'] == 1:
        # Upload Document
        st.header("Upload Document")
        uploaded_file = upload.upload_file()
        if uploaded_file:
            st.session_state['content'] = upload.extract_content(uploaded_file)
            if st.session_state['content']:
                st.success("Document uploaded and content extracted successfully.")
                # Automatically move to next step
                st.session_state['current_step'] = 2
                st.rerun()
            else:
                st.error("Failed to extract content from the uploaded document.")
        nav_buttons()

    elif st.session_state['current_step'] == 2:
        # Summary
        st.header("1. Document Summary")
        if st.session_state['content']:
            summarize.display_summary(st.session_state['content'])
            # User can click Next to proceed
        else:
            st.warning("Please upload a document first.")
        nav_buttons()

    elif st.session_state['current_step'] == 3:
        # Research Gaps
        st.header("2. Research Gaps")
        if st.session_state['content']:
            identify_gaps.display_gaps(st.session_state['content'])
            # User can click Next to proceed
        else:
            st.warning("Please upload a document and view the summary first.")
        nav_buttons()

    elif st.session_state['current_step'] == 4:
        # Hypotheses
        st.header("3. Hypothesis Generation")
        if st.session_state['gaps']:
            generate_hypotheses.display_hypotheses(st.session_state['gaps'])
        else:
            st.warning("Please identify research gaps first.")
        nav_buttons()

    elif st.session_state['current_step'] == 5:
        # Workflow
        st.header("4. Experiment Workflow")
        if st.session_state['hypothesis']:
            if st.session_state['workflow'] is None:
                with st.spinner('Generating workflow...'):
                    st.session_state['workflow'] = workflow_generation.generate_workflow(st.session_state['hypothesis'])
            st.write(st.session_state['workflow'])
        else:
            st.warning("Please generate a hypothesis first.")
        nav_buttons()

    elif st.session_state['current_step'] == 6:
        # Related Papers
        st.header("5. Related Research Papers")
        if st.session_state['hypothesis']:
            from routers.search_papers import display_related_papers
            display_related_papers(st.session_state['hypothesis'])
        else:
            st.warning("Please generate a hypothesis first.")
        nav_buttons()
        
    elif st.session_state['current_step'] == 7:  # Expert Chat step
        st.header("6. Expert Chat")
        if st.session_state['hypothesis']:
            from routers.expert_simulation import display_expert_chat
            display_expert_chat(st.session_state['hypothesis'])  # Dynamically call based on hypothesis
        else:
            st.warning("Please generate a hypothesis first.")
        nav_buttons()

if __name__ == "__main__":
    main()
