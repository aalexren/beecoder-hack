from time import time, sleep
import math

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def mock_value():
    dt = time()
    res = abs(math.sin(dt) * 10) + 18
    return res

def main():
    # Simulate sensors

    cred = credentials.Certificate('../beecoder.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    while True:
        sleep(5)
        coll = db.collection('sensors')
        devs = coll.stream()
        for dev in devs:
            ref = coll.document(dev.id)
            ref.update({'value':mock_value()})

if __name__ == '__main__':
    main()