API_KEY = 'AFRbT5nRxPgQqZC6N47mT8omKJcmiAZk3sJ0Okpr'


import requests
from requests.structures import CaseInsensitiveDict

url = f"https://api.currencyapi.com/v3/latest?apikey={API_KEY}"

headers = CaseInsensitiveDict()
headers["apikey"] = API_KEY

resp = requests.get(url, headers=headers)

data = resp.json()

for currency in data["data"].values():
    print(currency["code"])
    print(currency["value"])
    print()

# print(resp.json())