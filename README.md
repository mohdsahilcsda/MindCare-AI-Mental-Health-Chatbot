# 🧠 MindCare AI - Mental Health Support Chatbot
## Project Overview

MindCare AI is a simple AI-powered chatbot designed to provide general emotional support through conversational interaction.

The chatbot uses Python, Flask, and the Hugging Face Transformers library with the Microsoft DialoGPT-small model. It also includes basic safety filtering and chat session logging.

> **Note:** This chatbot provides general emotional support and is not a replacement for professional care.

## Features

* AI-based conversational interaction
* General emotional support responses
* Basic NLP safety filtering
* Supportive responses for stress, anxiety, sadness, and loneliness
* Hugging Face DialoGPT-small model integration
* Flask-based web application
* Simple chatbot user interface
* Local chat session logging
* Responsive and easy-to-use interface

## Technologies Used

* **Python** — Core programming language
* **Flask** — Web application and API backend
* **Hugging Face Transformers** — NLP and conversational AI
* **Microsoft DialoGPT-small** — Conversational language model
* **PyTorch** — Deep learning framework used with the model
* **HTML, CSS, JavaScript** — Frontend interface

## Project Structure

```text
AI_Mental_Health_Chatbot/
│
├── app.py
├── README.md
├── chat_logs.txt
├── data/
├── model/
└── venv/
```

### Main Files

* `app.py` — Main Flask application and chatbot logic
* `README.md` — Project documentation
* `chat_logs.txt` — Stores local chatbot session logs
* `data/` — Dataset/data files
* `model/` — Model-related files
* `venv/` — Python virtual environment

## How It Works

1. The user opens the MindCare AI chatbot web interface.
2. The user enters a message in the chat box.
3. The Flask backend receives the message.
4. Basic keyword-based safety filtering checks the input.
5. Supportive responses are provided for common emotional situations.
6. For other messages, the DialoGPT-small model generates a conversational response.
7. The chatbot response is displayed on the frontend.
8. The conversation is stored locally in `chat_logs.txt` for session logging.

## Installation & Setup

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create and activate the virtual environment

```bash
python -m venv venv
```

For Command Prompt:

```bash
venv\Scripts\activate.bat
```

### 3. Install required libraries

```bash
python -m pip install flask transformers torch
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the chatbot

Open the local Flask URL shown in the terminal and start chatting with MindCare AI.

## Project Workflow

The project follows these main stages:

**User Input → Safety Filter → Supportive Response / AI Response → Frontend Display → Session Logging**

This workflow combines predefined supportive responses with the DialoGPT-small conversational model to create a simple emotional-support chatbot.

## Conclusion

MindCare AI demonstrates how conversational AI can be used to provide simple, supportive interactions through a web-based chatbot.

The project helped in understanding Flask web development, Hugging Face Transformers, conversational AI models, basic NLP safety filtering, and session logging.

The chatbot is intended for general emotional support and should not be considered a replacement for professional mental health care.
