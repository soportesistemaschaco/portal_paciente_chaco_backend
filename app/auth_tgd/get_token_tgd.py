import requests
import json
from typing import Dict

from app.auth_tgd.config import TGD_API, GRANT_TYPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, PERSONA_ENDPOINT


class AuthTgd:
    @staticmethod
    def get_token_tgd(code: str) -> Dict:
        url = f"{TGD_API}grant_type={GRANT_TYPE}" \
              f"&client_id={CLIENT_ID}" \
              f"&client_secret={CLIENT_SECRET}" \
              f"&redirect_uri={REDIRECT_URI}" \
              f"&code={code}"
        response_code = requests.get(url)
        token = json.loads(response_code.text)
        response = requests.get(PERSONA_ENDPOINT, headers={"Authorization": f"Bearer {token['access_token']}"})
        print(response.text)
        return json.loads(response.text)
