from flask import Blueprint

bp = Blueprint('distribution', __name__, url_prefix='/distribution')


@bp.route('/', methods=['GET', 'POST'])
def distribution():
    pass


@bp.route('/complete', methods=['GET', 'POST'])
def distribution_complete():
    pass
