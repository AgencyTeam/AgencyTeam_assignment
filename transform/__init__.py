from flask import Flask
from .main import main
from .order import order

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main.bp)
    app.register_blueprint(order.bp)
    # app.register_blueprint(distribution.bp)
    # app.register_blueprint(upload.bp)

    return app