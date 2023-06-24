
# Third party app for real time currency rates

# Alpha Vantage
# https://www.alphavantage.co


# List of currency code of all the countries 
# https://www.iban.com/currency-codes


import requests

with open('10 mini projects\\Currency Convertor\\api.txt', 'r') as f:
    api_key = f.read()

def convert_curr(from_c, to_c, amount):
    base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = f"{base_url}&from_currency={from_c}&to_currency={to_c}&apikey={api_key}"
    response = requests.get(main_url)
    result = response.json()
    key = result['Realtime Currency Exchange Rate']
    rate = key['5. Exchange Rate']

    return float(rate) * amount


if __name__ == "__main__":
    print("\t\tCURRENCY CONVERTOR\n\n")
    while True:
        from_c = input("Enter currency code of currency to be converted : ").upper()
        to_c = input("Enter currency code of currency to convert : ").upper()
        amount = int(input("Enter amount : "))

        result = convert_curr(from_c, to_c, amount)
        print(f"{amount} {from_c} : {result} {to_c}")

        is_continue = input("Wanted to continue? (y/n) : ").lower()
        if is_continue == 'n': exit(0)