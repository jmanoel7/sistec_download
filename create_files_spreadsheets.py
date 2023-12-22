# -*- coding: utf-8 -*-


import os
import shutil
import sys
from campus import campus_list as campi


dir_audit_path        = os.getenv('DIR_AUDIT')
spreadsheets_path     = os.path.join(dir_audit_path, 'presencial')
spreadsheets_ead_path = os.path.join(dir_audit_path, 'ead')


for campus in campi:

    dir_campus_path = os.path.join(spreadsheets_path, campus)
    sistec_csv = os.path.join(dir_campus_path, 'sistec.csv')
    campus_csv = os.path.join(spreadsheets_path, campus + '.csv')
    shutil.copyfile(sistec_csv, campus_csv)
    shutil.rmtree(dir_campus_path)

    dir_campus_ead_path = os.path.join(spreadsheets_ead_path, campus)
    sistec_ead_csv = os.path.join(dir_campus_ead_path, 'sistec.csv')
    campus_ead_csv = os.path.join(spreadsheets_ead_path, campus + '.csv')
    shutil.copyfile(sistec_ead_csv, campus_ead_csv)
    shutil.rmtree(dir_campus_ead_path)


sys.exit(0)

