# -*- coding: utf-8 -*-

import time
import pyautogui as pg
import undetected_chromedriver as uc

# pg.write -> escrever um texto
# pg.press -> apertar 1 tecla
# pg.click -> clicar em algum lugar da tela
# pg.hotkey -> combinação de teclas
pg.PAUSE = 1.0

# # abrir o navegador (google chrome)
# pg.press("win")
# pg.write("google chrome")
# pg.press("enter")
# pg.write("https://sistec.mec.gov.br/")
# pg.press("enter")
# pg.hotkey('alt', 'f4')

# options = uc.ChromeOptions()
driver = uc.Chrome(browser_executable_path=r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
                   driver_executable_path=r'C:\\Users\\joaom\\OneDrive\\bin\\chromedriver.exe')
driver.get('https://sistec.mec.gov.br')

'''continua em breve'''

time.sleep(3600)

driver.quit()
