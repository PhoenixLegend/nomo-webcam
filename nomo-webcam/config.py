import os
import pymysql


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
   
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123123@127.0.0.1:3306/test'

# @staticmethod
    #def init_app(app):
       # pass 


class DevelopmentConfig(Config):
    DEBUG = False
    #数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123123@127.0.0.1:3306/test'


class TestingConfig(Config):
    TESTING = True
   # SQLALCHEMY_DATABASE_URI = 
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
   # SQLALCHEMY_DATABASE_URI =
   pass






confige = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}