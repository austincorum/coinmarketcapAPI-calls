import apikey
import json
import datetime
from datetime import date, timedelta
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# Set the limit of results to return
parameters = {"start": "1", "limit": "5", "convert": "USD"}

# insert API key below
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": apikey.key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters, headers=headers)
    data = json.loads(response.text)
    today = date.today()
    yesterday = str(today - timedelta(days=1))
    yesterday_datetime = datetime.datetime.strptime(yesterday, "%Y-%m-%d")

    for coin in data["data"]:
        symbol = coin["symbol"]
        date_added_str = coin["date_added"][:10]

        # Convert to datetime and format accordingly
        date_added = datetime.datetime.strptime(date_added_str, "%Y-%m-%d")

        # print the symbols that have been added in the last day
        if yesterday_datetime < date_added:
            print(symbol + ": " + date_added_str)
        else:
            pass

    # print(json.dumps(data,sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
