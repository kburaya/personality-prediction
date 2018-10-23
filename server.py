from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import subprocess
import requests
import os,binascii
import uuid
import shutil

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get_mbti(self, username):
        e_i = 'E' if random.randint(0, 1) == 0 else 'I'
        s_n = 'S' if random.randint(0, 1) == 0 else 'N'
        t_f = 'T' if random.randint(0, 1) == 0 else 'F'
        j_p = 'J' if random.randint(0, 1) == 0 else 'P'
        mbti = e_i + s_n + t_f + j_p

        if random.randint(0, 1) == 1:
            return None
        return mbti

    def get(self, name):
            # download 10 images from instagram
            # proc = subprocess.Popen("php instagram-crawler/crawl.php {}".format(name), shell=True, stdout=subprocess.PIPE)
            # script_response = proc.stdout.read()
            # urls = script_response.decode("utf-8").split('\n')
            # if (urls == 'error'):
            #     return {'status': 'ERROR'}
            # print (urls)
            # if os.path.exists('data/{}'.format(name)):
            #     shutil.rmtree('data/{}'.format(name), ignore_errors=True)
            # os.mkdir('data/{}'.format(name))
            # for url in urls:
            #     if len(url) > 10:
            #         r = requests.get(url, allow_redirects=True)
            #         open('data/{}/{}.jpg'.format(name, str(uuid.uuid4())), 'wb').write(r.content)
            # get images features
            # proc = subprocess.Popen("java -jar java -jar instragram-processing.jar /home/ubuntu/other/rest-server data", shell=True,
            #                         stdout=subprocess.PIPE)
            # script_response = proc.stdout.read()
            # get mbti type
            mbti_type = self.get_mbti(name)
            if mbti_type != None:
                mbti = {
                    'status': 'OK',
                    'mbti': { 'psy_type': mbti_type }
                }
            else:
                mbti = {'status': 'ERROR'}
            print (mbti)
            return mbti

# api.add_resource(User, "/user/<string:name>")

# app.run(debug=True)
user = User()
user.get('happyksuh')