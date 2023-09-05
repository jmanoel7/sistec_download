#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

import os
import sys

dir_base = os.path.join(os.path.curdir, 'sistec_cod_cursos')

file_name_orig = os.path.join(dir_base, 'codes_ead_sort.txt')
file_name_one = os.path.join(dir_base, 'codes_ead_one_sort.txt')
file_name_two = os.path.join(dir_base, 'codes_ead_two_sort.txt')

one_file_ead_course_codes = open(file_name_one, 'w')
two_file_ead_course_codes = open(file_name_two, 'w')

with open(file_name_orig, 'r') as orig_file_ead_course_codes:
    for line in orig_file_ead_course_codes:
        if len(line) < 6:
            one_file_ead_course_codes.write(line)
            one_file_ead_course_codes.flush()
        else:
            two_file_ead_course_codes.write(line)
            two_file_ead_course_codes.flush()

one_file_ead_course_codes.flush()
one_file_ead_course_codes.close()

two_file_ead_course_codes.flush()
two_file_ead_course_codes.close()

sys.exit(0)
