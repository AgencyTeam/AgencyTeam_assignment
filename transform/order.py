import os
from transform.auth import login_required
from flask import Blueprint, render_template, request
from lib.order_transform import order2order

ORDER_FILE_PATH = os.path.dirname(os.path.realpath(
    __file__)) + '/static/files/발주파일.xlsx'
bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/', methods=['GET', 'POST'])
@login_required
def order():
    return render_template('order/order.html')


@bp.route('/complete', methods=['GET', 'POST'])
def order_complete():
    if request.method == 'POST':
        try:
            # form 데이터 받기
            file = request.files['file']
            form_data = request.form
            # 받은 데이터를 엑셀로 변환하여 저장하기
            order_df = order2order(file, form_data)
            order_df.to_excel(ORDER_FILE_PATH)

            return render_template('order/order_complete.html')
        except:
            return '파일 변환에 실패하였습니다. 다시 시도해주세요.'
