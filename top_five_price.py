import apikey
import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": apikey.key,
}

parameters = {
    "start": "1",
    "limit": "5",
    "convert": "USD",
}

json = requests.get(url, params=parameters, headers=headers).json()

# print(json)
# Get data list
for coin in json["data"]:
    print(coin["symbol"], coin["quote"]["USD"]["price"], "\n")
