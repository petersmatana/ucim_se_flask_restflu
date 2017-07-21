from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with

app = Flask(__name__)
api = Api(app)

input_format = {
    'key': fields.String(),
}

todos = {}


class TodoSimple(Resource):

    @marshal_with(input_format)
    def get(self, todo_id):
        # curl http://localhost:5000/prvni -X GET
        if todo_id in todos:
            return {todo_id: todos[todo_id]}
        else:
            return {'je tu': 'hovno'}

    def put(self, todo_id):
        # curl http://localhost:5000/prvni -d "data=Remember the milk" -X PUT
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def post(self, todo_id):
        '''
curl http://localhost:5000/nevim -d "{"todo_id": "asdasdasd"}" -X POST -H "Content-Type: application/json"
        '''
        # todos[todo_id] = request.form['data']
        return {todo_id: todo_id}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
