#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-


import os
import shutil
import sys
from time import sleep

from selenium.common.exceptions import (ElementClickInterceptedException,
                                        ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from browser import get_browser
from campus import campus_dict as campi
from functions import clear_downloads

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

for campus in campi.items():

    # seleciona o campus
    xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/form/div/fieldset/div/select'
    while True:
        try:
            select_element = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                select_object = Select(select_element)
                select_object.select_by_value(campus[1])
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # clica no botão acessar
    xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/form/div/fieldset/input'
    while True:
        try:
            access_button = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                access_button.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # Janela de OK
    # xpath = '/html/body/div[7]/div[1]/div[2]/div/div/div[2]'
    # while True:
    #     try:
    #         ok_window = get_browser().find_element(by=By.XPATH, value=xpath)
    #     except NoSuchElementException:
    #         sleep(time_out)
    #         continue
    #     while True:
    #         try:
    #             ok_window.click()
    #         except ElementNotInteractableException:
    #             sleep(time_out)
    #             continue
    #         except ElementClickInterceptedException:
    #             sleep(time_out)
    #             continue
    #         break
    #     break

    # clica na aba 'Ciclo de Matrícula'
    xpath = '/html/body/div[2]/div[1]/div[2]/ul[2]/li[3]/a'
    while True:
        try:
            ciclo_matricula_tab = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                ciclo_matricula_tab.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
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
            except ElementClickInterceptedException:
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
            except ElementClickInterceptedException:
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
        while True:
            try:
                registro_civil.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # clicar em 'Parte do Nome'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[8]/input[2]'
    while True:
        try:
            parte_nome = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                parte_nome.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # inserir underline '_' no campo para pesquisa por parte do nome do aluno e dar <ENTER>
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[6]/input'
    while True:
        try:
            insert_underline = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                insert_underline.send_keys('_' + Keys.ENTER)
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    # clicar na lupa 'Pesquisar'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[10]/input[1]'
    while True:
        try:
            lupa_pesquisar = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                lupa_pesquisar.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
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
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

    clear_downloads(get_browser(), time_out * 2.0)

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
    while True:
        try:
            sistec_element = get_browser().find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        while True:
            try:
                sistec_element.click()
            except ElementNotInteractableException:
                sleep(time_out)
                continue
            except ElementClickInterceptedException:
                sleep(time_out)
                continue
            break
        break
    sleep(time_out)

get_browser().quit()
sys.exit(0)
