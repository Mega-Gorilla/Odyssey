import os
import socket
from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')
# ローカルサーバーの設定
bot = mineflayer.createBot({
    'username': 'simple-bot',
    'host': '192.168.100.24',
    'port': 30000,
    'version': '1.21.4',
    'hideErrors': False
})

# ログインイベント
@On(bot,'login')
def login(this):
    print('ログインしました')
