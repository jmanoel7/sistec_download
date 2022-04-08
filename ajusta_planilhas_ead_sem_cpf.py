#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys
import re

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

for item in planilhas.items():
    try:
        file_csv = open(path.join(path.curdir, item[0]), 'r+')
    except:
        e = sys.exc_info()[1]
        print (u'\n\tNão foi possível abrir o arquivo: \"%s\"' % item[0])
        print (u'\n\t\aErro: %s' % e)
        continue
    new_lines = []
    new_line_items = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    file_csv.readline()
    for line in file_csv:
        # COLUNAS DO ARQUIVO CSV
        # 00: CO_ALUNO            01: NO_ALUNO	           02: SG_SEXO	           03: DT_DATA_NASCIMENTO 04: DS_EMAIL	05: CO_PESSOA_FISICA_ALUNO
        # 06: DS_SENHA            07: CO_MATRICULA         08: CO_CICLO_MATRICULA  09: CO_CURSO           10: NU_CARGA_HORARIA
        # 11: DT_DATA_INICIO      12: DT_DATA_FIM_PREVISTO 13: CO_PERIODO_CADASTRO 14: NO_CICLO_MATRICULA 15: CO_TIPO_OFERTA_CURSO
        # 16: CO_TIPO_INSTITUICAO 17: CO_PORTFOLIO         18: NU_VAGAS_OFERTADAS  19: NU_TOTAL_INSCRITOS 20: NO_STATUS_MATRICULA
        # 21: CO_UNIDADE_ENSINO   22: MES_DE_OCORRENCIA
        # USAREMOS OS CAMPOS:
        # 01; CPF_ZERO; 09; 11; 12; 14; 15; item[1]; 20
        line_items = line.split(';')
        new_line_items[0] = line_items[1].strip('\"')
        new_line_items[1] = '000.000.000-00'
        new_line_items[2] = line_items[9].strip('\"')
        new_line_items[3] = line_items[11].strip('\"')
        new_line_items[4] = line_items[12].strip('\"')
        new_line_items[5] = line_items[14].strip('\"')
        new_line_items[6] = line_items[15].strip('\"')
        new_line_items[7] = str(item[1])
        new_line_items[8] = line_items[20].strip('\"')
        # VERIFICA SE CURSO EH DO TIPO EAD:
        re_ead = re.compile(u'^.*[AÀÁ]\s*DIST[AÂ]NCIA.*$')
        match_ead = re_ead.search(new_line_items[5])
        if not match_ead:
            continue
        if int(new_line_items[2]) not in [29, 31, 32, 34, 40, 47, 85, 154, 158]:
            continue
        # AJUSTA AS DATAS
        dt_inicio = new_line_items[3][8:10] + '/' + new_line_items[3][5:7] + '/' + new_line_items[3][0:4]
        dt_fim = new_line_items[4][8:10] + '/' + new_line_items[4][5:7] + '/' + new_line_items[4][0:4]
        new_line_items[3] = dt_inicio
        new_line_items[4] = dt_fim
        # CRIA UMA LINHA NOVA E ADICIONA SE NÃO FOR UMA LINHA REPETIDA
        new_line = ';'.join(new_line_items)
        new_line = new_line + '\n'
        if new_line in new_lines:
            print(new_line)
            continue
        new_lines.append(new_line)
    file_csv.seek(0)
    file_csv.truncate()
    file_csv.write('NO_ALUNO;NU_CPF;CO_CURSO;DT_DATA_INICIO;DT_DATA_FIM_PREVISTO;NO_CICLO_MATRICULA;CO_TIPO_OFERTA_CURSO;CO_POLO;NO_STATUS_MATRICULA\n')
    file_csv.writelines(new_lines)
    file_csv.flush()
    file_csv.close()
