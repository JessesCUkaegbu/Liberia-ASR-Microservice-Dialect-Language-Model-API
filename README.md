# Liberia-ASR-Microservice-Dialect-Language-Model-API
🎙️ ASR Microservice — Speech-to-Text API with Whisper  A lightweight Automatic Speech Recognition (ASR) microservice built with Flask and Faster-Whisper. Users can upload audio files (.wav or .mp3) through a web interface or API endpoint and receive fast, accurate transcriptions in real time.

## 🚀 Features

- Upload audio files via browser or REST API  
- Fast transcription using OpenAI Whisper models  
- CPU-friendly (runs without GPU)  
- Simple web UI for file upload  
- Easy public access using ngrok  
- JSON API responses  

---

## 🏗️ Architecture
Flask API Server → Whisper Model → Transcription JSON


## 📦 Tech Stack

- Python 3.10+
- Flask
- Faster-Whisper
- Pyngrok (for public access)
- FFmpeg / PyAV (audio decoding)

---

## 🔧 Installation

### 1. Create virtual environment

bash
python -m venv asr_env
source asr_env/bin/activate

Install dependencies

pip install faster-whisper flask pyngrok soundfile

Generate the requirements.txt file

pip install -r requirements.txt

Running the Server
python app.py
