import requests

response = requests.request(method="GET", url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
response.raise_for_status()
question_data = response.json()["results"]
