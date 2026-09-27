import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    HOST: str
    API_PORT: str
    KAFKA_PORT: str
    LOGIN: str
    PASSWORD: str
    CLIENT_ID: str
    TOPIC_NAME: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.test"), extra="ignore"
    )

    @property
    def base_url(self) -> str:
        return f"http://{self.HOST}:{self.API_PORT}"

    @property
    def kafka_url(self) -> str:
        return f"{self.HOST}:{self.KAFKA_PORT}"
