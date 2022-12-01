import requests
import json
from typing import Dict

from app.gear.sumar_chaco.config import ME_ENDPOINT, PRESTACIONES_ENDPOINT, EFECTORES_ENDPOINT
from app.gear.sumar_chaco.login import SumarChacoLogin


class SumarImplChaco:
    def __init__(self):
        self.token = SumarChacoLogin().login()

    @property
    def header(self):
        return{
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_me(self) -> Dict:
        url = f"{ME_ENDPOINT}"
        response = requests.get(url, headers=self.header)
        return json.loads(response.text)

    def get_prestaciones(self, dni: str) -> Dict:
        url = f"{PRESTACIONES_ENDPOINT}"
        payload = json.dumps({
            "dni": f"{dni}"
        })
        response = requests.get(url, headers=self.header, data=payload)
        return json.loads(response.text)

    def get_efectores(self) -> Dict:
        url = f"{EFECTORES_ENDPOINT}"
        response = requests.get(url, headers=self.header)
        return json.loads(response.text)


class Vacunacion:
    def get_vaccines(self, dni: str):
        prestaciones = SumarImplChaco()
        vacunas = prestaciones.get_prestaciones(dni)
        idObjetos = vacunas['idObj']
        vacunas_list = []
        for x in idObjetos:
            if x == "IMV015A98" or x == "IMV016A98" or x == "IMV017A98" or x == "IMV018A98" or x == "IMV019A98" or x == "IMV013A98" or x == "IMV001A98" or x == "IMV006A98" or x == "IMV002A98" or x == "IMV003A98" or x == "IMV009A98" or x == "IMV005A98" or x == "IMV012A98" or x == "IMV007A98" or x == "IMV004A98" or x == "IMV008A98" or x == "IMV010A98" or x == "IMV011A98" or x == "IMV014A98":
                vacunas_list.append(x)
        if vacunas_list:
            return vacunas_list
        else:
            return None
