import re
from urllib import response
import requests
import json

API = "http://sumar.chaco.gov.ar/api"
ENDPOINT_LOGIN = "login"

payload = json.dumps({
  "username": "apiuser",
  "password": "19XYAay45Guo8G5cTuCv6nsZQfhI2YJJZJ4Xk4jqcqodc3cK8u"
})

headers = {
  'Content-Type': 'application/json'
}

def post_login():
    url = f"{API}/{ENDPOINT_LOGIN}"
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.status_code

print(post_login())