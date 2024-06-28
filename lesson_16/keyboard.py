import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

MULTI_DROPDOWN = ("xpath", "//input[@id='react-select-4-input']")

driver.get("https://demoqa.com/select-menu")

driver.find_element(*MULTI_DROPDOWN).send_keys("Green")
time.sleep(1)
driver.find_element(*MULTI_DROPDOWN).send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(*MULTI_DROPDOWN).send_keys("Blue")
time.sleep(1)
driver.find_element(*MULTI_DROPDOWN).send_keys(Keys.ENTER)
time.sleep(1)