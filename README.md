# Podcast Summarization App

A web app that transcribes audio from podcast URLs and generates 
AI-powered summaries using OpenAI Whisper and Gemini API.

## Live Demo
[Click here to try the app](https://podcast-summarization-app.vercel.app)

## Tech Stack
- Python, Flask (backend)
- OpenAI Whisper (audio transcription)
- Google Gemini API (summarization)
- HTML, CSS, JavaScript (frontend)
- Deployed on Render + Vercel

## Features
- Paste any podcast URL
- Get full transcript
- Get a clean AI summary in seconds

## How to Run Locally
1. Clone this repo
2. pip install -r requirements.txt
3. Add GEMINI_API_KEY to .env file
4. python app.py
3. Add your Gemini API key to `backend/.env`
4. Run: `python backend/app.py`
5. Open `frontend/index.html` in browser

## Deployment
- Backend deployed on Render
- Frontend deployed on Vercel
