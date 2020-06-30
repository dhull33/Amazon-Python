#!/usr/bin/env python3


def main():
    iss_location = {
                    "message": "success",
                    "timestamp": 1593530434,
                    "iss_position": {
                        "longitude": "178.0128",
                        "latitude": "41.9694"
                        }
                    }
    longitude = iss_location["iss_position"]["longitude"]
    latitude = iss_location["iss_position"]["latitude"]

    print("The ISS is at a longitude of %s and latitude of %s" % (longitude, latitude))


if __name__ == "__main__":
    main()
