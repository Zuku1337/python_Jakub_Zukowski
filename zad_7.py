import urllib.request
import json


class Brewery:

    def __init__(self, id, obdb_id, name, brewery_type, street, address_2, address_3,
                 city, state, county_province, postal_code, country, longitude, latitude,
                 phone,website_url, updated_at, created_at):
        self.id = id
        self.obdb_id = obdb_id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self):
        return f"Browar {self.name} znajduje się w stanie {self.state}"


def get_info() -> None:
    with urllib.request.urlopen("https://api.openbrewerydb.org/breweries?page=15") as response:
        raw_data = response.read()
        data = raw_data.json()
        list_of_breweres = []
        for i in data:
            list_of_breweres.append(i['id'], i['name'], i['brewery_type'])

get_info()

