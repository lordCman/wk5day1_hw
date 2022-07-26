from flask import Flask 
from config import Config

hw = Flask(__name__)

hw.config.from_object(Config)

from . import routes