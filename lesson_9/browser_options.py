import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"
# options.add_argument("--headless")  # безголовый (фоновый) режим
# options.add_argument("--incognito")  # режим инкогнито
# options.add_argument("--ignore-certificate-errors")  # что бы не придирался к сертификатам
options.add_argument("--window-size=1920,1080")  # указываем размер окна
# options.add_argument("--disable-cache")  # отключить кеш
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


start_time = time.time()

driver.get("https://whatismyipaddress.com/")
end_time = time.time()
result = end_time - start_time

print(result)
