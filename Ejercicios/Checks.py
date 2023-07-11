"""
Lanzar una Request para obtenenr 2 valores booleano que hará que marquemos 2 checks en otra página

"""

import requests
from selenium import webdriver
import json

from selenium.webdriver.common.by import By

from Ejercicios.pageobjects.checkbox_apge import CheckboxPage

url_get = "https://mtp.alejmans.dev/maas/proxy/test/checkbox"
url_check = "https://the-internet.herokuapp.com/checkboxes"

response = requests.get(url_get)

print('STATUS:  ', response.status_code)
print('RESPONSE:', response.text)

data = response.json()

print('DICT:    ', data)

print('check1: ', data['checkbox 1'])
print('check2: ', data['checkbox 2'])

#*************************************
#*************************************

driver = webdriver.Chrome()


try:
    driver.get(url_check)

    #check1 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
    #check2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")
    #los tengo en poageobjects

    page = CheckboxPage(driver)

    if data['checkbox 1']:
        if not page.check1.is_selected():
            page.check1.click()
    else:
        if page.check1.is_selected():
            page.check1.click()

    if data['checkbox 2']:
        if not page.check2.is_selected():
            page.check2.click()
    else:
        if page.check2.is_selected():
            page.check2.click()
finally:
    print ("todo correcto")
    #driver.quit()