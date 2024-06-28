import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))

all_options = DROPDOWN.options

# for option in all_options:
#     time.sleep(1)
#     if "Option 1" in option.text:
#         print("Страна присутствует")
#     #DROPDOWN.select_by_visible_text(option.text)
for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_index(all_options.index(option))
    