#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys

planilhas = {
    u'CÂMPUS ÁGUAS LINDAS.csv': 3647,
    u'CÂMPUS ANÁPOLIS.csv': 699,
    u'CÂMPUS APARECIDA DE GOIÂNIA.csv': 210,
    u'CÂMPUS CIDADE DE GOIÁS.csv': 696,
    u'CÂMPUS FORMOSA.csv': 2012,
    u'CÂMPUS GOIÂNIA.csv': 212,
    u'CÂMPUS GOIÂNIA OESTE.csv': 3646,
    u'CÂMPUS INHUMAS.csv': 238,
    u'CÂMPUS ITUMBIARA.csv': 244,
    u'CÂMPUS JATAÍ.csv': 241,
    u'CÂMPUS LUZIÂNIA.csv': 209,
    u'CÂMPUS SENADOR CANEDO.csv': 3648,
    u'CÂMPUS URUAÇU.csv': 161,
    u'CÂMPUS VALPARAÍSO.csv': 3649
}

for item in planilhas.iteritems():
    # LÊ ARQUIVOS COM CPF:
    try:
        file_csv_com_cpf = open(path.join(path.curdir, 'com_cpf', item[0]), 'r')
    except:
        e = sys.exc_info()[1]
        print (u'\n\tNão foi possível abrir o arquivo: \"%s\"' % item[0])
        print (u'\n\t\aErro: %s' % e)
        continue
    new_lines = []
    file_csv_com_cpf.readline()
    for line in file_csv_com_cpf:
        new_lines.append(line)
    file_csv_com_cpf.close()
    # LÊ ARQUIVOS SEM CPF:
    try:
        file_csv_sem_cpf = open(path.join(path.curdir, 'sem_cpf', item[0]), 'r')
    except:
        e = sys.exc_info()[1]
        print (u'\n\tNão foi possível abrir o arquivo: \"%s\"' % item[0])
        print (u'\n\t\aErro: %s' % e)
        continue
    file_csv_sem_cpf.readline()
    for line in file_csv_sem_cpf:
        if line not in new_lines:
            new_lines.append(line)
    file_csv_sem_cpf.close()
    # ESCREVE ARQUIVOS CSV:
    try:
        file_csv = open(path.join(path.curdir, item[0]), 'w')
    except:
        e = sys.exc_info()[1]
        print (u'\n\tNão foi possível abrir o arquivo: \"%s\"' % item[0])
        print (u'\n\t\aErro: %s' % e)
        continue
    file_csv.seek(0)
    file_csv.truncate()
    file_csv.write('NO_ALUNO;NU_CPF;CO_CURSO;DT_DATA_INICIO;DT_DATA_FIM_PREVISTO;NO_CICLO_MATRICULA;CO_TIPO_OFERTA_CURSO;CO_POLO;NO_STATUS_MATRICULA\n')
    file_csv.writelines(new_lines)
    file_csv.flush()
    file_csv.close()
