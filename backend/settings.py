from os import environ
from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE = environ.get('TITLE', 'Notenapp')
    DESCRIPTION = environ.get('DESCRIPTION', '')
    VERSION = float(environ.get('VERSION', '0.1'))
    DEBUG = bool(int(environ.get('DEBUG', '0')))

    API_ROUTE = f'/api/v{int(VERSION)}'


settings = Settings()
