# JS + Python AI Voice Agents

An experimental project that integrates JavaScript, Python, and AI to create interactive voice agents. This project showcases the use of frontend technologies for voice input/output and backend AI processing using Python, making it possible to build voice-based AI applications for the web.

## 🧠 Features

- Voice interaction using Web APIs
- Backend integration with AI models (e.g., LLMs)
- Modular and extensible Python backend
- Simple UI using HTML/CSS/JS/TypeScript
- API endpoints for handling voice and prompt data

## 📁 Project Structure

JSPythonAIVoiceAgents/
├── frontend/ # HTML, CSS, JS/TS frontend code
├── api.py # Python FastAPI/Flask backend (handles AI requests)
├── db.py # Simple database handler or memory store
├── prompts.txt # Sample prompts or memory context
├── requirements.txt # Python dependencies


## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js (optional, for TypeScript build or frontend dev)
- A virtual environment (recommended)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/SamraAzizi/JSPythonAIVoiceAgents.git
cd JSPythonAIVoiceAgents
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the backend**
```bash

python api.py
```

5. **Open the frontend**
Open frontend/index.html in your browser (or serve it using a local server like Live Server in VS Code).


### Tech Stack
- Frontend: HTML, CSS, JavaScript, TypeScript
- Backend: Python (FastAPI or Flask)
- Voice APIs: Web Speech API (SpeechRecognition + SpeechSynthesis)
- AI Models: Can be integrated via OpenAI, Hugging Face, or local LLMs

### Usage

- Click the "Speak" button on the frontend to record your voice.
- The voice is transcribed and sent to the backend.
- The backend generates a response using an AI model.
- The response is spoken aloud using the browser's SpeechSynthesis API.

