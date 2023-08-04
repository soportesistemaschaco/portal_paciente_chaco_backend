import os

# CREDENTIALS
API_KEY = os.getenv("API_KEY")
API_CODE = os.getenv("API_CODE")

# API SERVICE
API_SERVICE = "https://hc.salud.chaco.gob.ar:9440/api/v1/ExternalService/"
TURNO_ENDPOINT = f"{API_SERVICE}Turnos"
HC_ENDPOINT = f"{API_SERVICE}Allergies"

# API PERSON
API_PERSON = "https://hc.salud.chaco.gob.ar:9440/api/v1/Person/"
GENDER_ENDPOINT = f"{API_PERSON}genders"
DOCUMENT_ENDPOINT = f"{API_PERSON}documents-type"
