from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

# Wait for the presence of an element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#python libraries
import time

# service = Service(executable_path="chromedriver")
driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Got it!"))
)

advertise_cookie_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Got it!")
advertise_cookie_btn.click()

language_selector_btn = driver.find_element(By.ID, "langSelect-EN")
language_selector_btn.click()

bigCookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

bigCookie_element = driver.find_element(By.ID, "bigCookie")
# bigCookie.click()

time.sleep(3)

while True:
    bigCookie_element.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    
    for i in range(2):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text
        product_price = int(product_price.replace(",", ""))

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

driver.quit()