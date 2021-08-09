from flask import Blueprint, render_template, request
import os
from lib.brand_domestic import brand2domestic
from lib.brand_SouthEastAsia import brand2SEA

UPLOAD_FILE_PATH = os.path.dirname(
    os.path.realpath(__file__)) + '/static/files/'
bp = Blueprint('upload', __name__, url_prefix='/upload')


@bp.route('/', methods=['GET', 'POST'])
def upload():
    return render_template('upload/upload.html')


@bp.route('/complete', methods=['GET', 'POST'])
def upload_complete():
    if request.method == 'POST':
        try:
            # form 데이터 받기 / 파일, 서버선택리스트
            file = request.files['file']
            server_list = request.form.getlist('server')

            if 'Domestic' in server_list:
                path_1 = UPLOAD_FILE_PATH + '국내서버업로드용.xlsx'
                brand2domestic(file).to_excel(path_1)
            if 'SouthEastAsia' in server_list:
                path_2 = UPLOAD_FILE_PATH + '동남아서버업로드용.xlsx'
                brand2SEA(file).to_excel(path_2)
            if 'China' in server_list:
                path_3 = UPLOAD_FILE_PATH + '중국(위챗)서버업로드용.xlsx'
                brand2domestic(file).to_excel(path_3)

            return render_template('upload/upload_complete.html', server_list=server_list)
        except:
            return '파일 변환에 실패하였습니다. 다시 시도해주세요.'
