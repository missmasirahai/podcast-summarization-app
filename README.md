# 🎙️ Podcast Summarization App

An AI-powered podcast summarizer built with Flask, Google Gemini API, and OpenAI Whisper.

## Features
- Paste any podcast transcript and get an instant AI summary
- Upload audio files (.mp3, .wav, .m4a) for automatic transcription
- Structured output: summary, key insights, top quotes, topics covered
- Sentiment analysis for each episode

## Tech Stack
- Backend: Python, Flask
- AI Summarization: Google Gemini API
- Audio Transcription: OpenAI Whisper
- Frontend: HTML, CSS, Vanilla JavaScript

## How to Run Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Gemini API key to `backend/.env`
4. Run: `python backend/app.py`
5. Open `frontend/index.html` in browser

## Deployment
- Backend deployed on Render
- Frontend deployed on Vercel
