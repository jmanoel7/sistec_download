#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-


import os
import re
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

for item in planilhas.items():
    print(item[0])
    print('INÍCIO')
    try:
        file_csv = open(os.path.join(os.path.curdir, item[0]), 'rb+')
    except:
        e = sys.exc_info()[1]
        print (u'\n\tNão foi possível abrir o arquivo: \"%s\"' % item[0])
        print (u'\n\t\aErro: %s' % e)
        continue
    new_lines = []
    new_line_items = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    file_csv.readline()
    for line in file_csv:
        line = line.decode('iso-8859-1')

        # COLUNAS DO ARQUIVO CSV

        # 00: CO_ALUNO_IDENTIFICADO    01: CO_ALUNO               02: NO_ALUNO
        # 03: NO_MAE_ALUNO             04: SG_SEXO                05: DT_DATA_NASCIMENTO
        # 06: NU_CPF                   07: DS_EMAIL               08: CO_PESSOA_FISICA_ALUNO
        # 09: DS_SENHA                 10: CO_MATRICULA           11: CO_CICLO_MATRICULA
        # 12: CO_CURSO                 13: NU_CARGA_HORARIA       14: DT_DATA_INICIO
        # 15: DT_DATA_FIM_PREVISTO     16: CO_PERIODO_CADASTRO    17: NO_CICLO_MATRICULA
        # 18: CO_TIPO_OFERTA_CURSO     19: CO_TIPO_INSTITUICAO    20: CO_PORTFOLIO
        # 21: NU_VAGAS_OFERTADAS       22: NU_TOTAL_INSCRITOS     23: NO_STATUS_MATRICULA
        # 24: CO_UNIDADE_ENSINO        25: MES_DE_OCORRENCIA

        # USAREMOS AS SEGUINTES COLUNAS:
        # 02; 06; 12; 14; 15; 17; 18; item[1]; 23

        line_items = line.split(';')
        try:
            new_line_items[0] = line_items[2].strip('\"')
            new_line_items[1] = line_items[6].strip('\"')
            new_line_items[2] = line_items[12].strip('\"')
            new_line_items[3] = line_items[14].strip('\"')
            new_line_items[4] = line_items[15].strip('\"')
            new_line_items[5] = line_items[17].strip('\"')
            new_line_items[6] = line_items[18].strip('\"')
            new_line_items[7] = str(item[1])
            new_line_items[8] = line_items[23].strip('\"')
        except IndexError:
            print('Erro:')
            print(line)
            os._exit(1)
        # VERIFICA SE CURSO EH DO TIPO EAD:
        re_ead = re.compile(u'^.*[AÀÁ]\s*DIST[AÂ]NCIA.*$')
        match_ead = re_ead.search(new_line_items[5])
        if not match_ead:
            continue
        cursos = [
            # -----BEGIN DISTANCE COURSE CODES-----
            29, 31, 32, 34, 40,
            47, 85, 154, 158
            # -----END DISTANCE COURSE CODES-----
        ]
        if int(new_line_items[2]) not in cursos:
            continue
        # AJUSTA O CPF
        if new_line_items[1].strip(' ') != '':
            cpf = new_line_items[1].strip(' ')
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
        new_line = new_line.encode('iso-8859-1')
        if new_line in new_lines:
            print(new_line)
            continue
        new_lines.append(new_line)
    file_csv.seek(0)
    file_csv.truncate()
    file_csv.write('NO_ALUNO;NU_CPF;CO_CURSO;DT_DATA_INICIO;DT_DATA_FIM_PREVISTO;NO_CICLO_MATRICULA;CO_TIPO_OFERTA_CURSO;CO_POLO;NO_STATUS_MATRICULA\n'.encode('iso-8859-1'))
    file_csv.writelines(new_lines)
    file_csv.flush()
    file_csv.close()
    print('FIM')
