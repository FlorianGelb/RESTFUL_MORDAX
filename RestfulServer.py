from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
CMD = None


class Redirect(Resource):
    def get(self):
        return {"INFO":CMD}


class RestfulServer(Resource):
    def start(self):
        app.run()

    def get(self):
        return {"INFO": CMD} *3

    def post(self):
        json = request.get_json()
        if self.get_KEY(json) == "owner":
            self.ID = self.get_ID(json)
            global CMD
            CMD = self.get_COMMAND(json)
            api.add_resource(type(self.ID,(), {"get":'return {"CMD":"{}"}'.format(CMD)}, "/{}/".format(self.ID)))
            return {"cmd":self.get_COMMAND(json)}

    @staticmethod
    def get_KEY(json):
        return json["KEY"]

    @staticmethod
    def get_COMMAND(json):
        return json["CMD"]

    @staticmethod
    def get_ID(json):
        return json["ID"]

api.add_resource(RestfulServer, "/")

r = RestfulServer()
r.start()
