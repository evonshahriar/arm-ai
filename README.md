# AI Research Mentor (ARM)

**AI Research Mentor (ARM)** assists new researchers in various aspects of their research workflow. ARM can help you:

- Upload and analyze research documents
- Summarize key points from the documents
- Identify research gaps
- Generate testable hypotheses
- Design experimental workflows
- Find related research papers
- Simulate expert consultations for real-time advice on hypotheses

ARM leverages **OpenAI's API** for natural language processing and offers a user-friendly interface built using **Streamlit**.

---

## Features

1. **Document Upload and Analysis**: Upload research documents (PDFs or DOCX) and extract content for further analysis.
2. **Document Summarization**: Summarizes the content, highlighting key points.
3. **Research Gap Identification**: Identifies potential gaps in the uploaded research, providing areas for further investigation.
4. **Hypothesis Generation**: Generates testable hypotheses based on the research gaps identified.
5. **Experimental Workflow Design**: Suggests detailed workflows for testing the generated hypotheses.
6. **Related Research Papers Search**: Uses CrossRef API to find related academic papers.
7. **Expert Chat Simulation**: Allows users to simulate a conversation with an expert, offering advice on selected hypotheses.

---

## Tech Stack

### **Frameworks & Libraries**

- **[Streamlit](https://streamlit.io/)**: Frontend framework to create a seamless user interface and interactive components.
- **[OpenAI API](https://beta.openai.com/)**: Used to integrate GPT-4 for natural language processing tasks such as summarization, gap identification, hypothesis generation, and expert chat simulation.
- **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/)**: A PDF parsing library for extracting text from uploaded PDF documents.
- **[python-docx](https://python-docx.readthedocs.io/en/latest/)**: Used to extract text from uploaded DOCX files.
- **[Requests](https://docs.python-requests.org/en/master/)**: A simple HTTP library used for interacting with the CrossRef API to search for related research papers.
- **[Streamlit Option Menu](https://github.com/victoryhb/streamlit-option-menu)**: A custom Streamlit component used for creating a sidebar navigation menu.

### **Other Technologies**

- **CrossRef API**: Used for fetching related academic papers based on the generated hypotheses.
- **CSS**: Custom styles for the user interface and experience, making it visually appealing and intuitive.

---

## Project Structure

The project is organized into different components as follows:

```
ai_research_mentor/
├── app.py                   # Main application file
├── routers/                 # Application routers for different functionalities
│   ├── __init__.py          # Init file for the routers module
│   ├── upload.py            # Upload document functionality
│   ├── summarize.py         # Document summarization functionality
│   ├── expert_simulation.py # Expert chat simulation functionality
│   ├── identify_gaps.py     # Research gap identification functionality
│   ├── generate_hypotheses.py  # Hypothesis generation functionality
│   └── search_papers.py     # Search for related papers functionality
├── services/                # Service files for backend processing
│   ├── __init__.py          # Init file for the services module
│   ├── text_extraction.py   # Text extraction services
│   ├── summarization.py     # Summarization services
│   ├── expert_selection.py  # Expert selection services
│   ├── image_generation.py  # Expert image generation services
│   ├── gap_identification.py # Research gap identification services
│   ├── hypothesis_generation.py  # Hypothesis generation services
│   ├── workflow_generation.py    # Workflow generation services
│   └── paper_search.py      # Related paper search services
├── requirements.txt         # Python dependencies
├── style.css                # Custom CSS for the app
├── images/                  # Folder containing images for the app
│   └── banner.png           # Banner image for the home page
└── .streamlit/              # Streamlit configuration files
    ├── secrets.toml         # API keys and secrets
    └── config.toml          # Streamlit theme and config settings
```

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/ai_research_mentor.git
cd ai_research_mentor
```

### 2. Set up a Python virtual environment (optional but recommended)

- **On Windows:**

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **On macOS/Linux:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install dependencies

Install the necessary Python dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Set up API keys

Create a `.streamlit/secrets.toml` file in the `.streamlit` directory to store your **OpenAI API key**:

```toml
[openai]
api_key = "your-openai-api-key"
```

### 5. Run the application

Start the Streamlit app by running the following command:

```bash
streamlit run app.py
```

---

## Usage

1. **Home**: A brief introduction to the application and its functionalities. Click **Get Started** to begin.
2. **Upload Document**: Upload a research document (PDF or DOCX).
3. **Summary**: View a summarized version of the uploaded document.
4. **Research Gaps**: Identify gaps in the research based on the document.
5. **Hypotheses**: Generate testable hypotheses from the identified gaps.
6. **Workflow**: Generate an experimental workflow to test the selected hypothesis.
7. **Related Papers**: Find related papers to support your hypothesis.
8. **Expert Chat**: Simulate an expert consultation based on the hypothesis.

---

## API Usage

The project leverages **OpenAI GPT-4** for summarization, research gap identification, hypothesis generation, and expert simulation. The **CrossRef API** is used to search for related research papers.

### 1. OpenAI GPT-4 Integration
- Extracts content from uploaded documents
- Summarizes key points
- Identifies research gaps
- Generates hypotheses
- Simulates expert conversations

### 2. CrossRef API Integration
- Finds related papers based on the generated hypotheses

---

## Customization

### Theme Customization
You can customize the appearance of the app by modifying `.streamlit/config.toml` and the `style.css` file.

### Adding New Features
New features can be added by creating new service files in the `services` directory and adding the corresponding UI elements in `app.py` and the `routers/` directory.

---

## Troubleshooting

1. **Missing API Key**: Make sure to add your OpenAI API key in `.streamlit/secrets.toml`.
2. **Python Version**: Ensure that you're using Python 3.7 or higher.
3. **Dependency Issues**: If any dependencies fail to install, try updating `pip` and reinstalling the requirements.

---

## Contributing

Feel free to submit issues or pull requests. Contributions are always welcome!

---

## License

This project is licensed under the MIT License.

---

## Contact

For any inquiries or questions, please contact [Your Name](mailto:evon@protonmail.com).
