import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
SHEET_URL = "GOOGLE_SHEET"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(ZILLOW_URL)

listings = driver.find_elements(By.CSS_SELECTOR, value=".ListItem-c11n-8-84-3-StyledListCardWrapper")
listings_link = []
listings_address = []
listings_price = []


def clean_address(raw_address: str) -> str:
    address = raw_address.strip()

    # Remove extra spaces and normalize commas
    address = re.sub(r'\s+', ' ', address)
    address = re.sub(r'\s*,\s*', ', ', address)

    # Normalize common street types
    abbreviations = {
        r'\bStreet\b': 'St',
        r'\bAvenue\b': 'Ave',
        r'\bRoad\b': 'Rd',
        r'\bBoulevard\b': 'Blvd',
        r'\bDrive\b': 'Dr',
        r'\bLane\b': 'Ln',
        r'\bCourt\b': 'Ct',
        r'\bPlace\b': 'Pl',
        r'\bTerrace\b': 'Ter',
        r'\bHighway\b': 'Hwy',
    }
    for full, abbr in abbreviations.items():
        address = re.sub(full, abbr, address, flags=re.IGNORECASE)

    # Remove anything before "|" (like "The Landing | 1395 22nd St...")
    address = address.split("|")[-1].strip()

    # Split parts by comma and remove partial duplicates
    parts = [p.strip() for p in address.split(",") if p.strip()]
    final_parts = []
    for part in parts:
        if not any(part.lower() in p.lower() or p.lower() in part.lower() for p in final_parts):
            final_parts.append(part)

    cleaned = ", ".join(final_parts)
    return cleaned


for listing in listings:
    link_element = listing.find_element(By.CSS_SELECTOR, value="a[data-test='property-card-link']")
    link = link_element.get_attribute("href")

    raw_address = listing.find_element(By.CSS_SELECTOR, "address[data-test='property-card-addr']").text.strip()
    address = clean_address(raw_address)

    raw_price = listing.find_element(By.CSS_SELECTOR, value="span[data-test='property-card-price']").text.strip()
    new_price = re.search(r"\$\d[\d,]*", raw_price)
    price = new_price.group().replace("+", "")

    listings_link.append(link)
    listings_address.append(address)
    listings_price.append(price)

driver1 = webdriver.Chrome(options=chrome_options)

i = 0
while i < len(listings_link):
    driver1.get(SHEET_URL)
    time.sleep(2)

    driver1.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(listings_address[i])
    driver1.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(listings_price[i])
    driver1.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(listings_link[i])

    driver1.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    time.sleep(2)
    i = i+1





