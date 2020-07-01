#!/usr/bin/env python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api"


def main():
    got_response = requests.get(AOIF)

    got_dj = got_response.json()

    print(got_dj)


if __name__ == "__main__":
    main()
