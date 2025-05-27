import requests
import json

file = 'last_request.json'

url = f"https://webhook.site/token/06b20f75-51d1-48e4-9557-da9ce774d660/requests?limit=1"

response = requests.get(url)

data = response.json()
with open(file, 'w') as txt:
	json.dump(data, txt)
