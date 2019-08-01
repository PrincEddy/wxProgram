from flask import Flask
from api.wx import wx

def create_app():
    app = Flask(__name__)
    app.register_blueprint(wx)
    return app