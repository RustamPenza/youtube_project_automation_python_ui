import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# LOCATORS

driver.get("https://demoqa.com/nestedframes")

driver.switch_to.frame("frame1")
print(driver.find_element("xpath", "//body").text)

driver.switch_to.frame(0)  # переходим на фрейм во фрейме по индексу
print(driver.find_element("xpath", "//body").text)

driver.switch_to.parent_frame()  # переключаемся в родительский фрейм
print(driver.find_element("xpath", "//body").text)

driver.switch_to.default_content()  # переключиться на стартовую страницу
