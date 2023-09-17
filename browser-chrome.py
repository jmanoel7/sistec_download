# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver import ChromeOptions as Options
from selenium.webdriver import ChromeService as Service

BROWSER = None


def start_browser():
    options = Options()
    options.binary_location = '/usr/bin/google-chrome'
    #  options.add_argument('--start-maximized')
    service = Service(executable_path='/usr/local/bin/chromedriver')
    browser = webdriver.Chrome(service=service, options=options)
    return browser


def get_browser():
    global BROWSER
    if BROWSER is None:
        BROWSER = start_browser()
    return BROWSER
