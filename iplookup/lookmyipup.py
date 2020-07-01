#!/usr/bin/env python3

import argparse
import turtle

import requests


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--ip", help="The IP address to lookup via the API service")
    args = parser.parse_args()

    if args.ip:
        iptolookup = args.ip
    else:
        iptolookup = input("What is the ip address to look up?")

    zresp = requests.get(f"http://ip-api.com/json/{iptolookup}")
