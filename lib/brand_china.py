import pandas as pd
import os
from openpyxl import load_workbook

def excel2df(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except:
        print("엑셀파일을 불러오는데 실패했습니다.")
        return 0

def generate_df(brand_df):
    # 중국 서버 파일에만 있는 열, 빈칸 만들때 필요
    china_file_path = os.getcwd() + "/tmp/china.xlsx"
    # china = pd.read_excel(china_file_path)
    wb = load_workbook(filename=china_file_path)
    china = wb["INFORM"]
    china_columns = china['B6':'O6'].value
    print(china_columns)

    # 빈 데이터프레임 선언
    data = pd.DataFrame()

    #브랜드 파일
    brand = brand_df
    # 중국 서버용 형식에 맞게 변환 / 정확해보인것들 일부만 해봄.
    data["구분(품번)"] = brand["상품코드"]

    # 브랜드에서 한글로 제품명 제공한경우, 영문으로 바꿔야함
    # data["상품명(영문 or 중문)"] = brand["상품명"]
    data["정상 공급가(vat 포함)"] = brand["최초소비자가"]
    data["색상(영문)"] = brand["색상"]
    data["재고수량"] = brand["총재고수량"]
    data["원산지(제조국)(영문)"] = brand["원산지"] + "/Korea"
    data["세탁방법"] = brand["세탁방법"]
    data["소재"] = brand["소재"]
    


    # 정보가 없는 컬럼 빈칸 처리
    for column in china_columns:
        if (column in data.columns):
            continue
        else:
            data[column] = ""

    return data


def brand2china(file_path):
    brand_df = excel2df(file_path)

    china_df = generate_df(brand_df)
    return china_df
    
