# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver import FirefoxOptions as Options
from selenium.webdriver import FirefoxService as Service

BROWSER = None


def start_browser():
    options = Options()
    options.binary_location = '/usr/local/bin/firefox'
    options.add_argument('--safe-mode')
    service = Service(executable_path='/usr/local/bin/geckodriver')
    browser = webdriver.Firefox(service=service, options=options)
    return browser


def get_browser():
    global BROWSER
    if BROWSER is None:
        BROWSER = start_browser()
    return BROWSER
