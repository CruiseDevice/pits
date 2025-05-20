# P.I.T.S. - Personalized Intelligent Tutoring System

PITS is an AI-powered tutoring system that creates customized learning experiences based on your uploaded materials. The system processes your documents, generates a structured course with slides and narration, and provides an interactive chatbot that answers questions about the material.

![PITS Workflow](https://github.com/yourusername/pits/raw/main/images/pits_workflow.png)

## Features

- **Personalized Learning**: Adapts to your knowledge level and learning goals
- **Document Processing**: Upload and process your own study materials in various formats
- **Interactive Quizzes**: Assess your knowledge with AI-generated quizzes
- **Structured Course Material**: Automatically generates slides with key bullet points
- **AI Tutor**: Chat with a personalized tutor that understands the context of your learning material
- **Session Management**: Resume your learning sessions whenever you want

## How It Works

1. **Onboarding**: Tell PITS your name, what you want to study, and your learning goals
2. **Upload Materials**: Provide your study documents (PDFs, Word documents, text files)
3. **Assessment**: Take a quiz to assess your current knowledge level or select it manually
4. **Learning**: Navigate through AI-generated slides with an interactive chatbot to answer your questions
5. **Progress Tracking**: Your learning sessions are saved so you can continue where you left off

## Technical Architecture

PITS leverages several key technologies:

- **LlamaIndex**: For document ingestion, knowledge extraction, and querying
- **OpenAI GPT-4**: Powers the conversational tutoring interface
- **Streamlit**: Provides the web-based user interface
- **Vector and Tree Indexes**: Enable efficient knowledge retrieval from your documents

## Installation

### Prerequisites
- Python 3.9+
- OpenAI API key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/CruiseDevice/pits.git
cd pits
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create the necessary folders if they don't exist:
```bash
mkdir -p cache index_storage ingestion_storage session_data
```

4. Run the application:
```bash
streamlit run app.py
```

5. On first launch, you'll be asked to enter your OpenAI API key

## Usage Guide

### Getting Started

1. Enter your name and the subject you want to study
2. Specify any learning goals you have (optional)
3. Upload your study materials
4. Choose your current knowledge level or take a quiz for assessment
5. Wait for the system to process your documents and generate the course material

### During Learning

- Navigate through slides using the number input in the sidebar
- Toggle narration on/off with the button provided
- Ask questions to the PITS chatbot about the current slide or general concepts
- Use the session management options to resume or start a new session

## File Structure

- `app.py`: Main application entry point
- `conversation_engine.py`: Chatbot functionality
- `document_uploader.py`: Document ingestion and processing
- `global_settings.py`: Application settings
- `index_builder.py`: Knowledge index construction
- `logging_functions.py`: Activity logging
- `quiz_UI.py`: Quiz interface
- `quiz_builder.py`: Quiz generation
- `session_functions.py`: Session state management
- `slides.py`: Slide deck implementation
- `training_UI.py`: Learning interface
- `training_material_builder.py`: Course content generation
- `user_onboarding.py`: User setup process

## Limitations

- Currently requires an OpenAI API key
- Processing large documents may take time
- The conversation storage is currently not fully working (noted in the code)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Insert your preferred license here]

## Acknowledgments

- LlamaIndex for providing the document indexing framework
- OpenAI for the GPT-4 model that powers the tutoring capability
- Streamlit for the interactive UI framework