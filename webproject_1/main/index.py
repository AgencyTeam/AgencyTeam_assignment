from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask import current_app as app
from order_transform import order2order
import os

app = Flask(__name__)
uploaded_file_path = os.getcwd() + "/webproject_1/main/static/uploads/"
gened_file_path = os.getcwd() + "/webproject_1/main/static/gen_files/"

def files_removing(file_path):
    file_list = os.listdir(file_path)
    if file_list == []:
        print(file_list, "삭제할 파일이 없습니다.")
        return 0
    else:
        for file in file_list:
            os.remove(file_path + file)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/complete', methods = ['GET', 'POST'])
def transform_file():
    if request.method == 'POST':
        files_removing(uploaded_file_path)
        files_removing(gened_file_path)
        try:
            f = request.files['file']
            upload_file_path = uploaded_file_path + secure_filename(f.filename)

            gen_file_path_1 = gened_file_path + '발주파일.xlsx'
            # gen_file_path_2 = gened_file_path + '물류파일.xlsx'
            
            f.save(upload_file_path)

            order2order(upload_file_path).to_excel(gen_file_path_1)
            # order2dist(upload_file_path).to_excel(gen_file_path_2)
            
            return render_template('complete.html')
        except:
            return '파일 변환에 실패하였습니다. 다시 시도해주세요.'

if __name__ == "__main__":
    app.run()