from flask import Flask, request
from flask_restful import Resource, Api
import random


class RestfulServer(Resource):
    task_list = []
    client_list = []
    ID_CNT = 0
    MAX_CLIENTS = 1000
    ID = None
    CMD = None

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(RestfulServer, "/")

    def start(self):
        self.app.run()

    @staticmethod
    def get():
        return {"Info": "RESTFUL_MORDAX"}

    def post(self):
        json = request.get_json()
        task_list_total = []
        client_list_total = []

        if self.get_key(json) == "owner" and self.get_command(json) != "GET_CLNTS" and len(self.task_list) != 0:
            for i in range(len(self.task_list)):
                task_list_total.append(self.task_list[i])
            return {"Task": task_list_total}

        if self.get_key(json) == "owner" and self.get_command(json) == "GET_CLNTS":
            if len(self.client_list) != 0:
                for i in range(len(self.client_list)):
                    client_list_total.append(self.client_list[i])
                return {"Clients": client_list_total}
            else:
                return{"Clients": "None"}

        if len(self.task_list) != 0 and self.get_key(json) is not None:
            for i in range(len(self.task_list)):
                if self.get_key(json) in self.task_list[i]:
                    return{"Task": self.task_list[i]}

        if self.get_id(json) is None and self.get_command(json) == "ID_RQST":
            new_id = self.check_id(random.randrange(10000))
            return {"NewID": new_id}

    def put(self):
        json = request.get_json()
        if self.get_key(json) == "owner":
            self.ID = self.get_id(json)
            self.CMD = self.get_command(json)
            self.task_list.append('{' + '"Task":"{}","ID":"{}"'.format(self.CMD, self.ID) + '}')
            return {"tasks": self.task_list}

    @staticmethod
    def get_key(json):
        try:
            return json["KEY"]
        except KeyError:
            return None

    @staticmethod
    def get_command(json):
        try:
            return json["CMD"]
        except KeyError:
            return None

    @staticmethod
    def get_id(json):
        try:
            return json["ID"]
        except KeyError:
            return None

    def check_id(self, new_id):
        if len(self.client_list) != 0:
            if new_id in self.client_list:
                self.check_id(random.randrange(self.MAX_CLIENTS))
            else:
                self.client_list.append(new_id)
                return new_id
        else:
            self.client_list.append(new_id)
            return new_id


r = RestfulServer()
r.start()
