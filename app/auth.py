from crypt import methods
from app import app, qr_num, db
from flask import jsonify, request

@app.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        email = json['email']
        key = json['key']
        print(email, key)
        
        # authorization check
        user_ref = db.collection('entrance_status').document(email)
        user = user_ref.get()
        if qr_num['number'] == key and user.exists:
            user_ref.update({'status': True})
            return jsonify({'status':200})
        else:
            return jsonify({'status':400, 'key':qr_num['number']})
    return jsonify({'status':400,'key':qr_num['number']})