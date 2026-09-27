import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    HOST: str
    PORT: str
    LOGIN: str
    PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.test"), extra="ignore"
    )

    @property
    def base_url(self) -> str:
        return f"http://{self.HOST}:{self.PORT}"
