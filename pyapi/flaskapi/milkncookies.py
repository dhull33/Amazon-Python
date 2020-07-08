#!/usr/bin/env python3
"""
Author: David Hull
Date: 7/8/20
Description: Something really dope.
"""

from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

# Entry point for users
@app.route("/login")
@app.route("/")
def index():
    return render_template("login.html")


# Set the cookie and send back to user
@app.route("/setcookie", methods=["GET", "POST"])
def setcookie():
    user = "defaultuser"
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")

        resp = make_response(render_template("readcookie.html"))

        resp.set_cookie("userID", user)

        return resp

    if request.method == "GET":
        return redirect(url_for("index"))


# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    # attempt to read the value of userID from user cookie
    name = request.cookies.get("userID")  # preferred method

    # name = request.cookies["userID"] # <-- this works but returns error
    # if value userID is not in cookie

    # return HTML embedded with name (value of userID read from cookie)
    return f"<h1>Welcome {name}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
