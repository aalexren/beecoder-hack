class Sensor:
    def __init__(self, name, status=True, value=0):
        self.name = name
        self.status = status
        self.value = value

    def get_status(self):
        return self.status

    def get_value(self):
        return self.value

    def __repr__(self):
        return f'{self.name} has the {self.status} status and {self.value} value'

from app import app, db
from flask import request, jsonify

@app.route('/sensor/all')
def sensor_all():
    devs = db.collection('devices').stream()
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