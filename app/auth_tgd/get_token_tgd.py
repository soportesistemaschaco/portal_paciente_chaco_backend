import requests
import json

API = "http://stage.ventanillaunica.chaco.gov.ar/oauth/v2/token?"
GRANT_TYPE = "authorization_code"
CLIENT_ID = "109_469fzlhy0084gkscg4gsk8k88ow4kgggso8s44ososo80ccos8"
CLIENT_SECRET = "1pnatc2ds77ocoggsk0gw4ccsw4gswoocows40ogcww4owg0c8"
REDIRECT_URI = "http://201.217.244.105:8000/token-tgd"


def get_token_tgd(code: str):
    url = f"{API}grant_type={GRANT_TYPE}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&redirect_uri={REDIRECT_URI}&code={code}"

    response = requests.get(url)
    return json.loads(response.text)
