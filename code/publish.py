import requests
import json
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")

api_url = "https://databus.openenergyplatform.org/api/publish"

params = {
    'verify-parts': 'true',
    'log_level': 'info',
}

with open("metadata/header.json", "r") as f_headers:
    headers = json.load(f_headers)

with open("metadata/publish.jsonld", "rb") as f_pub:
    response = requests.post(api_url, data=f_pub, params=params, headers=headers)
json_response = response.json()
print(f"response code is: {response}")

with open("output/publish.json", "w") as outfile:
    outfile.write(str(json_response))
