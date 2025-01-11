from pydantic import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Debug
    DEBUG_MODE: bool = True
    STATIC_DIR: str = "static"
    STATIC_URL: str = "/sub"
    STATIC_NAME: str = "static"
    TENOKARES_DIR: str = "templates"

    class Config:
        evn_file = ".env"


config = Settings()
