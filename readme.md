# GeoInsightFetcher CLI tool

## TODO:
* ~~virtualenv~~
* ~~accept and validate input~~
* accept file input
* ~~fetch city data from API~~ ~~(+rate limiting)~~
* ~~fetch Country and Currency fields~~
* ~~error messages~~
* readme (~~api keys~~)

## Setup
This app fetches city data from Back4App REST API with keys provided for example app
https://www.back4app.com/database/back4app/list-of-all-continents-countries-cities/get-started/python/rest-api/requests?objectClassSlug=world-cities-dataset-api

API credentials are fetched from environment variables and  may be provided in .env file in the project root

BACK4APP_REST_API_APP_ID= _app id_
BACK4APP_REST_API_KEY= _app key_