import requests

api_url = ""

response = requests.get(api_url)
response.json()
response.status_code
response.headers["Content-Type"]