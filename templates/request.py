import requests

url = 'http://localhost:5000/predict_api'
r = requests.get(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())