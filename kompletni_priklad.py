from flask import Flask, request, jsonify
from flask_restful import Resource, Api, marshal_with

app = Flask(__name__)
api = Api(app)


@api.resource("/helloworld")
class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}

    def put(self, data):
        return "data = ", data

if __name__ == '__main__':
    app.run(debug=True)

