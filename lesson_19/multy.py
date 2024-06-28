import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

LOGIN_FIELD = ("xpath", "//input[@type= 'email']")
PASSWORD_FIELD = ("xpath", "//input[@type= 'password']")
SUBMIT_BUTTON = ("xpath", "//button[@type= 'submit']")

driver.get("https://hyperskill.org/login")
time.sleep(5)
driver.find_element(*LOGIN_FIELD).send_keys("alekseik@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("Qwerty1321")
driver.find_element(*SUBMIT_BUTTON).click()
time.sleep(3)