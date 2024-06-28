import time

from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions


options = ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Locators
FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "//a[@class='nav-link' and text()= ' For Business ']")
START_FREE_BUTTON_LOCATOR = ("xpath", "//a[text()= 'Start for Free']")

driver.get("https://hyperskill.org/tracks")
time.sleep(3)
#driver.set_window_size(1980, 1080)

driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
time.sleep(3)

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
time.sleep(3)
