import time

import action as action
import requests
from selenium import webdriver
import json

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Ejercicios.pageobjects.checkbox_apge import CheckboxPage

url = "https://the-internet.herokuapp.com/hovers"
url2 = "https://the-internet.herokuapp.com/windows"

driver = webdriver.Chrome()




try:

    driver.get(url2)

    """Mouse Over"""
    Foto1 = lambda: driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(3) > img")
    Link1 = lambda: driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(3) > div > a")

    link =  lambda: driver.find_element(By.CSS_SELECTOR, "#content > div > a")

    """driver.get(url)
    
    a = ActionChains(driver)
    a.move_to_element(Foto1).perform()
    Link1().click()
    time.sleep(3)"""

    #action = webdriver.ActionChains(driver)
    #action.move_to_element(Foto1)
    #action.perform()
    #Link1().click()




    link().click()

    time.sleep(3)
    #parent = driver.window_handles[0]
    #child =  driver.window_handles[1]
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    time.sleep(3)

finally:
    driver.quit()


