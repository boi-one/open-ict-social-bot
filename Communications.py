from requests.exceptions import ConnectionError, Timeout, RequestException
import requests
import json
from Matching import *

url = 'http://localhost:3000/create-match'

def SendData(match):
    data = match.Serialize()
    try:
        res = requests.post(url, json=data, timeout=10)
        print(res.status_code, res.json())
    except (ConnectionError, Timeout, RequestException) as e:
        print("webserver is not running: ", e)