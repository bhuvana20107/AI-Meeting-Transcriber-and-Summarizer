# Meeting Summarizer using Whisper + LLM
`````````````````````````````````````````````
An **AI-powered meeting summarization tool** built with **Chainlit**, **OpenAI Whisper**, and **Hugging Face Transformers**.  
It automatically **transcribes meeting audio/video files**, **summarizes discussions**, and **extracts key decisions and action items** — all in one simple interface.

---

# Features

✅ **Automatic Speech Recognition (ASR)** using Whisper  
✅ **Summarization using BART (Hugging Face)**  
✅ **Key Decision & Action Item Extraction**  
✅ **Interactive Chainlit UI** for file uploads  
✅ **Transcript, Summary, and JSON output storage**  
✅ **Fast and lightweight — runs locally**

---

# Objective

Transcribe meeting audio and generate **action-oriented summaries** that highlight:
- Key points discussed  
- Final decisions taken  
- Follow-up actions or tasks  

---

# Tech Stack

| Component     | Technology Used  |
|---------------|------------------|
| Frontend      | Chainlit         |
| Backend       | Python           |
| ASR           | OpenAI Whisper   |
| NLP Model     | Facebook BART    |
| File Handling | Tempfile + OS    |
| Output Format | `.txt` + `.json` |


# Installation & Setup
1) Installation

Clone the repository:
```bash
git clone https://github.com/bhuvana20107/AI-Meeting-Transcriber-and-Summarizer.git
cd AI-Meeting-Transcriber-and-Summarizer

2) Create a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows

3) Install dependencies:

pip install -r requirements.txt


4) Run the app:

chainlit run app.py  #Then open the local URL shown in your terminal to use the web interface.

 How It Works

1> Upload your MP3 or MP4 meeting recording.
2> The app transcribes it using Whisper.
3> The transcript is summarized using BART (LLM).
4> Extracts Key Decisions and Action Items automatically.
5> Saves all results in the outputs/ folder.


# Output Files
All outputs are saved automatically inside the outputs/ folder as:
    outputs/
    ├── meeting1_transcript.txt
    ├── meeting1_summary.txt
    ├── meeting1_meta.json

