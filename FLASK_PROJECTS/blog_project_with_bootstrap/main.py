from flask import Flask, render_template, request
import requests
import smtplib
import csv
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_ADDRESS = os.getenv("TO_ADDRESS", EMAIL_ADDRESS)

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

@app.route('/contact', methods=['GET','POST'])
def receive_data():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        if not name or not email or not message:
            return render_template("contact.html", flash_msg="Please fill name, email and message.", flash_cat="danger",
                                   form={'name': name, 'email': email, 'phone': phone, 'message': message})

        subject = f"Contact form submission from {name}"
        body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}\n"
        email_text = f"Subject: {subject}\n\n{body}"

        try:
            with smtplib.SMTP(SMTP_ADDRESS, port=SMTP_PORT, timeout=15) as smtp:
                smtp.ehlo()
                if SMTP_PORT == 587:
                    smtp.starttls()
                    smtp.ehlo()
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.sendmail(EMAIL_ADDRESS, TO_ADDRESS, email_text.encode('utf-8'))

            csv_path = os.path.join(os.getcwd(), 'contact_submissions.csv')
            with open(csv_path, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([name, email, phone, message])

            return render_template("contact.html", flash_msg="Thank you — your message was sent!", flash_cat="success")

        except Exception as e:
            # Log the exception (print for now) and show friendly error
            print("Error sending contact email:", e)
            return render_template("contact.html", flash_msg="Error sending message — please try later.",
                                   flash_cat="danger",
                                   form={'name': name, 'email': email, 'phone': phone, 'message': message})

            # GET: show empty form
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)