from flask import Blueprint
from utils import wechat

Wx = Blueprint('wx',__name__ , url_prefix = '/api/wx/')

@Wx.route('')
def index():
    return 'wx index'

@Wx.route('login')
def login():
    wechat.login()
    return 'login'

@Wx.route('send')
def send():
    wechat.send()
    return 'send'