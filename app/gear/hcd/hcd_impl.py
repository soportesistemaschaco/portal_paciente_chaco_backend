import requests
import json
from typing import Dict

from app.gear.hcd.config import API_KEY, API_CODE, TURNO_ENDPOINT, HC_ENDPOINT, GENDER_ENDPOINT, DOCUMENT_ENDPOINT


class HSIImplChaco:
    def __init__(self):
        self.key = API_KEY
        self.code = API_CODE

    @property
    def header(self):
        return {
            "API_KEY": f"{self.key}",
            "API_CODE": f"{self.code}"
        }

    def get_turnos(self, dni: str, dni_tipo: int, genero_id: int) -> Dict:
        url = f"{TURNO_ENDPOINT}?documentoNro={dni}&tipoDocumentoId={dni_tipo}&generoId={genero_id}"
        response = requests.get(url, headers=self.header)
        return json.loads(response.text)

    def get_hc(self, dni: str, dni_tipo: int, genero_id: int) -> Dict:
        url = f"{HC_ENDPOINT}?documentoNro={dni}&tipoDocumentoId={dni_tipo}&generoId={genero_id}"
        response = requests.get(url, headers=self.header)
        return json.loads(response.text)

    def get_genders(self) -> Dict:
        url = f"{GENDER_ENDPOINT}"
        response = requests.get(url, headers=self.header)
        return json.loads(response.text)

    def get_documents_type(self) -> Dict:
        url = f"{DOCUMENT_ENDPOINT}"
        response = requests.get(url, headers=self.header)
        return json.loads(response.text)
