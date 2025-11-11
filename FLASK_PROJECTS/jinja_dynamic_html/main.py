from flask import Flask, render_template
import requests

app = Flask(__name__)

GENDER_URL = "https://api.genderize.io/"
AGE_URL = "https://api.agify.io/"

params = {
    "name": "peter"
}

response1 = requests.get(GENDER_URL, params=params)
response2 = requests.get(AGE_URL, params=params)
data1 = response1.json()
data2 = response2.json()

@app.route('/')
def home_route():
    return render_template("index.html")

@app.route("/<name>")
def age_and_gender(name):
    return render_template("name.html", age=data2["age"], gender=data1["gender"], name=name)

if __name__ == "__main__":
    app.run(debug=True)
