# -*- coding: utf-8 -*-


import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from browser import get_browser


get_browser().get('https://sistec.mec.gov.br/')
time_out = 2.5
sleep(time_out)

# Entrada de selecionar perfis
xpath = '//*[@id="tipo"]'
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

for campus in campi.items():

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

    # clica na aba 'Ciclo de Matrícula'
    xpath = '/html/body/div[2]/div[1]/div[2]/ul[2]/li[3]/a'
    while True:
        try:
            sistec_element = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    sistec_element.click()
    sleep(time_out)

    # clica na caixinha de '+' do aluno
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li[2]/img[1]'
    sistec_element = get_browser().find_element(By.XPATH, xpath)
    sistec_element.click()
    sleep(time_out)

    # clicar em 'Pesquisar Aluno'
    xpath = '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/ul/li[2]/ul/li[7]/span/a'
    sistec_element = get_browser().find_element(By.XPATH, xpath)
    sistec_element.click()
    sleep(time_out)

    # clicar em 'Registro Civil'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[5]/input[1]'
    sistec_element = get_browser().find_element(By.XPATH, xpath)
    sistec_element.click()
    sleep(time_out)

    # clicar em 'Parte do Nome'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[8]/input[2]'
    sistec_element = get_browser().find_element(By.XPATH, xpath)
    sistec_element.click()
    sleep(time_out)

    # inserir underline '_' no campo para pesquisa por parte do nome do aluno e dar <ENTER>
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[6]/input'
    sistec_element = get_browser().find_element(By.XPATH, xpath)
    sistec_element.send_keys('_' + Keys.ENTER)
    sleep(time_out)

    # clicar na lupa 'Pesquisar'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[3]/form/div/div[10]/input[1]'
    sistec_element = get_browser().find_element(By.XPATH, xpath)
    sistec_element.click()
    sleep(time_out)

    # clique no ícone do excel 'Exportar csv'
    xpath = '/html/body/div[2]/div[3]/div[3]/div[5]/div[2]/div/a[5]/input'
    while True:
        try:
            sistec_element = get_browser().find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(time_out)
            continue
        break
    sistec_element.click()
    sleep(time_out)

    # renomeia o arquivo sistec.csv de acordo com o Campus selecionado
    root_path = '/home/joaomanoel/Downloads/'
    sistec_csv = os.path.join(root_path, 'sistec.csv')
    campus_csv = os.path.join(root_path, campus[0] + '.csv')
    while True:
        try:
            os.rename(sistec_csv, campus_csv)
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

