import re
from urllib import response
import requests
import json

API = "http://sumar.chaco.gov.ar/api"
ENDPOINT_ME = "me"
ENDPOINT_PRESTACIONES= "prestaciones"
ENDPOINT_EFECTORES = "efectores"
# ENDPOINT_CHECKHEALTH = ""

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoiYXBpdXNlciJ9LCJpYXQiOjE2NjgzODgxMTcsImV4cCI6MTY2ODM5NTMxN30.LcvKNwIU9xBaNMoer-vLXf4tv6zgDq_c5rJLjnB4XAQ"

def header_prestaciones():
    return {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoiYXBpdXNlciJ9LCJpYXQiOjE2Njg0NTQwMTksImV4cCI6MTY2ODQ2MTIxOX0.BCmI4SVfQCYbyQfkY6e3jmQlNMjxjHDDkHyKtgGvlbU",
        "Content-Type": "application/json"
    }

def header():
    return {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoiYXBpdXNlciJ9LCJpYXQiOjE2Njg0NTQwMTksImV4cCI6MTY2ODQ2MTIxOX0.BCmI4SVfQCYbyQfkY6e3jmQlNMjxjHDDkHyKtgGvlbU"
    }

payload = json.dumps({
  "dni": "31109945"
})

def get_me():
    url = f"{API}/{ENDPOINT_ME}"
    response = requests.get(url, headers=header())
    return response.content

def get_prestaciones():
    url = f"{API}/{ENDPOINT_PRESTACIONES}"
    response = requests.get(url, headers=header_prestaciones(), data=payload)
    return response.content

def get_efectores():
    url = f"{API}/{ENDPOINT_EFECTORES}"
    response = requests.get(url, headers=header())
    return response.content

def get_checkHealth():
    url = f"{API}"
    response = requests.get(url)
    return response.content


