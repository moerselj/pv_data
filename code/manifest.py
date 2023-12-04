import requests
import json
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")

api_url = "https://databus.openenergyplatform.org/"

params = {
    'verify-parts': 'true',
    'log_level': 'info',
}

with open("metadata/header.json", "r") as f_headers:
    headers = json.load(f_headers)

response = requests.get(api_url, params=params, headers=headers)
ttl_response = response.text
print(f"response code is: {response}")

with open("output/manifest.ttl", "w") as outfile:
    outfile.write(str(ttl_response))
