import os


from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class ProjectModel(BaseSettings):
    BACKEND_HOST: str
    BACKEND_PORT: int

    class Config:
        env_file = "./.env"


class ElasticModel(BaseSettings):
    ELASTIC_HOST: str
    ELASTIC_PORT: int

    class Config:
        env_file = "./.env"


project_config = ProjectModel()
elastic_config = ElasticModel()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_URL = "/api/v1"
BASE_URL = (
    f"http://{project_config.BACKEND_HOST}:{project_config.BACKEND_PORT}{API_URL}"
)
ES_HOST = f"http://{elastic_config.ELASTIC_HOST}:{elastic_config.ELASTIC_PORT}"
