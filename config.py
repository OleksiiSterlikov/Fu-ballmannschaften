import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Base configuration."""

    APP_NAME = os.getenv("APP_NAME", "Flask application")
    SECRET_KEY = os.getenv("SECRET_KEY", "secret key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_ENABLED = False
    WTF_CSRF_ENABLED = False

    @staticmethod
    def configure_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL", "sqlite:///" + os.path.join(base_dir, "development.sqlite3"),)


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(base_dir, "production.sqlite3"),)
    WTF_CSRF_ENABLED = True


config = dict(development=DevelopmentConfig, production=ProductionConfig)
