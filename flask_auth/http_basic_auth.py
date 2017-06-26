# -*- coding: utf-8 -*-

# http://flask.pocoo.org/snippets/8/

from functools import wraps
from flask import request, Response, Flask
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, \
     check_password_hash


app = Flask(__name__)
api = Api(app)


class User(object):

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        # self.pw_hash = ""

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


def check_auth(username, password):
    for user in all_users:
        if user.username == username:
            return user.check_password(password)


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
        return {'api': 'ok2'}

api.add_resource(SecretApi, '/api')

all_users = []

if __name__ == '__main__':
    u1 = User('smonty', 'ahoj')
    u2 = User('verca', 'cau')

    all_users.append(u1)
    all_users.append(u2)

    app.run(debug=True)
