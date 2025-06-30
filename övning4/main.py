import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

file_path = "övning4/svensk_tal3.mp3"  # Ändra till din ljudfil

formats = ["text", "json", "verbose_json"]

for fmt in formats:
    with open(file_path, "rb") as file:
        result = client.audio.transcriptions.create(
            model="whisper-1",
            file=file,
            response_format=fmt,
            language="sv"
        )

    print(f"\n========== Format: {fmt} ==========")
    if fmt == "text":
        # Resultatet är redan text
        print(result)
    else:
        # Konvertera Transcription-objekt till dict för att kunna serialisera till JSON
        result_dict = result.to_dict()
        print(json.dumps(result_dict, indent=2, ensure_ascii=False))

