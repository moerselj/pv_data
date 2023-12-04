import requests
import json
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")

query = 'query=CSV-File&typeName=Artifact&partRequired=false'

api_url = "https://databus.openenergyplatform.org/api/search?"

params = {
    'verify-parts': 'true',
    'log_level': 'info',
}

with open("metadata/header.json", "r") as f_headers:
    headers = json.load(f_headers)

response = requests.get(api_url+query, params=params, headers=headers)
print(f"response code is: {response}")

with open("output/search.json", "w") as outfile:
    outfile.write(str(response.content))
