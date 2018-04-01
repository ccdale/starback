from chalice import Chalice

app = Chalice(app_name='sbaws')


@app.route('/', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def index():
    return {'starback': 'lambda'}
