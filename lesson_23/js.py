import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

driver = webdriver.Chrome()
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

EX_2_LOCATOR = ("xpath", "//h3[text()= 'Example 2: ']")

driver.get("https://seiyria.com/bootstrap-slider/")
ex_2 = driver.find_element(*EX_2_LOCATOR)

scrolls.scroll_to_element(ex_2)
time.sleep(2)
