from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    """funguje dobre, dotaz:
    http://localhost:5000/
    """
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        """todle funguje dokonce i v postmanovi
        """
        print 'todosimple, get = ', todo_id
        if todo_id in todos:
            return {todo_id: todos[todo_id]}
        else:
            return {'message': 'klic {0} tu neni'.format(todo_id)}

    def put(self, todo_id):
        """nevim proc v postmanu nefunguje.
         ale funguje:
            curl http://localhost:5000/todo1 -d "argument=asd" -X PUT
        """
        print 'todo simple, put, argument = ', todo_id
        todos[todo_id] = request.form['argument']
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, '/<string:todo_id>')


@app.route('/pokus/', methods=['GET'])
def pokus():
    """kdyz to nevracim pomoci jsonify tak to spadne na:
    TypeError: 'dict' object is not callable
    """
    # return {'a': 'b'}
    return jsonify({'pokus': 'pokus'})


@app.route('/pokus2/')
def poksu2():
    """funguje, ani nemusim uvadet ze to taham getem
    """
    return jsonify({'pokus2': 'pokus2'})


@app.route('/data/<data>')
def prijma_data(data):
    """klasika, pokud to neni jsonify tak to pada na
     stejne chybe
    """
    return jsonify({'prijma': 'data = {0}'.format(data)})




if __name__ == '__main__':
    app.run(debug=True)
