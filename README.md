📄 AI Resume Analyzer

An AI-powered web application that analyzes a resume and provides structured feedback using multiple AI agents.

📌 Project Overview

The AI Resume Analyzer allows a user to upload a resume as a .txt file and analyzes it using three specialized AI agents:

Resume Analysis Agent

Skills Analysis Agent

Career Recommendation Agent

The project is designed to provide short, focused results instead of rewriting the complete resume.

🛠️ Technologies Used

Python

Streamlit

OpenAI Swarm

Ollama

Llama 3.2

🤖 AI Model

Model: Llama 3.2

The application uses a local Ollama-compatible endpoint:

http://localhost:11434/v1

The model is used through the Swarm framework.

👨‍💼 AI Agents

1. Resume Analysis Agent

Analyzes the uploaded resume and provides:

Education

Experience

Main Projects

One Strength and One Weakness

The agent uses short bullet points and does not rewrite the resume.

2. Skills Analysis Agent

Analyzes the resume and provides:

Technical Skills

Soft Skills

Two Recommended Skills to Learn

The output is kept short and does not invent information.

3. Career Recommendation Agent

Analyzes the resume and provides:

Three suitable entry-level job roles

Two resume improvement suggestions

The recommendations are intended to be realistic for a beginner.

🔄 Project Workflow

Upload Resume
      ↓
Read Resume Text
      ↓
Resume Analysis Agent
      ↓
Skills Analysis Agent
      ↓
Career Recommendation Agent
      ↓
Display Results

🌐 Web Interface

The Streamlit interface provides:

📄 AI Resume Analyzer dashboard

📤 Resume upload

🤖 Three AI agents

🧠 Llama 3.2 model

📋 Resume analysis

🛠️ Skills analysis

💼 Career recommendations

📄 Uploaded resume preview

📁 Project Structure

AI-Resume-Analyzer/
│
├── ai-resume-analyzer.py
├── agents.py
├── resume.txt
├── requirements-ai-resume-analyzer.txt
└── README.md

💻 Installation

Install the required packages:

pip install -r requirements-ai-resume-analyzer.txt

The requirements file should contain:

streamlit
openai
git+https://github.com/openai/swarm.git

⚙️ Ollama Setup

Make sure Ollama is installed and running locally.

The project expects the Llama 3.2 model to be available.

The application connects to:

http://localhost:11434/v1

▶️ Run the Application

Start the Streamlit application with:

streamlit run ai-resume-analyzer.py

Then open the Streamlit URL shown in the terminal.

📤 Input

The application accepts:

.txt

resume files.

📋 Output

After analysis, the application displays three sections:

Resume Analysis
Skills Analysis
Career Recommendations

It also provides an option to view the uploaded resume.

🎯 Purpose

The project demonstrates how multiple specialized AI agents can be combined in a web application to analyze a resume and provide structured career-related feedback.

⚠️ Note

The recommendations are generated from the information available in the uploaded resume. The system is intended for educational and demonstration purposes and should not be treated as a professional hiring or career decision system.

👨‍💻 Author

Maaz Khan
