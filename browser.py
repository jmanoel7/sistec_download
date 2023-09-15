# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver import FirefoxOptions as Options
from selenium.webdriver import FirefoxService as Service

BROWSER = None


def start_browser():
    options = Options()
    options.binary_location = '/usr/bin/firefox-esr' # <-- change here firefox binary location
    # sudo apt-get install --yes firefox-esr
    # create profile 'developer-esr' with command 'firefox-esr -P'
    # init firefox-esr and choice profile 'developer-esr'
    # now open url 'about:config' and set config:
    # 1) moz:debuggerAddress -> true
    # 2) fission.bfcacheInParent -> false
    # 3) fission.webContentIsolationStrategy -> 0
    options.add_argument('--safe-mode') # <-- start in safe-mode (disables extensions and themes for this session)
    options.add_argument('-P developer-esr') # <-- choice created profile 'developer-esr'
    service = Service(executable_path='/usr/local/bin/geckodriver') # <-- change here geckodriver binary location
    browser = webdriver.Firefox(options=options, service=service)
    return browser


def get_browser():
    global BROWSER
    if BROWSER is None:
        BROWSER = start_browser()
    return BROWSER
