from flask import Blueprint

wx = Blueprint('wx',__name__ , url_prefix = '/api/wx')

@wx.route('')
def index():
    return 'wx index'