"""
Created October 10, 2022

This is a test using the Valorant API

"""

import requests
import valorant

response = requests.get("API")

response.raise_for_status()

data = response.json()

id = data["gameName"]
tag = data["tagLine"]

valorantTag = (id, tag)

print(valorantTag)


