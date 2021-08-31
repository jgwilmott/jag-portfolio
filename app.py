from flask import Flask, render_template
import requests
import decouple


full_name = "Jagier Wilmott"

projects_url = "https://api.github.com/users/jgwilmott/repos"
github_projects = requests.get(projects_url).json()

contact = decouple.config("CONTACT_FORM_API", default = None)

projects = []

for project in github_projects:
    name = project["name"]
    desc = project["description"]
    url = project["html_url"]

    projects.append({
        "name": name,
        "desc": desc,
        "url": url,
    })



list_of_banks = [
    "RBC",
    "BNS",
    "BMO"
]

app = Flask(__name__)

@app.route("/")
def about_page():
    return render_template("about.html", name = full_name, list_of_banks = list_of_banks)


@app.route("/projects")
def projects_page():
    return render_template("projects.html", name = full_name, projects = projects)


@app.route("/contact")
def contact_page():
    return render_template("contact.html", name = full_name, api = contact)


