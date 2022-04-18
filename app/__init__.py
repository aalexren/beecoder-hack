from flask import Flask, render_template
from os.path import join, dirname, realpath

app = Flask(__name__)

app.config['QR_FOLDER'] = join(dirname(realpath(__file__)), 'static/qr_file/')

from random import seed
from random import randint
from datetime import datetime
import time
import threading

seed(datetime.now())
qr_num = {'number': 0}

# @sched.scheduled_job('interval', seconds=10)
# def update_qr_num():
#     seed(datetime.now())
#     qr_num['number'] = randint(1, 100000000)

# def update_qr_num():
#     while True:
#         time.sleep(10)
#         seed(datetime.now())
#         # global qr_num
#         qr_num['number'] = randint(1, 100000000)

# thread = threading.Thread(name='update_qr_num', target=update_qr_num)
# thread.setDaemon(True)
# thread.start()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('beecoder.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

if __name__ == '__main__':
    app.run(debug=True)
    # sched.start()

from app import hello, qrcode, auth
