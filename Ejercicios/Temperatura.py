"""
Mostrar la temperaturta de Madrid siendo Madrid una Constate

"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TemperaturaBaja = 25
TemperaturaAlta = 30
Ciudad = "Madrid"


driver = webdriver.Chrome()

try:
    driver.get("http://www.google.es")

    print(driver.title)

    RechazarCookies = driver.find_element(By.ID, "W0wltc")
    tbx__search = driver.find_element(By.ID, "APjFqb")
    temperatura = lambda: driver.find_element(By.ID, "wob_tm")

    RechazarCookies.click()

    tbx__search.send_keys("temperatura " + Ciudad)
    tbx__search.send_keys(Keys.RETURN)

    time.sleep(2)
    temperatura_texto = temperatura().text

    print(temperatura_texto)


    if float(temperatura_texto) < TemperaturaBaja:
        print("Temperatura Baja")
    elif float(temperatura_texto) < TemperaturaAlta:
        print("Temperatura Media")
    else:
        print("Temperatura Alta")

finally:
    time.sleep(3)
    driver.close()
