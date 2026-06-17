from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    print("\n========== FULL PAYLOAD ==========")
    print(data)
    print("==================================\n")

    message = data.get("message", {})

    transcript = message.get("transcript")

    if transcript:
        print("Transcript:", transcript)

    return {"success": True}


@app.get("/")
def home():
    return {"message": "Server Running"}