#!/usr/bin/env python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import pprint
import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"


def main():
    got_response = requests.get(AOIF_BOOKS)

    got_dj = got_response.json()

    pprint.pprint(got_dj)


if __name__ == "__main__":
    main()
