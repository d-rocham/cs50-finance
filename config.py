import os
from tempfile import mkdtemp

# TO UNDERSTAND:
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Configuration base settings
    """

    SECRET_KEY = os.environ.get("SECRET_KEY") or "9d7daea4a862dd6513fee22b8223ad73"
    API_KEY = os.environ.get("API_KEY") or "pk_50b635ec6ed94958956473499a25881b"
    TEMPLATES_AUTO_RELOAD = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL") or "sqlite:///finance.db"
    )

    SESSION_FILE_DIR = mkdtemp()
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    # ATTENTION: Do jinja filters go in here?
    # ATTENTION: Do cache settings go in here?
    # ATTENTION: How to set API key from here?

    @staticmethod  # TODO:
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
