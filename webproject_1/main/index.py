from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from flask import current_app as app
from order_transform import order2order
from Excel_to_Json import excel2json
from distribution_transform import distributon_from_orderinfo
import os

app = Flask(__name__)

upload_path = os.path.dirname(os.path.realpath(__file__)) + '\\static\\files\\upload_files\\'
gen_path = os.path.dirname(os.path.realpath(__file__)) + '\\static\\files\\gen_files\\'

# file_path에 있는 파일들 삭제하는 함수
def files_removing(file_path):
    file_list = os.listdir(file_path)
    if file_list == []:
        print(file_list, "삭제할 파일이 없습니다.")
        return 0
    else:
        for file in file_list:
            os.remove(file_path + file)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    return render_template('order.html')

@app.route('/order/complete', methods = ['GET', 'POST'])
def order_transform():
    if request.method == 'POST':
        # 경로에 파일이 있으면 그 파일들 삭제
        files_removing(upload_path)
        files_removing(gen_path)
        try:
            if request.method == 'POST':
                f = request.files['file']
                form_data = request.form
                upload_file = upload_path + secure_filename(f.filename)
                gen_file = gen_path + '발주파일.xlsx'
                f.save(upload_file)
                order2order(upload_file, form_data).to_excel(gen_file)
                # excel2json(gen_file, gen_path + "발주파일.json")

                return render_template('order_complete.html')
        except:
            return '파일 변환에 실패하였습니다. 다시 시도해주세요.'

@app.route('/distribution', methods = ['GET', 'POST'])
def distribution():
    pass

@app.route('/distribution/complete', methods = ['GET', 'POST'])
def distribution_transform():
    pass

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    pass

@app.route('/upload/complete', methods = ['GET', 'POST'])
def upload_transform():
    pass

# @app.route('/complete', methods = ['GET', 'POST'])
# def transform_file():
#     if request.method == 'POST':
#         files_removing(uploaded_file_path)
#         files_removing(gened_file_path)
#         try:
#             f = request.files['file']
#             upload_file_path = uploaded_file_path + secure_filename(f.filename)

#             gen_file_path_1 = gened_file_path + '발주파일.xlsx'
#             gen_file_path_2 = gened_file_path + '물류파일.xlsx'   # 물류파일 저장할 경로
#             f.save(upload_file_path)

#             order2order(upload_file_path).to_excel(gen_file_path_1)
#             distributon_from_orderinfo(upload_file_path).to_excel(gen_file_path_2)
            
#             excel2json(gen_file_path_1, gened_file_path + "발주파일.json")
#             excel2json(gen_file_path_2, gened_file_path + "물류파일.json")
            
#             return render_template('complete.html')
#         except:
#             return '파일 변환에 실패하였습니다. 다시 시도해주세요.'

if __name__ == "__main__":
    app.run()