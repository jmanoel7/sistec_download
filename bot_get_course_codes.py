#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-


import os
import shutil
import sys
from time import sleep

import pyautogui as pg
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from browser import get_browser
from campus import campus_dict as campi


def clear_downloads(m_browser, m_time_out):
    sleep(m_time_out)
    main_window = m_browser.current_window_handle
    m_browser.switch_to.new_window('tab')
    m_browser.get('about:downloads')
    max_x, max_y = pg.size()
    pg.click(x=max_x/2.0, y=max_y/2.0, duration=1.0, button='right')
    sleep(1.0)
    pg.press('C')
    sleep(m_time_out)
    m_browser.close()
    m_browser.switch_to.window(main_window)
    return None


user_path = os.getenv('HOME')
downloads_path = os.path.join(user_path, 'Downloads') # <- change here downloads location
dir_base = os.path.join(os.getcwd(), 'sistec_course_codes') # <- change here spreadsheets (course codes) location (PUT THIS LOCATION INSIDE .gitignore)

get_browser().maximize_window()
get_browser().get('https://sistec.mec.gov.br/')
time_out = 2.5
sleep(time_out)

# Entrada de selecionar perfis
xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/form/div/fieldset/div/select'
while True:
    try:
        select_element = get_browser().find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        sleep(time_out)
        continue
    break

for campus in campi.items():

    # clear and create dir_campus
    dir_campus = os.path.join(dir_base, campus[0])
    try:
        os.removedirs(dir_campus)
    except FileNotFoundError:
        pass
    os.makedirs(dir_campus, mode=0o755)

    # seleciona o campus
    xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/form/div/fieldset/div/select'
    select_element = get_browser().find_element(by=By.XPATH, value=xpath)
    select_object = Select(select_element)
    select_object.select_by_value(campus[1])
    sleep(time_out)

    # clica no botão acessar
    xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/form/div/fieldset/input'
    access_button = get_browser().find_element(by=By.XPATH, value=xpath)
    access_button.click()
    sleep(time_out)

    # Janela de OK
    #  xpath = '/html/body/div[7]/div[1]/div[2]/div/div/div[2]'
    #  while True:
    #      try:
    #          ok_window = get_browser().find_element(by=By.XPATH, value=xpath)
    #      except NoSuchElementException:
    #          sleep(time_out)
    #          continue
    #      ok_window.click()
    #      break

    # clique na aba 'Cursos'
    xpath = '/html/body/div[2]/div[1]/div[2]/ul[2]/li[6]/a'
    while True:
        try:
            courses_tab = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    courses_tab.click()
    sleep(time_out)

    # no 'Menu Cursos' clique na caixinha '+' da opção 'Cadastro'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li/img[1]'
    while True:
        try:
            option_cadastro = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                option_cadastro.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # no 'Menu Cursos' clique na caixinha '+' da opção 'Outros Cursos'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li/ul/li[1]/img[2]'
    while True:
        try:
            option_outros_cursos = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                option_outros_cursos.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # no 'Menu Cursos' clique na opção 'Listar Existentes'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li/ul/li[1]/ul/li[1]/span/a'
    while True:
        try:
            option_listar_existentes = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                option_listar_existentes.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # clique no ícone do excel 'Exportar .csv'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[5]/div[2]/div/input[2]'
    while True:
        try:
            excel_exportar_csv = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                excel_exportar_csv.click()
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    clear_downloads(get_browser(), time_out)

    # move o arquivo sistec_csv.csv do diretório de downloads para o diretório do câmpus atual
    file_sistec_csv = os.path.join(downloads_path, 'sistec_csv.csv')
    while True:
        try:
            shutil.move(file_sistec_csv, dir_campus)
        except FileNotFoundError:
            sleep(time_out)
            continue
        break
    sleep(time_out)

    # no 'Menu Cursos' clique na caixinha '+' da opção 'Cursos Técnicos'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li/ul/li[6]/img[2]'
    while True:
        try:
            option_cursos_tecnicos = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                option_cursos_tecnicos.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # no 'Menu Cursos' clique na opção 'Listar Existentes'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li/ul/li[6]/ul/li/span/a'
    while True:
        try:
            option_listar_existentes = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                option_listar_existentes.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # na tela principal que se abriu, escolha a Oferta 'Regular' (input type radio button)
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div[1]/div/input[2]'
    while True:
        try:
            radio_button_regular = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    radio_button_regular.click()
    sleep(time_out)

    # na tela principal que se abriu, escolha a Situação 'Ativo' (input type radio button)
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div[5]/div/input[1]'
    while True:
        try:
            radio_button_ativo = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    radio_button_ativo.click()
    sleep(time_out)

    # na tela principal que se abriu, clique na opção 'Pesquisar'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/div[1]/input[1]'
    while True:
        try:
            option_pesquisar = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    option_pesquisar.click()
    sleep(time_out)

    # clique no ícone do excel 'Exportar .csv'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[5]/div[2]/div[1]/input[2]'
    while True:
        try:
            excel_exportar_csv = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                excel_exportar_csv.click()
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    clear_downloads(get_browser(), time_out)

    # move o arquivo cursos_tecnicos.csv do diretório de downloads para o diretório do câmpus atual
    file_cursos_tecnicos = os.path.join(downloads_path, 'cursos_tecnicos.csv')
    while True:
        try:
            shutil.move(file_cursos_tecnicos, dir_campus)
        except FileNotFoundError:
            sleep(time_out)
            continue
        break
    sleep(time_out)

    # clicar em 'Alterar Perfil'
    xpath = '/html/body/div[2]/div[1]/div[2]/ul[3]/li[5]/a'
    sistec_element = get_browser().find_element(by=By.XPATH, value=xpath)
    sistec_element.click()
    sleep(time_out)

get_browser().quit()
sys.exit(0)
