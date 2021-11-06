import requests

url = "https://www14.software.ibm.com/webapp/set2/flrt/liteTable?prodKey=aix&format=json"
timeout = 5

response = requests.get(url, timeout=timeout)
payload = response.json()

print(payload["input"])