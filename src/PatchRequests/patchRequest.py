import requests

api_url = ""

todo = {"title": "Mow lawn"}

response = requests.patch(api_url, json=todo)
response.json()
response.status_code