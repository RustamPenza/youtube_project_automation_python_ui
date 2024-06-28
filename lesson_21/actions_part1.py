import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver)


#LOCATORS
LEFT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name= 'leftClick']")
DOUBLE_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name= 'doubleClick']")
RIGHT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name= 'rightClick']")
HOVER_BUTTON_LOCATOR = ("xpath", "//button[@name= 'colorChangeOnHover']")

driver.get("https://testkru.com/Elements/Buttons")
left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
hover_button = driver.find_element(*HOVER_BUTTON_LOCATOR)

time.sleep(3)
action.click(left_button).pause(2) \
    .double_click(double_button) \
    .context_click(right_button) \
    .move_to_element(hover_button) \
    .perform()
time.sleep(3)
