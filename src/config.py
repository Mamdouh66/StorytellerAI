import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = os.getenv("OPENAI_API_KEY")
    # MODEL_NAME: str = "gpt-4-1106-preview"
    MODEL_NAME: str = "gpt-3.5-turbo"

    class Config:
        env_file = ".env"


settings = Settings()
