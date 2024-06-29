import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

response = requests.get(url)

# json.loads(response.content)

json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))

# print(response.text)
