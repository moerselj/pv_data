'''  
Publish metadata Json-LD (DataID) on the Databus.

Python-Script to perform an HTTP POST request to an API endpoint on OEP databus.
The payload for the request is read from a file (metadata/publish.jsonld), 
and additional parameters (verify-parts and log_level) are passed as query parameters.

'''
 
import requests as req         # 'requests' module is used for making HTTP requests.
import json
import logging

# Configures 'logging' system.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")

# Specifies the API endpoint URL and sets some parameters for the HTTP request.
api_url = "https://databus.openenergyplatform.org/api/publish"

params = {
    'verify-parts': 'true',    # fetch-file-properties
    'log_level': 'info',       # Desired detail of the publish report. Can be set to either 'error', 'info' or 'debug'.
}

# Reads a JSON file (metadata/header.json) containing specific headers for the HTTP request 
# such as the personal API-Key created in the OEP Databus Account.
with open("metadata/header.json", "r") as f_headers:
    headers = json.load(f_headers)

# Reads the data from a file (metadata/publish.jsonld) 
# and makes an HTTP POST request to the specified API endpoint.
with open("metadata/publish.jsonld", "rb") as f_pub:
    response = req.post(api_url, data=f_pub, params=params, headers=headers)

# Converts the response to a JSON file and prints the response.
json_response = response.json()
print(f"response code is: {response}")

# Writes the response to a JSON file (output/publish.json).
with open("output/publish.json", "w") as outfile:
    outfile.write(str(json_response))
