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

    tbx__search = driver.find_element(By.CSS_SELECTOR, "#tsf > div:nth-child(1) > div.A7Yvie.Epl37 > div.zGVn2e > div.SDkEP > div > style")
    temperatura = lambda: driver.find_element(By.ID, "wob_tm").text

    tbx__search.send_keys("temperatura " + Ciudad)
    tbx__search.send_keys(Keys.RETURN)

    temperatura_texto = temperatura.text

    print(temperatura.text)

    if float(temperatura_texto) < TemperaturaBaja:
        print("Temperatura Baja")
    elif float(temperatura_texto) < TemperaturaAlta:
        print("Temperatura Media")
    else:
        print("Temperatura Alta")

finally:
    time.sleep(3)
    driver.close()
