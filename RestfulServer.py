from flask import Flask, request
from flask_restful import Resource, Api
import random

class RestfulServer(Resource):
    task_list = []
    client_list = []
    def __init__ (self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(RestfulServer, "/")

    def start(self):
        self.task_list = []
        self.client_list = []
        self.ID_CNT = 0
        self.MAX_CLIENTS = 10000
        self.app.run()


    def get(self):
        return {"Info": "RESTFUL_MORDAX"}

    def post(self):
        json = request.get_json()
        task_list_total = []
        client_list_total = []

        if self.get_KEY(json) == "owner" and self.get_COMMAND(json) != "GET_CLNTS" and len(self.task_list) != 0:
            for i in range(len(self.task_list)):
                task_list_total.append(self.task_list[i])
            return {"Task": task_list_total}

        if self.get_KEY(json) == "owner" and self.get_COMMAND(json) == "GET_CLNTS":
            if len(self.client_list) != 0:
                for i in range(len(self.client_list)):
                    client_list_total.append(self.client_list[i])
                return {"Clients":client_list_total}
            else:
                return{"Clients":"None"}

        if len(self.task_list) != 0 and self.get_KEY(json) != None:
            for i in range(len(self.task_list)):
                if self.get_KEY(json) in self.task_list[i]:
                    return{"Task":self.task_list[i]}

        if self.get_ID(json) == None and self.get_COMMAND(json) == "ID_RQST":
            new_ID = self.check_ID(random.randrange(10000))
            return {"NewID":new_ID}

    def put(self):
        json = request.get_json()
        if self.get_KEY(json) == "owner":
            self.ID = self.get_ID(json)
            self.CMD = self.get_COMMAND(json)
            self.task_list.append('{' + '"Task":"{}","ID":"{}"'.format(self.CMD, self.ID) + '}')
            return {"tasks":self.task_list}

    @staticmethod
    def get_KEY(json):
        try:
            return json["KEY"]
        except Exception as e:
            return None

    @staticmethod
    def get_COMMAND(json):
        try:
            return json["CMD"]
        except Exception as e:
            return None

    @staticmethod
    def get_ID(json):
        try:
            return json["ID"]
        except Exception as e:
            return None

    def check_ID(self, ID):
        if len(self.client_list) != 0:
            if ID in self.client_list:
                self.check_ID(random.randrange(self.MAX_CLIENTS))
            else:
                self.client_list.append(ID)
                return ID
        else:
            self.client_list.append(ID)
            return(ID)


r = RestfulServer()
r.start()
