import requests

class RestfulOwner:
    def __init__(self):
        self.host = "http://127.0.0.1:5000/"
        self.ID = "owner"

        if self.check_server():
            self.run()

    def check_server(self):
        request = requests.get(self.host)
        if request.ok and request.json()["Info"] =="RESTFUL_MORDAX":
            return True
    def get_clients(self):
        request = requests.post(self.host, json={"KEY":self.ID, "CMD":"GET_CLNTS"})
        if request.ok:
            return request.json()

    def run(self):
        if self.get_clients()["Clients"] != None:
            for i in range(len(self.get_clients()["Clients"])):
                print("Client: {}".format(self.get_clients()["Clients"][i]))
r = RestfulOwner()