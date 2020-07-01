#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""

# using std library method for getting at API data
import urllib.request
import json

# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"


def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = urllib.request.urlopen(SPACEXURI)

    # pull STRING data off of the 200 response (even tho it's JSON!)
    xString = coreData.read().decode()

    # convert STRING data into Python Lists and Dictionaries
    listOfCores = json.loads(xString)

    count = 1
    for core in listOfCores:

        coreSerial = core["core_serial"]
        og_launch = core["original_launch"]
        missions = core["missions"]

        myString = f"{count}. Core Serial Number: {coreSerial}\n    Original Launch: {og_launch}\n    Missions:\n"
        if len(missions) != 0:
            for mission in missions:
                myString += f"        Name: {mission.get('name')}, Flight Number: {mission.get('flight')}\n"

        else:
            myString += "        None"

        print(myString)
        count = count + 1


if __name__ == "__main__":
    main()
