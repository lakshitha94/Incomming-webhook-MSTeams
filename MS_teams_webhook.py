import requests
import json
from cognite.client import CogniteClient
from cognite.client.exceptions import CogniteAPIError
import sys
import logging
import lib.config as config

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# messenger method
def ms_tems_alerter(webhookurl,message):

    url = webhookurl
    payload = {
        "text": message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response




# Contact Project Admin to get these details
TENANT_ID = config.TENANT_ID
CLIENT_ID = config.CLIENT_ID_
CDF_CLUSTER = config.CLUSTER  # bluefield, westeurope-1 etc
COGNITE_PROJECT = "cognite-support-qa"

SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

CLIENT_SECRET = config.SECRET  # store secret in env variable


TOKEN_URL = "https://login.microsoftonline.com/%s/oauth2/v2.0/token" % TENANT_ID

try:
    client = CogniteClient(
        token_url=TOKEN_URL,
        token_client_id=CLIENT_ID,
        token_client_secret=CLIENT_SECRET,
        token_scopes=SCOPES,
        project=COGNITE_PROJECT,
        base_url=f"https://{CDF_CLUSTER}.cognitedata.com",
        client_name="client_secret_test_script",
        debug=True,
    )
except Exception as e:
    ms_tems_alerter(config.url,f"{e}")
else:
    ms_tems_alerter(config.url,f"Login Sucessfully to {COGNITE_PROJECT} project.....!")    