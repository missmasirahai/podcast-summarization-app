import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from summarizer import summarize_transcript
try:
    from transcriber import transcribe_audio, cleanup_file
    WHISPER_AVAILABLE = True
except Exception:
    WHISPER_AVAILABLE = False
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"mp3", "wav", "m4a"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Route 1 — Summarize from pasted text
@app.route("/summarize-text", methods=["POST"])
def summarize_text():
    try:
        data = request.get_json()
        transcript = data.get("transcript", "")

        if not transcript.strip():
            return jsonify({"error": "No transcript provided"}), 400

        result = summarize_transcript(transcript)
        parsed = json.loads(result)

        return jsonify({"success": True, "data": parsed})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route 2 — Summarize from uploaded audio file
@app.route("/summarize-audio", methods=["POST"])
def summarize_audio():
    if not WHISPER_AVAILABLE:
        return jsonify({"error": "Audio transcription is not available on this server. Please use the text paste option."}), 503

    try:
        if "audio" not in request.files:
            return jsonify({"error": "No audio file uploaded"}), 400

        file = request.files["audio"]

        if not allowed_file(file.filename):
            return jsonify({"error": "Only mp3, wav, m4a files allowed"}), 400

        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        transcript = transcribe_audio(filepath)
        cleanup_file(filepath)

        result = summarize_transcript(transcript)
        parsed = json.loads(result)

        return jsonify({
            "success": True,
            "transcript": transcript,
            "data": parsed
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route 3 — Health check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Podcast Summarizer API is running!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)