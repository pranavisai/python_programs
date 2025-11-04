from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

sleep(3)

english_language = driver.find_element(By.ID, value="langSelect-EN")
english_language.click()
sleep(3)

sleep(2)

cookie_found = driver.find_element(By.ID, value="bigCookie")

# Get all store items (products 0-17)
item_ids = [f"product{i}" for i in range(18)]

wait_time = 5
time_out = time() + wait_time
five_min = time() + 60 * 5

while True:
    cookie_found.click()

    if time() > time_out:
        try:
            cookie_text = driver.find_element(By.ID, value="cookies").text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            products = driver.find_elements(By.XPATH, value='div[id^="product"]')

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        time_out = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break



