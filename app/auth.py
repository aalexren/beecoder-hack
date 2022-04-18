# from crypt import methods
from app import app, db
from flask import jsonify, request
from os.path import join

@app.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        email = json['email']
        key = json['key']

        f_path = join(app.config['QR_FOLDER'],'qr_file.txt')
        print(f_path)
        f = open(f_path, 'r')
        qr_num = int(f.read())
        f.close()
        
        # authorization check
        user_ref = db.collection('entrance_status').document(email)
        user = user_ref.get()
        if str(qr_num) == str(key):
            if user.exists:
                user_ref.update({'status': True})
                return jsonify({'status':200, 'key':qr_num})
            return jsonify({'status':300, 'key':qr_num})
        else:
            return jsonify({'status':400, 'key':qr_num})
    return jsonify({'status':500,'key':qr_num})