import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

file_path= "övning1/min_fil.mp3"

with open(file_path, "rb") as file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=file

    )

print(transcript.text)