from flask import Blueprint, render_template, request
import os
from lib.brand_domestic import brand2domestic
from lib.brand_SouthEastAsia import brand2SEA
from lib.brand_china import brand2china
from path import UPLOAD_DIR_PATH

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
            file_name = request.args.get('name', None)
            file_list = []

            if 'Domestic' in server_list:
                path_1 = f"{UPLOAD_DIR_PATH}/{file_name}국내서버업로드용.xlsx"
                brand2domestic(file,path_1)
                file_list.append(path_1)
            if 'SouthEastAsia' in server_list:
                path_2 = f"{UPLOAD_DIR_PATH}/{file_name}동남아서버업로드용.xlsx"
                brand2SEA(file,path_2)
                file_list.append(path_2)
            if 'China' in server_list:
                path_3 = f"{UPLOAD_DIR_PATH}/{file_name}중국(위챗)서버업로드용.xlsx"
                brand2china(file,path_3)
                file_list.append(path_3)
            

            return render_template('upload/upload_complete.html', server_list=server_list, file_list = file_list)
        except:
            return '파일 변환에 실패하였습니다. 다시 시도해주세요.'
