import click


@click.command()
@click.argument("name", nargs=-1, type=click.STRING)
def get_data(name):
    """
    GeoInsightFetcher is a tool that gets a name of a city (or multiple)
    and returns some interesting insights about it.
    """

    if len(name) == 0:
        name = input("Please enter a city name: ")

    # formatting city names
    cities = " ".join(name)
    cities = cities.split(",")
    # city name must contain at least 3 characters
    cities = list(filter(lambda x: len(x) >= 3, cities))
    cities = list(map(lambda city: city.strip().lower(), cities))

    # fetching city data
    if len(cities) > 0:
        for i in cities:
            click.echo(f"fetching data for '{i}'")

    else:
        raise ValueError("No valid city name was provided")


if __name__ == "__main__":
    get_data()
