import os
import time
import pickle

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)


driver.get("https://www.drive2.ru/reception/")

driver.delete_all_cookies()

cookies = pickle.load(open(os.getcwd()+"\\cookies\\drive2.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(5)
