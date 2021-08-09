import pandas as pd
import os

def excel2df(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except:
        print("엑셀파일을 불러오는데 실패했습니다.")
        return 0
    try:
        df = pd.read_csv(file_path)
        return df
    except:
        print("csv파일을 불러오는데 실패했습니다.")
        return 0

def generate_df(brand_df):
    # 동남아 서버 파일에만 있는 열, 빈칸 만들때 필요
    sea_file_path = os.getcwd() + "/tmp/SouthEastAsia.xlsx"
    sea = pd.read_excel(sea_file_path, sheet_name="Template")

    # 빈 데이터프레임 선언
    data = pd.DataFrame()

    #브랜드 파일
    brand = brand_df
    # 동남아 서버용 형식에 맞게 변환 / 정확해보인것들 일부만 해봄.
    data["Product Name"] = brand["상품명"].str[0:255]
    # data["Product Description"] = brand[""]
    data["Maximum Purchase Quantity"] = brand["판매가능 총수량"]
    data["Price"] = brand["최초소비자가"]
    data["Stock"] = brand["총재고수량"]
    data["Weight"] = brand["무게"]
    # data["미성년자 구매"] = "Y"

    # 정보가 없는 컬럼 빈칸 처리
    for column in sea.columns:
        if (column in data.columns):
            continue
        else:
            data[column] = ""

    return data


def brand2SEA(file_path):
    brand_df = excel2df(file_path)
    sea_df = generate_df(brand_df)
    return sea_df
    

