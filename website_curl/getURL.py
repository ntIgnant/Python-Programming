import requests

url = "https://modules.lancaster.ac.uk/user/index.php?id=44691/*.json"

response = requests.get(url)

if response.headers.get("Content-Type") == "application/json; charset=utf-8":
    print("This is a JSON response")
    data = response.json()
    print(data)
else:
    print("Not JSON")
