import requests

res = requests.put("http://127.0.0.1:5000/", json={"KEY":"owner", "CMD":"a", "ID":"8411"})
res = requests.put("http://127.0.0.1:5000/", json={"KEY":"owner", "CMD":"b", "ID":"2"})
res = requests.put("http://127.0.0.1:5000/", json={"KEY":"owner", "CMD":"c", "ID":"3"})

res = requests.post("http://127.0.0.1:5000/", json={"CMD":"ID_RQST"})
if res.ok:
    print res.json()
res = requests.post("http://127.0.0.1:5000/", json={"CMD":"ID_RQST"})
if res.ok:
    print res.json()


res = requests.post("http://127.0.0.1:5000/", json={"KEY":"owner","CMD":"GET_CLNTS"})
if res.ok:
   print res.json()
