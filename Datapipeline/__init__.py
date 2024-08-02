from flask import Flask
from flask_migrate import Migrate
from config import config


def create_app(config_mode):
    appInstance = Flask(__name__)
    appInstance.config.from_object(config[config_mode])
    
    return appInstance