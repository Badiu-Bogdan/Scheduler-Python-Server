import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "helloworld")
# response = requests.get(BASE + "helloworld")
response = requests.put(BASE + "helloworld/bill/19", {"likes": 10})
# response = requests.put(BASE + "video")

print(response.json())
