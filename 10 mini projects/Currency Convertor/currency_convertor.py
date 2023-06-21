import requests
from bs4 import BeautifulSoup

def get_data(amount: int, _from: str, _to: str):
    html_text = requests.get(f"in.investing.com/{_from}-{_to}").text
    soup = BeautifulSoup(html_text, "lxml")

    price_tag = soup.find('bdo', _class="last-price-value js-streamable-element").text

    res = price_tag * amount
    return res

if __name__ == "__main__":
    _from = input("Enter currency name from : ")
    _to = input("Enter currency name to : ")
    amount = int(input("Enter amount to be convert : "))

    res = get_data(amount, _from, _to)

    print(res)