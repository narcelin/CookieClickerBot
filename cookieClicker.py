from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

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

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

bigCookie_element = driver.find_element(By.ID, "bigCookie")
# bigCookie.click()

time.sleep(3)

upgrade_prefix = "upgrade"

while True:
    i = 100
    while i > 0:
        bigCookie_element.click()
        i -= 1

    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))

    # for i in range(12):
    #     try:
    #         upgrade_element = driver.find_element(By.ID, "upgrade" + str(i))
    #     except NoSuchElementException:
    #         print("Element not found")
    #         break

    #     upgrade_element.click()

    for i in range(12):
        product_price = driver.find_element(By.ID, "productPrice" + str(i)).text
        
        if product_price:
            product_price = int(product_price.replace(",", ""))

            # upgrade_price = driver.find_element(By.ID, )

            if cookies_count >= product_price:
                product = driver.find_element(By.ID, "product" + str(i))
                product.click()
                
                break

   

driver.quit()