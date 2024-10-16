import requests
import json
import sys

try:
    if len(sys.argv) == 2:
        number = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        currency = result["bpi"]
        country = currency["USD"]
        amount = country["rate_float"]
        total = amount * number
        print(f"${total:,.4f}")
    else:
        sys.exit("Missing command=line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")