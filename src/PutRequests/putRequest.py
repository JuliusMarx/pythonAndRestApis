import requests

api_url = ""

response = requests.get(api_url)
response.json()

todo = {"userId": 1, "title": "Wash car", "completed": True}

response = requests.put(api_url, json=todo)
response.json()
response.status_code