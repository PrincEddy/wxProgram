from flask import Flask
from api.wx.wx import Wx

def create_app():
    app = Flask(__name__)
    app.register_blueprint(Wx)
    return app