# -*- coding: utf-8 -*-


import os
import shutil
import sys
from campus import campus_list as campi


dir_base_path = os.getenv('DIR_BASE')


for campus in campi:

    dir_campus_path = os.path.join(dir_base_path, campus)

    try:
        shutil.rmtree(dir_campus_path)
    except FileNotFoundError:
        pass
    except NotADirectoryError:
        os.remove(dir_campus_path)

    os.mkdir(dir_campus_path, mode=0o755)


sys.exit(0)

