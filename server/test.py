from enum import Enum
import json
import requests

class POSTTYPE(Enum):
    NEW = 1
    UPD = 2

BASE = "http://127.0.0.1:5000/"

data = {"0": {"type":1, "name" : "Derek"},
        "1": {"type":1, "name" : "Tejas"},
        "2": {"type":1, "name" : "Pradyun"},
        "3": {"type":1, "name" : "Jon"}}

for key, value in data.items():
    print(requests.post(BASE + "database/" + key, value).json())
# requests.post(BASE + "database/2", {"type" : 2, "location" : "lolza", "time" : "20:00", "list" : "3,1"})

print(requests.get(BASE + "database/3").json())