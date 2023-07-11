""""crear 10 elementos dándole a "add" en esta web

https://the-internet.herokuapp.com/add_remove_elements/

y luego borrarlos dándole a "delete"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/add_remove_elements/"
driver = webdriver.Chrome()

Add = lambda: driver.find_element(By.CSS_SELECTOR, "#content > div > button")

try:
    #Abrimos y maximizamos chorme
    driver.get(URL)
    driver.maximize_window()

    #añadimos 10 elementos haciendo click 10 veces
    for i in range(10):
        Add().click()

    #esperamos para evr el resultado
    time.sleep(3)

    #borramos el boton1 10 veces
    for i in range(10):
        delete = driver.find_element(By.CSS_SELECTOR, "#elements > button:nth-child(1)")
        delete.click()

    # esperamos para ver el resultado
    time.sleep(3)

finally:
    print("Todo correcto")
    driver.quit()

