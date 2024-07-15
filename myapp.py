import requests

URL = "http://127.0.0.1:8000/api2/student_allDetails/"

r = requests.get(url=URL)

data = r.json()

print(data)