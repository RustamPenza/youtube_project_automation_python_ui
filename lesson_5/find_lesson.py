import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://freeconferencecall.com/login")
time.sleep(3)

driver.find_element("id", "loginformsubmit").click()
time.sleep(3)
