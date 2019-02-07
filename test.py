import requests

res = requests.post("http://127.0.0.1:5000/", json={"KEY":"owner", "CMD":"a", "ID":"1"})
res = requests.post("http://127.0.0.1:5000/", json={"KEY":"owner", "CMD":"b", "ID":"2"})
res = requests.post("http://127.0.0.1:5000/", json={"KEY":"owner", "CMD":"c", "ID":"3"})
if res.ok:
    print res.json()