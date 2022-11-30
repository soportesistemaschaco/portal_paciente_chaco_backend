import requests
import json

from app.gear.sumar_chaco.config import SUMAR_USERNAME, SUMAR_PASSWORD, LOGIN_ENDPOINT


class SumarChacoLogin:
    @property
    def header(self):
        return {
            'Content-Type': 'application/json'
        }

    def login(self):
        url = f"{LOGIN_ENDPOINT}"
        payload = json.dumps({
            "username": f"{SUMAR_USERNAME}",
            "password": f"{SUMAR_PASSWORD}"
        })
        response = requests.post(url, data=payload, headers=self.header)
        result = json.loads(response.text)
        return result['token']
