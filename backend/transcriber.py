import whisper
import os
import subprocess

# Get the exact ffmpeg exe path
FFMPEG_PATH = "C:\\Users\\Usaid\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages\\imageio_ffmpeg\\binaries\\ffmpeg-win-x86_64-v7.1.exe"

# Patch whisper to use our ffmpeg directly
import whisper.audio
original_load_audio = whisper.audio.load_audio

def patched_load_audio(file, sr=16000):
    cmd = [
        FFMPEG_PATH,
        "-nostdin",
        "-threads", "0",
        "-i", file,
        "-f", "s16le",
        "-ac", "1",
        "-acodec", "pcm_s16le",
        "-ar", str(sr),
        "-"
    ]
    out = subprocess.run(cmd, capture_output=True, check=True).stdout
    import numpy as np
    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0

whisper.audio.load_audio = patched_load_audio

print("✅ ffmpeg patched successfully!")

model = whisper.load_model("base")

def transcribe_audio(audio_file_path):
    print(f"Transcribing audio file: {audio_file_path}")
    result = model.transcribe(audio_file_path)
    transcript = result["text"]
    print("✅ Transcription complete!")
    return transcript

def cleanup_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted temporary file: {file_path}")

def cleanup_file(file_path):
    import time
    time.sleep(1)  # Wait 1 second for Whisper to release the file
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted temporary file: {file_path}")
    except Exception as e:
        print(f"Could not delete file (will be cleaned later): {e}")