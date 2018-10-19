from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get_mbti(self, username):
        e_i = 'E' if random.randint(0, 1) == 0 else 'I'
        s_n = 'S' if random.randint(0, 1) == 0 else 'N'
        t_f = 'T' if random.randint(0, 1) == 0 else 'F'
        j_p = 'J' if random.randint(0, 1) == 0 else 'P'

        mbti = {
            'Extraversion/Intraversion': e_i,
            'Sensing/Intuition': s_n,
            'Thinking/Feeling': t_f,
            'Judjing/Perception': j_p
        }

        if random.randint(0, 1) == 1:
            return None
        return mbti

    def get(self, name):
            # download 10 images from instagram
            mbti = self.get_mbti(name)
            if mbti != None:
                mbti['status'] = 'OK'
            else:
                mbti = {'status': 'ERROR'}
            return mbti

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)