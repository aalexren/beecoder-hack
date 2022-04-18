from flask import render_template
from app import app, qr_num

@app.route('/qr-code')
def qr_code():
    return render_template('index.html')

# Random number to generate qr code
@app.route('/qr-code/seed')
def qr_code_seed():
    f = open(app.config['QR_FOLDER'] + 'qr_file.txt', 'r')
    qr_num = f.read()
    f.close()
    return f'{qr_num}'
    # return f'{qr_num["number"]}'