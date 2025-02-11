from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Define configurações e variveis de ambiente que serão usadas no projeto"""

    MODEL_ID: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
