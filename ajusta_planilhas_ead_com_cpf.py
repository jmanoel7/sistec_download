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

for item in planilhas.iteritems():
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
        # 00: CO_ALUNO_IDENTIFICADO
        # 01: CO_ALUNO
        # 02: NO_ALUNO
        # 03: NO_MAE_ALUNO
        # 04: NO_NOME_SOCIAL
        # 05: NU_CPF
        # 06: DS_EMAIL
        # 07: CO_PESSOA_FISICA_ALUNO
        # 08: DS_SENHA
        # 09: CO_MATRICULA
        # 10: CO_CICLO_MATRICULA
        # 11: CO_STATUS_CICLO_MATRICULA
        # 12: CO_CURSO
        # 13: NU_CARGA_HORARIA
        # 14: DT_DATA_INICIO
        # 15: DT_DATA_FIM_PREVISTO
        # 16: CO_UNIDADE_ENSINO
        # 17: CO_PERIODO_CADASTRO
        # 18: NO_CICLO_MATRICULA
        # 19: ST_ATIVO
        # 20: CO_TIPO_OFERTA_CURSO
        # 21: CO_TIPO_INSTITUICAO
        # 22: CO_INSTITUICAO
        # 23: CO_PORTFOLIO
        # 24: CO_TIPO_NIVEL_OFERTA_CURSO
        # 25: CO_TIPO_PROGRAMA_CURSO
        # 26: ST_CARGA
        # 27: DT_DATA_FINALIZADO
        # 28: NU_VAGAS_OFERTADAS
        # 29: NU_TOTAL_INSCRITOS
        # 30: ST_ETEC
        # 31: CO_POLO
        # 32: UAB
        # 33: ST_PREVISTO
        # 34: NU_VAGAS_PREVISTAS
        # 35: CO_CURSO_SUPERIOR_CORRELATO
        # 36: NU_CARGA_HORARIA_ESTAGIO
        # 37: NO_ARQUIVO
        # 38: NO_CAMINHO_ARQUIVO
        # 39: ST_ESTAGIO
        # 40: ST_EXPERIMENTAL
        # 41: NO_STATUS_MATRICULA
        # 42: CO_PESSOA_FISICA
        # 43: NU_RG
        # 44: SG_SEXO
        # 45: DT_NASCIMENTO
        # 46: NO_PESSOA_FISICA
        # 47: CO_PESSOA
        # 48: CO_CARGO
        # 49: DS_ORGAO_EXPEDIDOR
        # 50: SG_UF_ORG_EXPED
        # 51: DS_CARGO
        # 52: CO_UNIDADE_ENSINO_IMPORTACAO
        # 53: CO_MATRICULA_RESPONSAVEL
        # 54: NO_SOCIAL
        # USAREMOS AS SEGUINTES COLUNAS:
        # 02; 05; 12; 14; 15; 18; 20; 31; 41
        line_items = line.split(';')
        new_line_items[0] = line_items[2].strip('\"')
        new_line_items[1] = line_items[5].strip('\"')
        new_line_items[2] = line_items[12].strip('\"')
        new_line_items[3] = line_items[14].strip('\"')
        new_line_items[4] = line_items[15].strip('\"')
        new_line_items[5] = line_items[18].strip('\"')
        new_line_items[6] = line_items[20].strip('\"')
        new_line_items[7] = line_items[31].strip('\"')
        new_line_items[8] = line_items[41].strip('\"')
        # VERIFICA SE CURSO EH DO TIPO EAD:
        re_ead = re.compile(u'^.*[AÀÁ]\s*DIST[AÂ]NCIA.*$')
        match_ead = re_ead.search(new_line_items[5])
        if not match_ead:
            continue
        if int(new_line_items[2]) not in [29, 31, 32, 34, 47, 85, 154, 158]:
            continue
        # AJUSTA O POLO
        new_line_items[7] = str(item[1])
        # AJUSTA O CPF
        if new_line_items[1].strip(' ') != '':
            cpf = new_line_items[1][0:3] + '.' + new_line_items[1][3:6] + '.' + new_line_items[1][6:9] + '-' + new_line_items[1][9:11]
        else:
            cpf = '000.000.000-00'
        new_line_items[1] = cpf
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
