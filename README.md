Meeting Transcriber & Summarizer
````````````````````````````````
Objective
---------
Automatically transcribe meeting audio and generate action-oriented summaries — including key decisions and action items.

Features
--------
1) Audio transcription using OpenAI Whisper / Hugging Face ASR

2) Smart summarization via LLM (Hugging Face model)

3) Saves transcript, summary, and action items in /outputs folder

4) Chat-based interface using Chainlit

Tech Stack
----------
1) Python 3.10+

2) Chainlit (Frontend & chat interface)

3) Whisper / Hugging Face Transformers (Speech-to-text)

4) Transformers / Hugging Face pipeline (Summarization)

5)JSON & File I/O for persistent storage

Setup Instructions
------------------
Install Requirements
    pip install -r requirements.txt
Run the App
    chainlit run app.py -w
Upload an Audio File
    App transcribes and summarizes automatically.
    Outputs saved in /outputs folder:
        <filename>_transcript.txt
        <filename>_summary.txt
        <filename>_meta.json


# 🎯 Meeting Summarizer using Whisper + LLM

An **AI-powered meeting summarization tool** built with **Chainlit**, **OpenAI Whisper**, and **Hugging Face Transformers**.  
It automatically **transcribes meeting audio/video files**, **summarizes discussions**, and **extracts key decisions and action items** — all in one simple interface.

---

## 🚀 Features

✅ **Automatic Speech Recognition (ASR)** using Whisper  
✅ **Summarization using BART (Hugging Face)**  
✅ **Key Decision & Action Item Extraction**  
✅ **Interactive Chainlit UI** for file uploads  
✅ **Transcript, Summary, and JSON output storage**  
✅ **Fast and lightweight — runs locally**

---

## 🧠 Objective

Transcribe meeting audio and generate **action-oriented summaries** that highlight:
- Key points discussed  
- Final decisions taken  
- Follow-up actions or tasks  

---

## 🧩 Tech Stack

| Component     | Technology Used  |
|---------------|------------------|
| Frontend      | Chainlit         |
| Backend       | Python           |
| ASR           | OpenAI Whisper   |
| NLP Model     | Facebook BART    |
| File Handling | Tempfile + OS    |
| Output Format | `.txt` + `.json` |


## 🛠️ Installation & Setup
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


📂 Output Files

All outputs are saved automatically inside the outputs/ folder as:

outputs/
 ├── meeting1_transcript.txt
 ├── meeting1_summary.txt
 ├── meeting1_meta.json

🧩 Example Prompt Used for LLM

“Summarize this meeting transcript into key decisions and action items.”

🧪 Example Output

📘 Summary:

The team discussed upcoming release timelines and decided to extend the testing phase by one week.

🎯 Key Decisions:

The release will be postponed by a week.

✅ Action Items:

QA team to rerun integration tests.

PM to update the project timeline in Jira.



