from enum import Enum
import json
import requests

class POSTTYPE(Enum):
    NEW = 1
    UPD = 2

BASE = 'http://127.0.0.1:5000/'

data = {'0': {'type':1, 'name' : 'Derek', 'lat' : 40.47, 'lng' : -74.67},
        '1': {'type':1, 'name' : 'Tejas', 'lat' : 40.48, 'lng' : -74.62},
        '2': {'type':1, 'name' : 'Pradyun', 'lat': 40.48, 'lng' : -74.59},
        '3': {'type':1, 'name' : 'Jon', 'lat' : 40.48, 'lng' : -74.60}}

for key, value in data.items():
    print(requests.post(BASE + 'database/' + key, value).json())

requests.post(BASE + 'database/2', {'type' : 2, 'day' : 21, 'month' : 2, 'year' : 2021, 'lat' : 40.47, 'lng' : -74.67, 'list' : '3,1'})

print(requests.get(BASE + 'database/2').json())