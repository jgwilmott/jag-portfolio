from flask import Flask, render_template

name = "Jagier Wilmott"

list_of_banks = [
    "RBC",
    "BNS",
    "BMO"
]

app = Flask(__name__)

@app.route("/")
def about_page():
    return render_template("about.html", name = name, list_of_banks = list_of_banks)


@app.route("/projects")
def projects_page():
    return render_template("projects.html", name = name)


@app.route("/contact")
def contact_page():
    return render_template("contact.html", name = name)


