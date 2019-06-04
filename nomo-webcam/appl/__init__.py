#应用包构造文件
import os
import sys
from flask import Flask
from flask_bootstrap import Bootstrap
#from flask_moment import Moment
sys.path.append("..")
from flask_sqlalchemy import SQLAlchemy
from config import confige



bootstrap = Bootstrap()
#moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
#def create_app():
    app = Flask(__name__)
    app.config.from_object(confige[config_name]) 
    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app