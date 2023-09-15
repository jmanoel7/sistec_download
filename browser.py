# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

BROWSER = None


def start_browser():
    options = Options()
    options.binary_location = '/usr/bin/firefox-esr' # <-- change here firefox binary location
    options.add_argument('--safe-mode') # <-- start in safe-mode (disables extensions and themes for this session)
    options.add_argument('-P Developer') # <-- choice profile 'Developer'
    service = Service(executable_path='/usr/local/bin/geckodriver') # <-- change here geckodriver binary location
    browser = webdriver.Firefox(service=service, options=options)
    return browser


def get_browser():
    global BROWSER
    if BROWSER is None:
        BROWSER = start_browser()
    return BROWSER
