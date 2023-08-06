from dataclasses import dataclass, asdict
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass
class BaseConfig:
    def asdict(self):
        return asdict(self)


@dataclass
class DatabaseConfig(BaseConfig):
    """Database connection variables"""
    name: str = getenv("POSTGRES_DATABASE")
    user: str = getenv("POSTGRES_USER")
    passwd: str = getenv("POSTGRES_PASSWORD")
    port: int = int(getenv("POSTGRES_PORT"))
    host: str = getenv("POSTGRES_HOST")


@dataclass
class BotConfig(BaseConfig):
    """Bot configuration"""
    BASE_URL: str = getenv("BASE_URL")
    TOKEN: str = getenv("TOKEN")

    WEB_SERVER_HOST: str = "localhost"
    WEB_SERVER_PORT: int = 8080
    BOT_PATH: str = "/webhook/main"


@dataclass
class Configuration:
    """All in one configuration's class"""

    db = DatabaseConfig()
    bot = BotConfig()


conf = Configuration()
