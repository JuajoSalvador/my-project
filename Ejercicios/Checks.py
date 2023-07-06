import requests
from selenium import webdriver
import json

url_get = "https://mtp.alejmans.dev/maas/proxy/test/checkbox"
url_check = "http://dummy.restapiexample.com/api/v1/create"

response = requests.get(url_get)

print('STATUS:  ', response.status_code)

checkbox 1
checkbox 2

print('RESPONSE:', response.text)
data = response.json()

print('DICT:    ', data)

#*************************************
#*************************************

driver = webdriver.Chrome()
driver.get(url_check)


tbx__search = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
tbx__search = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")

