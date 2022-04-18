from flask import render_template
from app import app, qr_num

@app.route('/qr-code')
def qr_code():
    return render_template('index.html')

# Random number to generate qr code
@app.route('/qr-code/seed')
def qr_code_seed():
    print(qr_num)
    return f'{qr_num["number"]}'