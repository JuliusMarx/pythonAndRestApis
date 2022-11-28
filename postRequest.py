import requests

api_url = ""

json = {"userId": 1, "title": "Buy milk", "completed": False}

response = requests.post(api_url, json)
response.json()
response.status_code