from flask import Blueprint

bp = Blueprint('upload', __name__, '/upload')

@bp.route('/', methods = ['GET', 'POST'])
def upload():
    pass

@bp.route('/complete', methods = ['GET', 'POST'])
def upload_complete():
    pass