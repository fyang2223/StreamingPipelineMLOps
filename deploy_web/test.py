import predict
import requests

data = [{'Age':29, 'Pclass':1, 'Fare':20},
        {'Age':29, 'Pclass':3, 'Fare':4}]
data = {"Age":29, "Pclass":1, "Fare":20}

url = 'http://localhost:9696/predict'

response = requests.post(url, json=data)

print(response.json())





