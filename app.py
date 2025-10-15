import chainlit as cl
import tempfile
import whisper
import os
import warnings
import json
from transformers import pipeline

# ----------------------------
# INITIAL SETUP
# ----------------------------
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

# Load Whisper (ASR model)
model = whisper.load_model("base")

# Load Hugging Face summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ----------------------------
# HELPER FUNCTION
# ----------------------------
def generate_summary_and_actions(text):
    # Summarize text using BART
    summary = summarizer(text, max_length=200, min_length=60, do_sample=False)[0]["summary_text"]

    # Basic extraction of key decisions and action items
    decisions = [line.strip() for line in text.split(".") if "decided" in line.lower() or "conclude" in line.lower()]
    actions = [line.strip() for line in text.split(".") if "will" in line.lower() or "need to" in line.lower()]

    return summary, decisions, actions

# ----------------------------
# CHAINLIT INTERFACE
# ----------------------------
@cl.on_chat_start
async def start():
    await cl.Message(
        content="",
        elements=[
            cl.Image(name="App Logo", display="inline", path="logo.png", size="small"),
        ]
    ).send()

    await cl.Message(
        content="👋 **Welcome to Meeting Summarizer!**\n\nUpload your meeting audio or video file (MP3 or MP4) to get transcript, summary, key decisions, and action items."
    ).send()


@cl.on_message
async def handle_message(message: cl.Message):
    # Step 1: Ensure file uploaded
    if not message.elements:
        await cl.Message(content="❌ Please upload an MP3 or MP4 file first.").send()
        return

    file = message.elements[0]

    # Step 2: Save uploaded file
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, file.name)

    if hasattr(file, "content") and file.content:
        with open(file_path, "wb") as f:
            f.write(file.content)
    elif hasattr(file, "path") and os.path.exists(file.path):
        file_path = file.path
    else:
        await cl.Message(content="⚠️ Failed to read uploaded file. Please re-upload.").send()
        return

    await cl.Message(content=f"✅ File '{file.name}' uploaded successfully! Starting transcription...").send()

    try:
        # Step 3: Transcribe
        result = model.transcribe(file_path)
        transcript = result["text"].strip()

        # Step 4: Generate AI summary, decisions, actions
        hf_summary, decisions, actions = generate_summary_and_actions(transcript)

        # Step 5: Display results
        final_message = (
            "📝 **Transcript (first 1200 chars):**\n"
            + (transcript[:1200] + ("..." if len(transcript) > 1200 else ""))
            + "\n\n📘 **Summary:**\n"
            + hf_summary
            + "\n\n"
        )

        if decisions:
            final_message += "🎯 **Key Decisions:**\n" + "\n".join([f"- {d}" for d in decisions]) + "\n\n"
        if actions:
            final_message += "✅ **Action Items:**\n" + "\n".join([f"- {a}" for a in actions]) + "\n\n"

        await cl.Message(content=final_message).send()

        # Step 6: Save outputs
        os.makedirs("outputs", exist_ok=True)
        base = os.path.join("outputs", os.path.splitext(file.name)[0])

        with open(base + "_transcript.txt", "w", encoding="utf-8") as f:
            f.write(transcript)
        with open(base + "_summary.txt", "w", encoding="utf-8") as f:
            f.write(
                hf_summary
                + "\n\nKey Decisions:\n"
                + "\n".join(decisions)
                + "\n\nAction Items:\n"
                + "\n".join(actions)
            )
        with open(base + "_meta.json", "w", encoding="utf-8") as f:
            json.dump(
                {
                    "transcript": transcript,
                    "summary": hf_summary,
                    "decisions": decisions,
                    "actions": actions,
                },
                f,
                indent=2,
            )

        # ✅ Show saved file location inside Chainlit
        await cl.Message(
            content=f"💾 **Files saved in:** `outputs/{file.name.split('.')[0]}_*`\n\nYou can check the folder for:\n- Transcript (.txt)\n- Summary (.txt)\n- Metadata (.json)"
        ).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {e}").send()
