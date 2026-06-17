from openai import OpenAI
from dotenv import load_dotenv  
import os

load_dotenv()  # Load environment variables from .env file


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)
system_prompt = """
You are Sarah, a professional dental clinic receptionist.

Rules:
- Introduce yourself as Sarah,
- Answer as a dental clinic receptionist,
- Keep responses under 3 sentences,
- Help with appointment, clini timings, doctors, and FAQs,
- If information is unavailable, politely ask the caller to contact the clinic.
"""

while True:
    #print("Type Exit to quit the program.")
    user_input = input("You:")
    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
    model= "Qwen/Qwen2.5-1.5B-Instruct:featherless-ai",
    messages=[

        {"role":"system","content":system_prompt},
        {"role":"user","content":"user_input"}
     ]
        ,
    max_tokens=100
)

    print("\nAI:",response.choices[0].message.content)