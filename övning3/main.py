import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

file_path = "övning3/svensk_tal2.mp3"  # eller valfri ljudfil

with open(file_path, "rb") as file:
    srt_result = client.audio.transcriptions.create(
        model="whisper-1",
        file=file,
        response_format="srt",   # 👈 viktig parameter
        language="sv"            # valfritt men bra för icke-engelska
    )

# Skriv resultatet till en .srt-fil
with open("undertexter.srt", "w", encoding="utf-8") as srt_file:
    srt_file.write(srt_result)
