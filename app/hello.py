from app import app

@app.route('/hello')
async def hello():
    return 'Hello'
