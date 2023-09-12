#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-


import os
import sys

dir_base = os.path.join(os.getcwd(), 'sistec_course_codes')
os.chdir(dir_base)

file_name_course_codes = os.path.join(dir_base, 'codes.txt')
file_name_ead_course_codes = os.path.join(dir_base, 'codes_ead.txt')

lista_campus = [
    u'CÂMPUS ÁGUAS LINDAS',
    u'CÂMPUS ANÁPOLIS',
    u'CÂMPUS APARECIDA DE GOIÂNIA',
    u'CÂMPUS CIDADE DE GOIÁS',
    u'CÂMPUS FORMOSA',
    u'CÂMPUS GOIÂNIA',
    u'CÂMPUS GOIÂNIA OESTE',
    u'CÂMPUS INHUMAS',
    u'CÂMPUS ITUMBIARA',
    u'CÂMPUS JATAÍ',
    u'CÂMPUS LUZIÂNIA',
    u'CÂMPUS SENADOR CANEDO',
    u'CÂMPUS URUAÇU',
    u'CÂMPUS VALPARAÍSO'
]

file_course_codes = open(file_name_course_codes, 'w')
file_ead_course_codes = open(file_name_ead_course_codes, 'w')

for campus in lista_campus:

    os.chdir(campus)

    with open('sistec_csv.csv', 'rb') as sistec_course_codes:

        sistec_course_codes.readline()

        for line in sistec_course_codes:

            line = line.decode('iso-8859-1')
            line_items = line.split(';')

            education_model = line_items[23].strip('\"').strip()
            course_code = line_items[16].strip('\"').strip()

            if education_model == u'EDUCAÇÃO PRESENCIAL':

                file_course_codes.write(f'{course_code}\n')
                file_course_codes.flush()

            elif education_model == u'EDUCAÇÃO A DISTÂNCIA':

                file_ead_course_codes.write(f'{course_code}\n')
                file_ead_course_codes.flush()

            else:

                raise KeyError

    with open('cursos_tecnicos.csv', 'rb') as technician_course_codes:

        technician_course_codes.readline()

        for line in technician_course_codes:

            line = line.decode('iso-8859-1')
            line_items = line.split(';')

            education_model = line_items[31].strip()
            course_code = line_items[23].strip()

            if education_model == u'EDUCAÇÃO PRESENCIAL':

                file_course_codes.write(f'{course_code}\n')
                file_course_codes.flush()

            elif education_model == u'EDUCAÇÃO A DISTÂNCIA':

                file_ead_course_codes.write(f'{course_code}\n')
                file_ead_course_codes.flush()

            else:

                raise KeyError

    os.chdir(os.path.pardir)

file_course_codes.close()
file_ead_course_codes.close()

os.chdir(os.path.pardir)

sys.exit(0)
