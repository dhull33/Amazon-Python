#!/usr/bin/env python3
import os
import requests
import pprint

from dotenv import load_dotenv

load_dotenv()

NASA_KEY = os.getenv("NASA_API_KEY")


def main():
    nasa_url = "https://api.nasa.gov/planetary/apod"
    api_params = {"api_key": NASA_KEY}

    nasa_response = requests.get(nasa_url, params=api_params)

    apod = nasa_response.json()

    pprint.pprint(apod)


if __name__ == "__main__":
    main()
