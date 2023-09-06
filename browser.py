# -*- coding: utf-8 -*-


from time import strftime
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions as Options
from selenium.webdriver.chromium.service import ChromiumService as Service


BROWSER = None


def start_browser():
    options = Options()
    options.binary_location = '/usr/bin/chromium'
    service = Service('/usr/bin/chromedriver', start_error_message='%s\t' % strftime('[%Y-%m-%d %H:%M:%S]'))
    browser = webdriver.Chrome(service=service, options=options)
    return browser


def get_browser():
    global BROWSER
    if BROWSER is None:
        BROWSER = start_browser()
    return BROWSER
