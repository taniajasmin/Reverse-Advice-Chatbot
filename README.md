# Reverse-Advice-Chatbot

Welcome to the **Reverse Advice Chatbot**, a Flask-based web application that provides valuable advice to your problems. Built with a touch of humor, this chatbot remembers your past interactions and responds with ridiculous suggestions to keep you entertained!

## Features
- **Interactive Chat**: Enter your problems and get hilariously bad advice in real-time.
- **Memory**: The chatbot remembers your previous questions and responses across sessions.
- **Responsive UI**: A simple, user-friendly interface with distinct message bubbles for user and bot interactions.

## Prerequisites
- Python 3.x
- Internet connection (for OpenAI API calls)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/taniajasmin/reverse-advice-chatbot.git
   cd reverse-advice-chatbot
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

5. **Run the Application**
   ```bash
   python app.py
   ```
   Open your browser and visit `http://127.0.0.1:5000/` to start chatting!

## Usage
- Type your problem in the input field (e.g., "My eyes hurt" or "I wanna go home").
- Click "Send" to receive terrible advice (e.g., "Stare directly at the sun!" or "Knock over coffee on your boss's desk!").
- The chat history will persist, and you can manage memory by clicking the book icon beneath a message or disabling it in settings.

## Project Structure
```
REVERSE-ADVICE
├── static/
│   └── style.css         # CSS for styling the UI
├── templates/
│   └── index.html        # HTML template for the chatbot
├── .env                  # Environment variables (e.g., API key)
├── app.py                # Main Flask application
├── advice_engine.py      # Logic for generating bad advice (optional, if separate)
└── requirements.txt      # Python dependencies
```

## Dependencies
- `flask`
- `python-dotenv`
- `openai`

## Acknowledgments
- Built with Flask and the OpenAI API.
- Built with OpenAI API.
