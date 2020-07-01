#!/usr/bin/env python3


def main():
    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:
        dnslist = dnsfile.readlines()

        for server in dnslist:

            print(server, end="")
            # No need to close file because with close it automatically


if __name__ == "__main__":
    main()
