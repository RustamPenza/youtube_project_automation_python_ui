import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = "64.227.4.244:8888"  # если есть авторизация для прокси то указываем "username:password@64.227.4.244:8888"

options = Options()
options.add_argument(f"--proxy-server={PROXY_SERVER}")

driver = webdriver.Chrome(options=options)

driver.get("https://2ip.ru")  # 94.181.132.20

time.sleep(5)
