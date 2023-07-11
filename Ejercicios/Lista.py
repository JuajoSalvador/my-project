
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/tables"

def get_dollars(d, fila):
    celda = d.find_element(By.CSS_SELECTOR, f"#table1 > tbody > tr:nth-child({fila}) > td:nth-child(4)")
    texto_celda = celda.text
    return int(texto_celda.split(".")[0].lstrip("$"))


def get_persona(d, fila):
    celda = d.find_element(By.CSS_SELECTOR, f"#table1 > tbody > tr:nth-child({fila}) > td:nth-child(1)")
    texto_celda = celda.text
    return texto_celda


driver = webdriver.Chrome()
try:

    fila = driver.find_element(By.CSS_SELECTOR, "#table1 > tbody > tr:nth - last - child(1)")
    print(fila)

    driver.get(URL)
    dollars = []
    for i in range(4):
        dollars.append(get_dollars(driver, i + 1))

    filas_con_mas_de_50 = []
    for i, dollar in enumerate(dollars):
        if dollar > 50:
            filas_con_mas_de_50.append(i)

    personas = []
    for i in range(4):
        personas.append(get_persona(driver, i + 1))

finally:
    driver.quit()


for fila in filas_con_mas_de_50:
    print("nombre: "  + personas[fila])
