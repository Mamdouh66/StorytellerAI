import os

from openai import OpenAI
from config import settings

client = OpenAI(api_key=settings.API_KEY)


def text_to_speech(text: str) -> None:
    output_dir = f"./story_audio"
    output_file = os.path.join(output_dir, f"output_{os.urandom(4).hex()}.mp3")

    try:
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="onyx",
            input=text,
        )
    except Exception as e:
        print("Something went wrong with tts...", e)
        return

    response.stream_to_file(output_file)


def generate_image(text: str) -> str:
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"""Generate an image for the following chapter of a story: {text[:400]}""",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url
