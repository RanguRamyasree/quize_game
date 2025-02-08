import requests

parameters = {"amount": 10,
"type": "boolean"
}

responce = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
data = responce.json()

question_data = data['results']
print(question_data)
