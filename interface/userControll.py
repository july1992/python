# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
import flask_restful


app = Flask(__name__)
api = flask_restful.Api(app)

class login(flask_restful.Resource):
    def get(self):
        return {'code': 0,'message':'succsess','data':[]}

class registe(flask_restful.Resource):
    def post(self,phone):
        if phone == 'vily':
            return {'code': 0,'message':'succsess','data':[]}
        else: return {'code': 1000,'message':'fail','data':[]}

api.add_resource(login, '/login','/')
api.add_resource(registe, '/registe')

if __name__ == '__main__':
    app.run(host='localhost',port=6600)