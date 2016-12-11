# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    """
    curl http://localhost:5000/
    """
    def get(self):
        return {'data': 'world'}

todos = {}

class TodoSimple(Resource):
    """
    jak mam "zavolat", spis namapovat get?
    """
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        s = request.form['data']
        return {'hovno': s}


class Moje(Resource):
    """
    prvni moznost
    curl http://localhost:5000/coze13 -d "data=asd fe  dssd" -X PUT

    zkousim tam naprat nejaky argumenty?
    curl http://localhost:5000/coze13 -d "data=asd fe  dssd&nechapu=asdsad" -X PUT
    """
    def put(self, coze_id, nechapu_id):
        return {
            'moje': request.form['data'],
            'wtf': request.form['data2']
        }

# definovani endpointu

api.add_resource(HelloWorld, '/', '/hello')
api.add_resource(TodoSimple, '/<string:todo_id>')

# tohle nejde
# api.add_resource(TodoSimple, '/geet')
api.add_resource(Moje, '/<string:coze_id>&<string:nechapu_id>')


if __name__ == '__main__':
    app.run(debug=True)
