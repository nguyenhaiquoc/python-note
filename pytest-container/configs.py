from pydantic_settings import BaseSettings, SettingsConfigDict


# define the settings class read value from .env file
class Config(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_ACCOUNT: str
    DB_PASSWORD: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


if __name__ == "__main__":
    config = Config()
