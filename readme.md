# GeoInsightFetcher CLI tool

This app fetches city data from Back4App REST API with keys obtained from example app code on [this page](https://www.back4app.com/database/back4app/list-of-all-continents-countries-cities/get-started/python/rest-api/requests?objectClassSlug=world-cities-dataset-api)

## Setup
####1. create a new virtual environment
####2. install dependencies from requirements.txt
`pip install -r requirements.txt`
####3. provide API credentials

API credentials are fetched from environment variables and  may be provided in .env file in the project root

```
BACK4APP_REST_API_APP_ID={your_app_id}
BACK4APP_REST_API_KEY={your_app_key}
```

