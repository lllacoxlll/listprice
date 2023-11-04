import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import scrapy

service = Service('/Users/acox/Downloads/chromedriver-mac-arm64/chromedriver')

driver = webdriver.Chrome(service=service)

driver.get("http://www.google.com")

print("Selenium version:", selenium.__version__)
print("Scrapy version:", scrapy.__version__)

print(driver.title)

time.sleep(5)

driver.quit()