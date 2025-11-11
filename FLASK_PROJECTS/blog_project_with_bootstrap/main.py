from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/674f5423f73deab1e9a7"

response = requests.get(BLOG_URL)
posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts= posts)

@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    requested_post = None
    for post in posts:
        if post["id"] == blog_id:
            requested_post = post
    return render_template("post.html", post=requested_post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)