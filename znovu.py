# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource

app = Flask(__name__)


@app.route('/')
def index():
    """funguje
    """
    return 'proc to nefunguje? - aaa, funguje :)'


@app.route('/volej/<id>/ahoj/')
def volani_s_argumentem(id):
    """nefunguje nejvic, vraci to, ze nema zadnou
    response od serveru
    """
    return 'volam api s argumentem = ', id


@app.route('/volej2/<nechapuid>/')
def volani_posranyho_id(nechapuid):
    """zajimavy je, ze do konzole se hezky napise
     text spolu s argumentem co predavam. ale PostMan
     na me sere
    """
    print 'volani_posranyho_id = ', nechapuid
    # return 'volam api s id = ', nechapuid

    # kdyz takhle vracim slovnik, pise mi to 'dict'
    # object is not callable
    return {'argument': nechapuid}


# tady nefunguje vubec nic

@app.route('/ahoj2/nevim/')
class NejakyApi2(Resource):
    def get(self):
        return {'key2': 'value'}


@app.route('/ahoj')
class NejakyApi(Resource):
    def get(self):
        return {'key': 'value'}


if __name__ == '__main__':
    app.run(debug=True)
