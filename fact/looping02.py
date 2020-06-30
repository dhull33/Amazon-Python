#!/usr/bin/env python3

def main():

    dnsfile = open("dnsservers.txt", "r")

    dnslist = dnsfile.readlines()

    for server in dnslist:
        print(server, end = "")

    dnsfile.close()

if __name__ == "__main__":
    main()