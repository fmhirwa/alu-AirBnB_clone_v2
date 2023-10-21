#!/usr/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return render_template("index.html")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return render_template("hbnb.html")

@app.route("/c/<text>", strict_slashes=False)
def c(text="is cool"):
    return render_template("c.html", text=text.replace("_", " "))

@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return render_template("python.html", text=text.replace("_", " "))

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    try:
        n = int(n)
        return "n is a number"
    except ValueError:
        return "n is not a number"

@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    try:
        n = int(n)
        return render_template("number_template.html", n=n)
    except ValueError:
        return "n is not a number"

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    try:
        n = int(n)
        if n % 2 == 0:
            return render_template("number_odd_or_even.html", n=n, parity="even")
        else:
            return render_template("number_odd_or_even.html", n=n, parity="odd")
    except ValueError:
        return "n is not a number"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
