import os
from logging import config as logging_config

from pydantic import BaseSettings
from dotenv import load_dotenv

from .logger import LOGGING

load_dotenv()

logging_config.dictConfig(LOGGING)


class ProjectModel(BaseSettings):
    PROJECT_NAME: str = "movies"
    BACKEND_PORT: int

    class Config:
        env_file = "./.env"


class RedisModel(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = "./.env"


class ElasticModel(BaseSettings):
    ELASTIC_HOST: str
    ELASTIC_PORT: int

    class Config:
        env_file = "./.env"


project_config = ProjectModel()
redis_config = RedisModel()
elastic_config = ElasticModel()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
