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
    # 국내 서버 파일에만 있는 열, 빈칸 만들때 필요
    domestic_file_path = os.getcwd() + "/lib/domestic.xlsx"
    domestic = pd.read_excel(domestic_file_path)

    # 빈 데이터프레임 선언
    data = pd.DataFrame()

    #브랜드 파일
    brand = brand_df
    # 국내 서버용 형식에 맞게 변환 / 정확해보인것들 일부만 해봄.
    data["상품명"] = brand["상품명"].str[0:100]
    data["자체 상품코드"] = brand["상품코드"].str[0:50]
    data["판매상태"] = brand["판매가능 총수량"].apply(lambda x : "판매중" if x>0 else "품절")
    data["판매가"] = brand["최초소비자가"]
    data["무게"] = brand["무게"]
    data["상품 상세정보"] = brand["상품고시정보_HTML"]
    # data["미성년자 구매"] = "Y"
    data["원산지"] = brand["원산지"]
    data["제조사"] = brand["제조원"].str.strip()
    data["브랜드"] = brand["브랜드"].str.strip()


    # 정보가 없는 컬럼 빈칸 처리
    for column in domestic.columns:
        if (column in data.columns):
            continue
        else:
            data[column] = ""

    return data


def brand2domestic(file_path):
    brand_df = excel2df(file_path)
    domestic_df = generate_df(brand_df)
    return domestic_df
    

