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

driver.get("https://google.com")

# ?Error
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "glFyf"))
# )

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("tech with tim", Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

# elements or element, PARTIAL is optional
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

# time.sleep(10)

driver.quit()