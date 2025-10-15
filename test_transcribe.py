import subprocess
import whisper
import os
import sys
from transformers import pipeline

# 1️⃣ Automatically locate FFmpeg
def find_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "ffmpeg"
    except FileNotFoundError:
        local_path = os.path.join(os.path.dirname(__file__), "ffmpeg", "bin", "ffmpeg.exe")
        if os.path.exists(local_path):
            os.environ["PATH"] += os.pathsep + os.path.dirname(local_path)
            return local_path
        else:
            print("❌ FFmpeg not found. Please download and place it in the project folder under 'ffmpeg/bin/'.")
            sys.exit(1)

ffmpeg_path = find_ffmpeg()
print(f"✅ Using FFmpeg: {ffmpeg_path}")

# 2️⃣ Audio file (raw string to avoid escape issues)
audio_file = r"audio\Record (online-voice-recorder.com).mp3"

# 3️⃣ Load Whisper model
print("🎧 Loading Whisper model (base)...")
model = whisper.load_model("base")

# 4️⃣ Transcribe function
def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

# 5️⃣ Run transcription
print("🎙️ Transcribing audio...")
transcript = transcribe_audio(audio_file)

# 6️⃣ Output transcript
print("✅ Transcription complete!\n")
print("📝 Transcript:\n", transcript)

# 7️⃣ Initialize Hugging Face summarizer
print("\n📝 Generating summary...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 8️⃣ Generate summary
summary_result = summarizer(transcript, max_length=150, min_length=30, do_sample=False)
summary_text = summary_result[0]['summary_text']

print("\n📝 Summary:\n", summary_text)

# 9️⃣ Generate action items
action_items = ["- " + sentence.strip() for sentence in summary_text.split('.') if sentence]

print("\n✅ Action Items:")
for item in action_items:
    print(item)
