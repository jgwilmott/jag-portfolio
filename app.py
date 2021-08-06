from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def route_hello_world():
    return render_template("hello.html")


@app.route("/<name>")
def route_hello_name(name):
    return f"<p>Hello, {name}!</p>"
