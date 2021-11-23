from Brewery import Brewery
import urllib.request
import json
import argparse


def get_info(arg: str) -> None:
    print(arg)
    if arg is not None:
        url = f"https://api.openbrewerydb.org/breweries?by_city={arg}"
        get_breweries(url)
    else:
        url = "https://api.openbrewerydb.org/breweries?page=20"
        get_breweries(url)


def get_breweries(url: str) -> None:
    with urllib.request.urlopen(url) as response:
        raw_data = response.read()
        data = json.loads(raw_data)
        list_of_breweries = [Brewery(**i) for i in data]
        for brewery in list_of_breweries:
            print(brewery)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--city")
    args = parser.parse_args()
    get_info(vars(args)['city'])

