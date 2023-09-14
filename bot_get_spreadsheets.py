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
git_project_path = os.getenv('GIT_PROJECT_PATH')
sistec_audit_path = os.path.join(git_project_path, 'sistec_audit') # <- change here spreadsheets (sistec data) location (PUT THIS LOCATION INSIDE .gitignore)
spreadsheets_path = os.path.join(sistec_audit_path, 'presencial')
spreadsheets_ead_path = os.path.join(sistec_audit_path, 'ead')

try:
    os.mkdir(sistec_audit_path, mode=0o755)
except FileExistsError:
    os.chmod(sistec_audit_path, mode=0o755)

try:
    os.mkdir(spreadsheets_path, mode=0o755)
except FileExistsError:
    os.chmod(spreadsheets_path, mode=0o755)

try:
    os.mkdir(spreadsheets_ead_path, mode=0o755)
except FileExistsError:
    os.chmod(spreadsheets_ead_path, mode=0o755)

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

# Códigos do Campus do IFG
campi = {
    u'CÂMPUS ÁGUAS LINDAS': '1660670',
    u'CÂMPUS ANÁPOLIS': '1660636',
    u'CÂMPUS APARECIDA DE GOIÂNIA': '1660641',
    u'CÂMPUS CIDADE DE GOIÁS': '1660637',
    u'CÂMPUS FORMOSA': '1660650',
    u'CÂMPUS GOIÂNIA': '1660652',
    u'CÂMPUS GOIÂNIA OESTE': '1660653',
    u'CÂMPUS INHUMAS': '1660662',
    u'CÂMPUS ITUMBIARA': '1660663',
    u'CÂMPUS JATAÍ': '1660664',
    u'CÂMPUS LUZIÂNIA': '1660666',
    u'CÂMPUS SENADOR CANEDO': '1662833',
    u'CÂMPUS URUAÇU': '1660667',
    u'CÂMPUS VALPARAÍSO': '1660669'
}

for campus in campi.items():

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

    # clica na aba 'Ciclo de Matrícula'
    xpath = '/html/body/div[2]/div[1]/div[2]/ul[2]/li[3]/a'
    while True:
        try:
            ciclo_matricula_tab = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    ciclo_matricula_tab.click()
    sleep(time_out)

    # clica na caixinha de '+' do aluno
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li[2]/img[1]'
    while True:
        try:
            aluno_mais = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                aluno_mais.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # clicar em 'Pesquisar Aluno'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li[2]/ul/li[7]/span/a'
    while True:
        try:
            pesquisar_aluno = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                pesquisar_aluno.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # clicar em 'Registro Civil'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[5]/input[1]'
    while True:
        try:
            registro_civil = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    registro_civil.click()
    sleep(time_out)

    # clicar em 'Parte do Nome'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[8]/input[2]'
    while True:
        try:
            parte_nome = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    parte_nome.click()
    sleep(time_out)

    # inserir underline '_' no campo para pesquisa por parte do nome do aluno e dar <ENTER>
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[6]/input'
    while True:
        try:
            insert_underline = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    insert_underline.send_keys('_' + Keys.ENTER)
    sleep(time_out)

    # clicar na lupa 'Pesquisar'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[10]/input[1]'
    while True:
        try:
            lupa_pesquisar = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    lupa_pesquisar.click()
    sleep(time_out)

    # clique no ícone do excel 'Exportar csv'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[5]/div[2]/div/a[5]/input'
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

    # renomeia o arquivo sistec.csv de acordo com o Campus selecionado
    sistec_csv = os.path.join(downloads_path, 'sistec.csv')
    campus_csv = os.path.join(spreadsheets_path, campus[0] + '.csv')
    campus_ead_csv = os.path.join(spreadsheets_ead_path, campus[0] + '.csv')
    while True:
        try:
            shutil.copyfile(sistec_csv, campus_csv)
            shutil.copyfile(sistec_csv, campus_ead_csv)
        except FileNotFoundError:
            sleep(time_out)
            continue
        break
    os.remove(sistec_csv)
    sleep(time_out)

    # clicar em 'Alterar Perfil'
    xpath = '/html/body/div[2]/div[1]/div[2]/ul[3]/li[5]/a'
    sistec_element = get_browser().find_element(by=By.XPATH, value=xpath)
    sistec_element.click()
    sleep(time_out)

get_browser().quit()
sys.exit(0)
