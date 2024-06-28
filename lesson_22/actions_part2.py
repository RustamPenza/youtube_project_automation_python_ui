import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver1 = webdriver.Chrome()
action = ActionChains(driver1)

# LOCATORS
CUBE_A_LOCATOR = ("xpath", "//div[@id= 'column-a']")
CUBE_B_LOCATOR = ("xpath", "//div[@id= 'column-b']")

driver1.get("https://the-internet.herokuapp.com/drag_and_drop")

A = driver1.find_element(*CUBE_A_LOCATOR)
B = driver1.find_element(*CUBE_B_LOCATOR)

action.drag_and_drop(A, B).perform()
time.sleep(3)

# SECOND SITE LOCATORS
GRID_ITEM_LOCATOR = ("xpath", "//div[@class = 'grid__item'][2]")
SIDEBAR_ITEM_LOCATOR = ("xpath", "//div[@class = 'drop-area__item'][3]")

driver2 = webdriver.Chrome()
action = ActionChains(driver2)

driver2.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

grid_item = driver2.find_element(*GRID_ITEM_LOCATOR)
sidebar_item = driver2.find_element(*SIDEBAR_ITEM_LOCATOR)

action.click_and_hold(grid_item) \
    .pause(1.5) \
    .move_to_element(sidebar_item) \
    .release() \
    .perform()

time.sleep(3)
