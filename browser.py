# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

BROWSER = None


def start_browser():
    options = Options()
    options.binary_location = '/home/joaomanoel/.local/chrome-linux64/chrome'
    options.add_argument('--start-maximized')
    service = Service('/home/joaomanoel/.local/bin/chromedriver')
    browser = webdriver.Chrome(service=service, options=options)
    return browser


def get_browser():
    global BROWSER
    if BROWSER is None:
        BROWSER = start_browser()
    return BROWSER
