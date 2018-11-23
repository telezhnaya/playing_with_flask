import os
import pathlib

BASEDIR = pathlib.Path(__file__).parent


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'hard to guess string')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
