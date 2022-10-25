import requests

ENDPOINT = "http://stage.ventanillaunica.chaco.gov.ar/api/v1/persona"


def auth_tgd(token: str):

    response = requests.get(ENDPOINT, headers={"Authorization": f"Bearer {token}"})
    return response.content
