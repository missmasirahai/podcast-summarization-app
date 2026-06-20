from google import genai
import os
from dotenv import load_dotenv

# Load .env from the backend folder
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: GEMINI_API_KEY not found in .env file!")
else:
    print("✅ Gemini API key loaded successfully!")

client = genai.Client(api_key=api_key)

def summarize_transcript(transcript_text):
    prompt = f"""
You are an expert podcast summarizer.

Given the following podcast transcript, return a structured JSON response with exactly these fields:

{{
  "title": "A short catchy title for this podcast episode",
  "summary": "A 3-4 sentence overview of the full episode",
  "key_insights": [
    "Insight 1",
    "Insight 2",
    "Insight 3",
    "Insight 4",
    "Insight 5"
  ],
  "top_quotes": [
    "Quote 1 from the transcript",
    "Quote 2 from the transcript"
  ],
  "topics_covered": [
    "Topic 1",
    "Topic 2",
    "Topic 3"
  ],
  "sentiment": "Positive / Negative / Neutral / Mixed"
}}

Return ONLY the JSON. No explanation. No extra text. No markdown backticks.

TRANSCRIPT:
{transcript_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text