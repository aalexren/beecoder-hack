from enum import Enum

class SensorType(Enum):
    TEMPERATURE = 'temperature'
    HUMIDITY = 'humidity'

class Sensor:
    def __init__(self, name: str, place: str, type_: SensorType, status=True, value=0):
        self.name = name # id
        self.status = status
        self.value = value
        self.place = place
        self.type_: SensorType = type_

    def get_status(self) -> str:
        return self.status

    def get_value(self) -> int:
        return self.value

    def __repr__(self):
        return ' '.join([self.name, str(self.status), str(self.value), self.place, str(self.type_)])

from app import app, db
from flask import request, jsonify
import math
import time
# from datetime import datetime

@app.route('/sensor/all', methods=['GET'])
def sensor_all():
    # def mock_value():
    #     dt = time.time()
    #     res = abs(math.sin(dt) * 5 / math.e + math.cos(dt * 10))
    #     return res

    devs = db.collection('sensors').stream()
    to_ret = []
    for dev in devs:
        di = dev.to_dict()
        di['uid'] = dev.id
        ref = db.collection('sensors').document(dev.id)
        # ref.update({'value':mock_value()})
        to_ret.append(di)
    return jsonify(to_ret)

@app.route('/device/all', methods=['GET'])
def devices_all():
    devs = db.collection('devices').stream()
    to_ret = []
    for dev in devs:
        di = dev.to_dict()
        di['uid'] = dev.id
        ref = db.collection('devices').document(dev.id)
        # ref.update({'value':mock_value()})
        to_ret.append(di)
    return jsonify(to_ret)
    return jsonify([(dev.id, dev.to_dict()) for dev in devs])

@app.route('/sensor/<string:id>', methods=['GET'])
def sensor(id):
    try:
        device_ref = db.collection('devices').document(id)
        device = device_ref.get().to_dict()
        print(device)
    except:
        pass

    return jsonify(device)