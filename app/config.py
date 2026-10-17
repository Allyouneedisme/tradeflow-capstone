from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://tradeflow:tradeflow_pass@localhost:5432/tradeflow_db"
    APP_NAME: str = "TradeFlow"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
