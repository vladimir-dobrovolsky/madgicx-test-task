import json
import os
import urllib
from time import sleep

import click
import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def fetch_from_API(name):
    """
    This function fetches city data from Back4App REST API
    https://www.back4app.com/database/back4app/list-of-all-continents-countries-cities/get-started/python/rest-api/requests?objectClassSlug=world-cities-dataset-api
    :param name: city name
    :return: dict with city data
    """

    # return {"Country": "Ukraine", "Currency": "UAH"}

    # API keys taken from from Back4App REST API example app
    headers = {
        "X-Parse-Application-Id": os.environ.get("BACK4APP_REST_API_APP_ID"),
        "X-Parse-Master-Key": os.environ.get("BACK4APP_REST_API_KEY"),
    }

    where = urllib.parse.quote_plus(
        """
    {
        "name": "%s"
    }
    """
        % name
    )
    url = f"https://parseapi.back4app.com/classes/City?limit=1&order=-population&include=country&keys=name,country,country.name,country.currency,population,cityId&where={where}"

    data = json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
    # print(json.dumps(data, indent=2))
    if "results" in data:
        if len(data["results"]) > 0:
            result = {
                # "City": data["results"][0]["name"],
                "Country": data["results"][0]["country"]["name"],
                "Currency": data["results"][0]["country"]["currency"],
            }

            # if multiple currencies, return only first
            if "," in result["Currency"]:
                result["Currency"] = result["Currency"].split(",")[0]

            return result
    elif "error" in data:
        print(headers)
        raise ConnectionRefusedError("Request authorization error")
    else:
        print(json.dumps(data, indent=2))


@click.command()
@click.option("-f", "file", type=click.Path(exists=True))
@click.argument("name", nargs=-1, type=click.STRING)
def get_data(name=None, file=None):
    """
    GeoInsightFetcher is a tool that gets a name of a city (or multiple)
    and returns some interesting insights about it.
    """

    if file:
        with open(click.format_filename(file)) as txt:
            cities = list()
            for city in txt.readlines():
                cities.append(city)

    else:
        if len(name) == 0:
            name = [input("Please enter a city name: ")]

        # formatting city names
        cities = " ".join(name)
        cities = cities.split(",")

    # city name must contain at least 3 characters
    cities = list(filter(lambda x: len(x) >= 3, cities))
    cities = list(map(lambda city: city.strip().lower().title(), cities))

    separator = "=>" + "-" * 13

    # fetching city data
    if len(cities) > 0:
        for i in cities:
            result = fetch_from_API(i)
            click.echo(f"=> ​ {i}")
            click.echo(separator)
            if result:
                for k, v in result.items():
                    click.echo(f"=>{k}: {v}")
            else:
                click.echo(f"=> Invalid City Name")

            click.echo(separator)
            if len(cities) > 1:
                click.echo("=>")
                # limiting request rate (1/sec)
                sleep(1)

    else:
        raise ValueError("No valid city name was provided")


if __name__ == "__main__":
    get_data()
