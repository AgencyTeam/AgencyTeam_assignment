from transform.auth import login_required
from flask import Blueprint, render_template, request
from lib.order_transform import make_excel
from .path import UPLOAD_DIR_PATH, ROOT_PATH
import datetime as dt
import json

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/', methods=['GET', 'POST'])
@login_required
def order():
    with open(ROOT_PATH + "/transform/default_json/order.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
        return render_template('order/order.html', data=data)


@bp.route('/complete', methods=['GET', 'POST'])
def order_complete():
    if request.method == 'POST':

        # 파일 이름 생성
        x = dt.datetime.now()
        file_name = f"{x.year}{x.month}{x.day}{x.hour}{x.minute}{x.second}{x.microsecond}"

        # form 데이터 받기
        file = request.files['file']
        form_data = request.form
        upload_path = f"{UPLOAD_DIR_PATH}/{file_name}.xlsx"

        # 받은 데이터를 엑셀로 변환하여 저장하기
        make_excel(file, form_data, upload_path)

        return render_template('order/order_complete.html', filename=f"{file_name}.xlsx")


@bp.route('/default_update', methods=['GET', 'POST'])
def order_default_update():
    if request.method == 'GET':
        with open(ROOT_PATH + "/transform/default_json/order.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            return render_template('order/order_default.html', data=data)

    elif request.method == 'POST':
        form_data = request.form
        info = dict()

        for key in form_data:
            info[key] = form_data[key]

        with open(ROOT_PATH + "/transform/default_json/order.json", 'w', encoding='utf-8') as f:
            try:
                json.dump(info, f, ensure_ascii=False, indent='\t')
                success = True
            except:
                print("json 쓰기 실패")
            return render_template('order/order_default.html', data=info, success=success)
