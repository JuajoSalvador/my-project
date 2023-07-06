"""
Imprimir por pantalla la temperatura en Madrid y añadir un mensaje indicando en cual de estas franjas está:
franja 1:  < 25ºC
franja 2:  25ºC < x < 30ºC
franja 3:  > 30ºC
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

T_B = 25
T_A = 30
CIUDAD = 'Madrid'

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get('https://www.google.com/search?q=tiempo+en+madrid&source=hp&ei=yLmlZNvuDYWJkdUPnvOx6Ao&iflsig=AD69kcEAAAAAZKXH2NNc-Q8RvGzfEfafzKtk26SZ3qWC&ved=0ahUKEwjb8r2wnPj_AhWFRKQEHZ55DK0Q4dUDCAo&uact=5&oq=tiempo+en+madrid&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQgAIyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQ6EAgAEAMQjwEQ6gIQjAMQ5QI6EAguEAMQjwEQ6gIQjAMQ5QI6CwgAEIAEELEDEIMBOgsIABCKBRCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CwguEIAEELEDEIMBOgsILhCKBRCxAxCDAToOCAAQgAQQsQMQgwEQyQM6CAgAEIAEEJIDOggIABCKBRCSA1C4B1ihFGC_FWgBcAB4AIABywGIAZUPkgEGMC4xNS4xmAEAoAEBsAEK&sclient=gws-wiz')

    texto_temperatura = float(driver.find_element(By.ID, 'wob_tm').text)

    print (f'La temperatura en ', CIUDAD,' es: ',texto_temperatura, 'grados')

    if texto_temperatura < T_B:
        print ('La temperatura es baja para la época')
    elif texto_temperatura > T_A:
        print ('La temperatura es alta')
    else:
        print ('La temperatura es la adecuada para la época')

finally:
    time.sleep(3)
    driver.close()