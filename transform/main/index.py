from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask import current_app as app
from data_transform import order2order
import os

app = Flask(__name__)
uploaded_file_path = os.getcwd() + "/transform/main/static/uploads/"
gened_file_path = os.getcwd() + "/transform/main/static/gen_files/"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/complete', methods = ['GET', 'POST'])
def transform_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            upload_file_path = uploaded_file_path + secure_filename(f.filename)
            gen_file_path = gened_file_path + 'complete.xlsx'
            f.save(upload_file_path)
            order2order(upload_file_path).to_excel(gen_file_path)
            return render_template('complete.html')
        except:
            return '파일 변환에 실패하였습니다. 다시 시도해주세요.'

if __name__ == "__main__":
    app.run()