import os

from openai import OpenAI
from config import settings

client = OpenAI(api_key=settings.API_KEY)


def text_to_speech(text: str) -> None:
    output_dir = f"../story_audio"
    output_file = os.path.join(output_dir, f"output_{os.urandom(4).hex()}.mp3")

    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=text,
        )
    except Exception as e:
        print("Something went wrong with tts...", e)
        return

    response.stream_to_file(output_file)
