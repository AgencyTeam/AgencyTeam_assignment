from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from flask import current_app as app
from order_transform import order2order
from Excel_to_Json import excel2json
from distribution_transform import distributon_from_orderinfo
import os

#파일경로 /AgencyTeam_assignment_1 추가함
app = Flask(__name__)
uploaded_file_path = os.getcwd() + "/webproject_1/main/static/uploads/"
gened_file_path = os.getcwd() + "/webproject_1/main/static/gen_files/"
print(os.getcwd())
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
def index():
    print("index")
    return render_template('index.html')

@app.route('/complete', methods = ['GET', 'POST'])
def transform_file():
    print("trans 시작")
    if request.method == 'POST':
        files_removing(uploaded_file_path)
        files_removing(gened_file_path)
        try:
            print("try")
            f = request.files['file']
            upload_file_path = uploaded_file_path + secure_filename(f.filename)
            print(upload_file_path)
            gen_file_path_1 = gened_file_path + '발주파일.xlsx'
            gen_file_path_2 = gened_file_path + '물류파일.xlsx'   # 물류파일 저장할 경로
            print(gen_file_path_2)
            f.save(upload_file_path)

            order2order(upload_file_path).to_excel(gen_file_path_1)
            print("order 완료")
            distributon_from_orderinfo(upload_file_path).to_excel(gen_file_path_2)
            print("dist 완료")
            excel2json(gen_file_path_1, gened_file_path + "발주파일.json")
            excel2json(gen_file_path_2, gened_file_path + "물류파일.json")
            
            return render_template('complete.html')
        except:
            return '파일 변환에 실패하였습니다. 다시 시도해주세요.'

if __name__ == "__main__":
    app.run()