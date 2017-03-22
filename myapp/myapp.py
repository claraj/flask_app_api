from myapp import app

@app.route('/')
def index():
    return 'This is the home page'
