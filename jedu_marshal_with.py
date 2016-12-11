# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api, fields, marshal_with, Resource, reqparse


# abych mohl parsovat vstup? wtf? proc tak slozite?
parser = reqparse.RequestParser()
parser.add_argument('task')

app = Flask(__name__)
api = Api(app)

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

data_structure = {
    'todo1': fields.String,
    'todo2': fields.String,
    'todo3': fields.String
}

data = {
    'todo1': 'nejaky data',
    'todo2': 'jiny data',
    'todo3': 'zas neco jinyho'
}


def is_there_some_data(data_id):
    if data_id not in data:
        # nevim, ten druhej return mi dava vetsi
        # smysl, vracim slovnik s necim a http status code

        # return abort(404, 'neni tu')
        return {'error': 'blbost'}, 404


# nemam poneti, co timhle chtel basnik rict :D
# class TodoDao(object):
#     def __init__(self, todo_id, task):
#         self.todo_id = todo_id
#         self.task = task
#
#         # This field will not be sent in the response
#         self.status = 'active'
#
#     def get_as_dist(self):
#         return {'todo': self.todo_id}
#
#
# class Todo(Resource):
#     @marshal_with(resource_fields)
#     def get(self):
#         return TodoDao(todo_id='my_todo', task='Remember the milk').get_as_dist()


class MojeApi(Resource):
    @marshal_with(data_structure)
    def get(self, todo_id):
        if is_there_some_data(todo_id):
            return data


class SaveData(Resource):
    def put(self, data_id):
        # print parser.parse_args()
        print 'asd'


api.add_resource(MojeApi, '/mojeapi/<todo_id>')
api.add_resource(SaveData, '/saves/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
