#!/usr/bin/env python3
"""
Author: David Hull
Date: 7/7/20
Description: Something really dope.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"
    ## V2 STYLE STRING FORMATTER - return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
