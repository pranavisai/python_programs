import smtplib
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
ADDR = os.getenv("SMTP_ADDRESS")

AMAZON_URL = "https://www.amazon.de/Instant-Pot-Plus-1-Multikocher-Schnellkochtopf/dp/B0DMWK3RDV/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=31U1LUOPWPIV&dib=eyJ2IjoiMSJ9.J2chGoDwqurz7IE-xaFOXAHwLEp4vJMbtqU15kAP3mESs_p0L12EvFvKAmTU7TRQA1OM1dKDw23jibAzj5oEn5X0xKq4qdOEPLscozCGdKYj30LIZSIrvZG2C97iIsb4IZ2ixZzeULvVHZb8E25rAE8__UBr7lWWGg5zeS9Tio-aT44oh-aNOGJ09gvlS1wTXMfx_B9FeWplk3kn1xbZosD7ROLV_6S_tTBMF0L82h0.57K-zj0ZqF-0neQzs9nAUM_oSMjpyzXts8Pc0X8kROs&dib_tag=se&keywords=instant%2Bpot&qid=1761925657&sprefix=instant%2Bpot%2Caps%2C139&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
BUY_PRICE = 200

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
}

response = requests.get(AMAZON_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

whole = soup.select_one(".a-price-whole").text.strip()[:3]
title = soup.find(id="productTitle").text.strip()

price = int(whole)

if price < BUY_PRICE:
    message = f"{title} is on sale for the price of {price}€!"

    with smtplib.SMTP_SSL(ADDR, port=465) as connection:
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: Amazon Price Alert for your item!\n\n{message}\n{AMAZON_URL}".encode("utf-8")
        )

