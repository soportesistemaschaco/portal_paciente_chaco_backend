import os

# CREDENTIALS
API_KEY = os.getenv("API_KEY")
API_CODE = os.getenv("API_CODE")

# API SERVICE
API_SERVICE = "http://hcd-api.ddns.net/api/v1/ExternalService/"
TURNO_ENDPOINT = f"{API_SERVICE}Turnos"
HC_ENDPOINT = f"{API_SERVICE}Allergies"

# API PERSON
API_PERSON = "http://hcd-api.ddns.net/api/v1/Person/"
GENDER_ENDPOINT = f"{API_PERSON}genders"
DOCUMENT_ENDPOINT = f"{API_PERSON}documents-type"
