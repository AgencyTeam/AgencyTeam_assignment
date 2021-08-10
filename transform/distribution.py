from flask import Blueprint, render_template, request
from transform.auth import login_required
from lib.distribution_transform import distribution_from_orderinfo


bp = Blueprint('distribution', __name__, url_prefix='/distribution')

@bp.route('/', methods = ['GET', 'POST'])
@login_required
def distribution():
    return render_template('distribution/distribution.html')

@bp.route('/complete', methods = ['GET', 'POST'])
def distribution_complete():
    if request.method == 'POST':
        try:
            # form 데이터받기
            file = request.files['file']
            form_data = request.form
            #받은 데이터를 엑셀로 변환하여 저장하기
            distribution_from_orderinfo(file, form_data)
            
            return render_template('distribution/distribution_complete.html')
        except:
            return '파일 변환에 실패하였습니다. 다시 시도해주세요'