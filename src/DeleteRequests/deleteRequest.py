import requests

api_url = ""

response = requests.delete(api_url)
response.json()
response.status_code