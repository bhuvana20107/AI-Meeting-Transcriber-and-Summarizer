import os
os.environ["FFMPEG_BINARY"] = r"C:\Users\kbhuv\OneDrive\Desktop\ffmpeg-8.0-essentials_build\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

import whisper

def transcribe_audio(audio_path):
    if not os.path.exists(audio_path):
        print(f"❌ Audio file not found: {audio_path}")
        return ""

    print("🎧 Loading Whisper model (base)...")
    model = whisper.load_model("base")

    print("🎙️ Transcribing audio...")
    result = model.transcribe(audio_path)

    print("✅ Transcription complete!")
    return result["text"]
