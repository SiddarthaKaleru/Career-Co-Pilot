# CAREER CO-POLIT 🤖

Welcome to the AI Assistant Hub, a powerful Streamlit web application that leverages a multi-agent AI system built with **CrewAI** and powered by the lightning-fast **Groq API**. This hub provides a suite of intelligent tools designed to streamline complex tasks, starting with an expert-level resume analysis system.

*(**Note**: You can replace the URL above with a screen recording/GIF of your application in action.)*

## Table of Contents

  - [Features](https://www.google.com/search?q=%23features)
  - [Tech Stack](https://www.google.com/search?q=%23tech-stack)
  - [Project Structure](https://www.google.com/search?q=%23project-structure)
  - [Setup & Installation](https://www.google.com/search?q=%23setup--installation)
  - [How to Run](https://www.google.com/search?q=%23how-to-run)
  - [How It Works: The AI Crew](https://www.google.com/search?q=%23how-it-works-the-ai-crew)
  - [License](https://www.google.com/search?q=%23license)

-----

## Features

The AI Assistant Hub currently offers two primary tools:

### 1\. ATS Resume Expert 📄🔍

A sophisticated resume analyzer that simulates an Applicant Tracking System (ATS) and provides feedback from a team of specialized AI agents.

  - **Multi-Agent Analysis**: Utilizes a crew of four distinct AI agents, each with a specific role (parsing, scoring, summarizing, and compiling).
  - **Comprehensive Reporting**: Delivers a single, cohesive report that includes:
      - **Parsed Resume Data**: Structured extraction of contact info, experience, skills, etc.
      - **ATS Match Score**: A percentage score indicating alignment with the job description, along with a rationale.
      - **In-Depth Fit Summary**: A qualitative analysis of strengths, weaknesses, and actionable improvement suggestions.
  - **PDF Upload**: Seamlessly processes resumes uploaded in PDF format.
  - **Fast & Powerful**: Powered by Groq's API for near-instantaneous LLM inference.

### 2\. AI Conversational ChatBot 💬

A responsive and intelligent chatbot for general-purpose tasks, powered by Groq and Llama 3.

  - **Real-time Interaction**: Engage in fluid conversations for content creation, brainstorming, or question-answering.
  - **Session History**: Remembers the context of your conversation within a session.

-----

## Tech Stack

This project is built with a modern, AI-centric Python stack:

  - **Web Framework**: [Streamlit](https://streamlit.io/)
  - **AI Agent Framework**: [CrewAI](https://www.crewai.com/)
  - **LLM Provider**: [Groq](https://groq.com/)
  - **Core Language**: Python
  - **Key Libraries**:
      - `python-dotenv` for environment management.
      - `PyMuPDF` for robust PDF text extraction.
      - `langchain-groq` for seamless LLM integration.

-----

## Project Structure

The project is organized into modules for clarity and scalability:

```
/AI-Assistant-Hub
├── app.py                  # Main Streamlit hub entry point
├── agents.py               # Defines the CrewAI agents
├── tasks.py                # Defines the CrewAI tasks
├── .env                    # Stores API keys and environment variables
├── requirements.txt        # Project dependencies
├── /pages
│   ├── 1_ATS.py            # Streamlit page for the ATS tool
│   └── 2_ChatBot.py        # Streamlit page for the ChatBot
└── /tools
    └── file_read_tool.py   # Custom tool for reading PDF files
```

-----

## Setup & Installation

Follow these steps to get the AI Assistant Hub running on your local machine.

### 1\. Clone the Repository

```bash
git clone https://github.com/your-username/ai-assistant-hub.git
cd ai-assistant-hub
```

### 2\. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv myenv
myenv\Scripts\activate

# For macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

### 3\. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4\. Set Up Your Environment Variables

You'll need a Groq API key to power the AI agents.

1.  **Get a Groq API Key**:

      * Go to the [Groq Console](https://console.groq.com/).
      * Sign up or log in.
      * Navigate to the "API Keys" section and create a new secret key.

2.  **Create a `.env` file** in the root directory of the project.

3.  **Add your API key** to the `.env` file:

    ```env
    GROQ_API_KEY="gsk_YourSecretGroqApiKeyHere"
    ```

-----

## How to Run

Once the setup is complete, you can launch the Streamlit application with a single command:

```bash
streamlit run app.py
```

Your web browser should automatically open to the application's main page.

-----

## How It Works: The AI Crew

The core of the ATS Resume Expert is a sequential crew of AI agents, where the output of one task becomes the context for the next.

1.  **Resume Information Parser (`data_extractor`)**:

      - **Goal**: Reads the raw text from the uploaded PDF.
      - **Task**: Extracts key information (experience, skills, education) and structures it into a clean markdown format.

2.  **Advanced ATS Simulator (`ats_analyst`)**:

      - **Goal**: Scores the resume against the job description.
      - **Task**: Takes the parsed resume data as context, calculates a precise match percentage, and provides a rationale for the score.

3.  **Resume Evaluation Expert (`resume_screener`)**:

      - **Goal**: Provides a qualitative, human-like review.
      - **Task**: Uses the parsed data and ATS score as context to write a comprehensive fit summary, analyze skill matches, and suggest specific improvements.

4.  **Final Report Compiler (`final_report_compiler`)**:

      - **Goal**: To synthesize all analyses into a final document.
      - **Task**: Takes the outputs of all previous tasks and compiles them into a single, cohesive, and professionally formatted report for the user.

This sequential process ensures that each agent builds upon the work of the previous one, resulting in a detailed and context-aware final analysis.

-----

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
