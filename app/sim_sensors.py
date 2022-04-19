from time import time, sleep
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def mock_temperature(prev):
    return prev + random.randrange(-30, 30) / 100


def mock_humidity(prev):
    return prev + random.randrange(-25, 25) / 100


mock = {
    'temperature_sensor': mock_temperature,
    'humidity_sensor': mock_humidity      
}


def main():
    # Simulate sensors
    cred = credentials.Certificate('../beecoder.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    while True:
        sleep(1)
        coll = db.collection('sensors')
        devs = coll.stream()
        for dev in devs:
            ref = coll.document(dev.id)
            dev = dev.to_dict()
            ref.update({'value': mock[dev['type']](dev['value'])})
            
            

if __name__ == '__main__':
    main()