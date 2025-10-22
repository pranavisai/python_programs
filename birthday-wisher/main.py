import pandas as pd
import datetime as dt
import smtplib
import random

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {
    (row["month"], row["day"]): row
    for (index, row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    name = person["name"]
    email = person["email"]

file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", name)

my_email = "saipranavi.com"
password = "1234"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Happy Birthday!\n\n{contents}"
    )
    connection.close()



