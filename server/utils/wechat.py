from wxpy import *
import uuid
from common import file

root_dic = file.get_root_dic()
sessonid = '1cf091b0-b439-11e9-bc86-0492264c1b57'#uuid.uuid1()

def qr_callback(uuid,status,qrcode):
    print (uuid,status,qrcode)
def login_callback ():
    print ('login succcess.')

wx_users = dict()
def login():
    bot = Bot(
        cache_path = f'{root_dic}/cache/pkl/{sessonid}.pkl',
        qr_path = f'{root_dic}/cache/qr/{sessonid}.png',
        # qr_callback = qr_callback,
        login_callback = login_callback
    )
    wx_users[sessonid] = bot
    
def send():
    wx_users[sessonid].file_helper.send('Hello from wxpy!')

