#!/usr/bin/python3

from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
