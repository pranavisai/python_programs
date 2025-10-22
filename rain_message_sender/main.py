import requests
from twilio.rest import Client

api_key = ""
URL = "https://api.openweathermap.org/data/2.5/forecast"
auth_token = ""
account_sid = ""

LAT = 51.050991
LON = 13.733630

parameters = {
   "lat" : LAT,
    "lon" : LON,
    "appid": api_key,
    "cnt": 6,
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+1',
        body = "It's going to rain! Dont forget your umbrella ☔️!",
        to='whatsapp:+9'
    )