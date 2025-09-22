import requests
import json
from Matching import *

url = 'http://localhost:3000/get-match'

def SendData(match):
    data = match.Serialize()
    res = requests.post(url, json=data, timeout=10)
    print(res.status_code, res.json())