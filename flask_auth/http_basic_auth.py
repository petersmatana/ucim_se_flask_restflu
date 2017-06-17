# -*- coding: utf-8 -*-

# http://flask.pocoo.org/snippets/8/

from functools import wraps
from flask import request, Response, Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def check_auth(username, password):
    return username == 'admin' and password == 'secret'


def authenticate():
    return Response('to vis ze jo', 401, {
        'WWW-Authenticate': 'Basic ''realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/secret-page')
@requires_auth
def secret_page():
    return 'ok'


class SecretApi(Resource):

    @requires_auth
    def get(self):
        return {'api': 'ok'}

api.add_resource(SecretApi, '/api')

if __name__ == '__main__':
    app.run(debug=True)
