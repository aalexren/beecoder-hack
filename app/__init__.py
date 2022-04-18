from flask import Flask, render_template

app = Flask(__name__)

from random import seed
from random import randint
from datetime import datetime
import time
import threading

seed(datetime.now())
qr_num = {'number': randint(1, 100000000)}
def update_qr_num():
    while True:
        time.sleep(10)
        seed(datetime.now())
        global qr_num
        qr_num['number'] = randint(1, 100000000)

thread = threading.Thread(name='update_qr_num', target=update_qr_num)
thread.setDaemon(True)
thread.start()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('beecoder.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

if __name__ == '__main__':
    app.run(debug=True)

from app import hello, qrcode, auth
