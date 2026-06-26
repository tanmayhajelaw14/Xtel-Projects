import whisper
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
print("HF_TOKEN loaded:", os.getenv("HF_TOKEN"))
# ------------------------
# Whisper
# ------------------------

model = whisper.load_model("base")

result = model.transcribe("patient.wav")

transcript = result["text"]

print("\nPatient:")
print(transcript)


# ------------------------
# LLM
# ------------------------

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)

system_prompt = """
You are Sarah, a professional dental clinic receptionist.

Rules:
- Introduce yourself as Sarah.
- Keep responses under 3 sentences.
- Never invent doctors, appointment slots, clinic timings, room numbers, prices, or patient information.
- Only use information explicitly provided by the user or external systems.
- If appointment availability is requested and no scheduling data is available, state that you do not currently have access to the clinic schedule and ask for contact details so clinic staff can follow up.
- If information is unavailable, say so explicitly instead of guessing.
- Remain concise and professional.
"""

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct:featherless-ai",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": transcript
        }
    ],
    max_tokens=100
)

reply = response.choices[0].message.content

print("\nSarah:")
print(reply)