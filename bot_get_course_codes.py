# -*- coding: utf-8 -*-

import os
import shutil
import sys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from browser import get_browser

get_browser().get('https://sistec.mec.gov.br/')
time_out = 2.5
sleep(time_out)

# Entrada de selecionar perfis
xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/form/div/fieldset/div/select'
while True:
    try:
        select_element = get_browser().find_element(By.XPATH, xpath)
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

dir_base = os.path.join(os.getcwd(), 'sistec_cod_cursos') # <- change here spreadsheets location (PUT THIS LOCATION INSIDE .gitignore)
downloads_path = '/home/joaomanoel/Downloads' # <-- change here downloads location

for campus in campi.items():

    dir_campus = os.path.join(dir_base, campus[0])
    os.mkdir(dir_campus, mode=0o755)

    # seleciona o campus
    xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/form/div/fieldset/div/select'
    select_element = get_browser().find_element(By.XPATH, xpath)
    select_object = Select(select_element)
    select_object.select_by_value(campus[1])
    sleep(time_out)

    # clica no botão acessar
    xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/form/div/fieldset/input'
    sistec_element = get_browser().find_element(By.XPATH, xpath)
    sistec_element.click()
    sleep(time_out)

    # Janela de OK
    #  xpath = '/html/body/div[7]/div[1]/div[2]/div/div/div[2]'
    #  while True:
    #      try:
    #          select_element = get_browser().find_element(By.XPATH, xpath)
    #      except NoSuchElementException:
    #          sleep(time_out)
    #          continue
    #      select_element.click()
    #      break

    # clique na aba 'Cursos'
    xpath = '/html/body/div[2]/div[1]/div[2]/ul[2]/li[6]/a'
    while True:
        try:
            courses_tab = get_browser().find_element(By.XPATH, xpath)
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
            option_cadastro = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    option_cadastro.click()
    sleep(time_out)

    # no 'Menu Cursos' clique na caixinha '+' da opção 'Outros Cursos'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li/ul/li[1]/img[2]'
    while True:
        try:
            option_outros_cursos = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    option_outros_cursos.click()
    sleep(time_out)

    # no 'Menu Cursos' clique na opção 'Listar Existentes'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li/ul/li[1]/ul/li[1]/span/a'
    while True:
        try:
            option_listar_existentes = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    option_listar_existentes.click()
    sleep(time_out)

    # clique no ícone do excel 'Exportar .csv'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[5]/div[2]/div/input[2]'
    while True:
        try:
            excel_exportar_csv = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    excel_exportar_csv.click()
    sleep(time_out)

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
            option_cursos_tecnicos = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    option_cursos_tecnicos.click()
    sleep(time_out)

    # no 'Menu Cursos' clique na opção 'Listar Existentes'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li/ul/li[6]/ul/li/span/a'
    while True:
        try:
            option_listar_existentes = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    option_listar_existentes.click()
    sleep(time_out)

    # na tela principal que se abriu, escolha a Oferta 'Regular' (input type radio button)
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div[1]/div/input[2]'
    while True:
        try:
            radio_button_regular = get_browser().find_element(By.XPATH, xpath)
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
            radio_button_ativo = get_browser().find_element(By.XPATH, xpath)
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
            option_pesquisar = get_browser().find_element(By.XPATH, xpath)
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
            excel_exportar_csv = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    excel_exportar_csv.click()
    sleep(time_out)

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
    sistec_element = get_browser().find_element(By.XPATH, xpath)
    sistec_element.click()
    sleep(time_out)

sys.exit(0)