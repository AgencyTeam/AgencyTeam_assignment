import os
from pathlib import Path

ROOT_PATH = str(Path(os.path.realpath(__file__)).parent.parent)
ORDER_EXCEL_FORM = ROOT_PATH + '/transform/static/excel_form/발주form.xlsx'
UPLOAD_DIR_PATH = ROOT_PATH + '/upload_files'
