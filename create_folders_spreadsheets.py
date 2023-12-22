# -*- coding: utf-8 -*-


import os
import shutil
import sys
from campus import campus_list as campi


dir_audit_path        = os.getenv('DIR_AUDIT')
spreadsheets_path     = os.path.join(dir_audit_path, 'presencial')
spreadsheets_ead_path = os.path.join(dir_audit_path, 'ead')


try:
    shutil.rmtree(spreadsheets_path)
except FileNotFoundError:
    pass
except NotADirectoryError:
    os.remove(spreadsheets_path)

os.mkdir(spreadsheets_path, mode=0o755)

for campus in campi:

    dir_campus_path = os.path.join(spreadsheets_path, campus)

    try:
        shutil.rmtree(dir_campus_path)
    except FileNotFoundError:
        pass
    except NotADirectoryError:
        os.remove(dir_campus_path)

    os.mkdir(dir_campus_path, mode=0o755)


try:
    shutil.rmtree(spreadsheets_ead_path)
except FileNotFoundError:
    pass
except NotADirectoryError:
    os.remove(spreadsheets_ead_path)

os.mkdir(spreadsheets_ead_path, mode=0o755)

for campus in campi:

    dir_campus_path = os.path.join(spreadsheets_ead_path, campus)

    try:
        shutil.rmtree(dir_campus_path)
    except FileNotFoundError:
        pass
    except NotADirectoryError:
        os.remove(dir_campus_path)

    os.mkdir(dir_campus_path, mode=0o755)


sys.exit(0)

