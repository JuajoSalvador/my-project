import requests
from selenium import webdriver
import json

from selenium.webdriver.common.by import By

url_get = "https://mtp.alejmans.dev/maas/proxy/test/checkbox"
url_check = "https://the-internet.herokuapp.com/checkboxes"

response = requests.get(url_get)

print('STATUS:  ', response.status_code)

#checkbox 1
#checkbox 2

print('RESPONSE:', response.text)
data = response.json()

print('DICT:    ', data)

print('TYPE', type(data))

print('check1: ', data['checkbox 1'])
print('check2: ', data['checkbox 2'])

#*************************************
#*************************************

driver = webdriver.Chrome()
driver.get(url_check)


check1 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
check2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")

if data['checkbox 1']:
    if not check1.is_selected():
        check1.click()
else:
    if check1.is_selected():
        check1.click()

if data['checkbox 2']:
    if not check2.is_selected():
        check2.click()
else:
    if check2.is_selected():
        check2.click()