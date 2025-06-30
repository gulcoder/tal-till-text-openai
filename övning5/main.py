import os
from dotenv import load_dotenv
from openai import OpenAI
import json

def main():
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

    print("=== Transkribering med OpenAI Whisper ===")
    file_path = input("Ange sökväg till ljudfil (t.ex. övning5/min_fil2.mp3): ").strip()

    # Kontrollera att filen finns
    if not os.path.isfile(file_path):
        print(f"Filen '{file_path}' hittades inte. Kontrollera sökvägen och försök igen.")
        return

    print("Välj utdataformat:")
    print("1: text")
    print("2: json")
    print("3: verbose_json")
    format_choice = input("Ange nummer (1-3): ").strip()

    formats = {"1": "text", "2": "json", "3": "verbose_json"}

    if format_choice not in formats:
        print("Felaktigt val av format.")
        return

    response_format = formats[format_choice]

    try:
        with open(file_path, "rb") as file:
            result = client.audio.transcriptions.create(
                model="whisper-1",
                file=file,
                response_format=response_format,
                language="sv"  # Valfritt, kan tas bort eller ändras
            )

        print("\n=== Transkriptionsresultat ===")
        if response_format == "text":
            print(result)
        else:
            result_dict = result.to_dict()
            print(json.dumps(result_dict, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"Ett fel uppstod: {e}")

if __name__ == "__main__":
    main()
