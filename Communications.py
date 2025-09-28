from requests.exceptions import ConnectionError, Timeout, RequestException
import requests
import json
from Matching import *
from Messages import SendMatchLink

url = 'http://localhost:3000/create-match'

async def SendData(match):
    data = match.Serialize()
    try:
        res = requests.post(url, json=data, timeout=10)
        # print(res.status_code, f"json is dit: {res.json().get("customURL")}")
        await SendMatchLink(res.json().get("customURL"), match)
    except (ConnectionError, Timeout, RequestException) as e:
        print("webserver is not running: ", e)