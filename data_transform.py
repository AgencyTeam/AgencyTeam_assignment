import pandas as pd

# 엑셀파일을 데이터프레임으로 변환
def excel2df(file_path, sheet_name=None):
    if sheet_name:
        try:
            df = pd.read_excel(file_path, sheet_name)
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

# 주문정보 파일의 주소부분을 발주서에 맞게 하기 위해 결합
def address_combine(df):
    fixed_address = [f"{a} {b} {c}" for a, b, c in zip(df["province"], df["city"], df["area"])]
    df = df.drop(["province", "city", "area"], axis=1)
    df["fixed address"] = fixed_address
    return df

# 주문정보 파일의 쓸모없는 column을 지움
def df_transform(df, need_columns):
    for column in df:
        if (column in need_columns):
            continue
        else:
            df = df.drop(column, axis=1)
    df = address_combine(df)
    return df

# 발주서에 필요한 정보를 담은 dict를 발주서파일 형태의 df로 정렬시킴
def sorted_order(dict, sorted_column):
    new_df = pd.DataFrame(dict)
    for column in sorted_column:
        if (column in new_df.columns):
            continue
        else:
            new_df[column] = ""
    new_df = new_df[sorted_column]
    return new_df

# 주문 df를 발주서 df로 변환
def generate_df(transformed_order_df, master_df, order_columns):
    order_dict = dict()

    for column in transformed_order_df.columns:
        data = transformed_order_df[column]
        #1
        if (column == "product model"):
            order_dict["상품코드"] = data
        #2
        elif (column == "vendor product No."):
            order_dict["사이즈코드"] = list(map(lambda x: x[-3:], data))
        #3
        elif (column == "product quantity"):
            order_dict["주문수량"] = data
        #4, 5
        elif (column == "order No."):
            order_dict["외부몰주문번호"] = data
            order_dict["주문 메모"] = data
        #6
        elif (column == "create time"):
            tmp = []
            for date in data:
                ymd = date.split(' ')
                tmp.append(ymd[0])
            order_dict["결제일시"] = tmp
        #7, 8
        elif (column == "customer name"):
            order_dict["주문자성명"], order_dict["수령자 이름"] = data, data
        #9, 10, 11, 12
        elif (column == "customer phone"):
            order_dict["주문자 전화번호"], order_dict["주문자 휴대폰"], order_dict["수령자 전화번호"], order_dict["수령자 휴대폰"] = data, data, data, data
        #13, 14
        elif (column == "fixed address"):
            order_dict["주문자 고정주소"], order_dict["수령자 고정주소"] = data, data
        #15, 16
        elif (column == "detailed address"):
            order_dict["주문자 상세주소"], order_dict["수령자 상세주소"] = data, data
        #17
        elif (column == "settle price"):
            data = list(map(int, data))
            order_dict["실판매가"] = list(map(lambda x: x/67*100, data))
    customer_price = []
    delivery_price = []
    for product_code in order_dict["상품코드"]:
        is_code = master_df["자체 상품코드"] == product_code
        value1 = list(master_df[is_code]["판매가"])
        value2 = list(master_df[is_code]["배송비"])
        customer_price.append(value1[0]) if value1 != [] else customer_price.append(0)
        delivery_price.append(value2[0]) if value2 != [] else delivery_price.append(0)
    #18
    order_dict["소비자가"] = customer_price
    #19
    order_dict["베송비"] = delivery_price
    #20
    order_dict["실판매가-배송비"] = [a - b for a, b in zip(order_dict["실판매가"], order_dict["베송비"])]
    #21
    order_dict["발주가"] = [b if a > b else a for a, b in zip(order_dict["실판매가-배송비"], order_dict["소비자가"])]
    #22
    order_dict["발주가(최종)"] = list(map(lambda x: x - x%10, map(int, order_dict["발주가"])))
    #23
    order_dict["총주문금액"] = order_dict["발주가(최종)"]

    return sorted_order(order_dict, order_columns)

# 주문파일을 발주서 df로 변환
def order2order(file_path):
    sheet_name = {'발주': '발주파일', '물류': '물류파일', '상품': 'commodity', '주문[영문]': 'secoo주문영문', '주문[중문]': 'secoo주문중문', '마스터': '마스타파일'}
    need_columns = ['product model', 'vendor product No.', 'product quantity', 'order No.', 'create time', 'customer name', 'customer phone', 'province', 'city', 'area', 'detailed address', 'settle price']

    order_form_df = excel2df(file_path, sheet_name=sheet_name['발주'])
    order_df = excel2df(file_path, sheet_name=sheet_name['주문[영문]'])
    master_df = excel2df(file_path, sheet_name=sheet_name['마스터'])
    order_columns = list(order_form_df.columns)

    transformed_order_df = df_transform(order_df, need_columns)
    return generate_df(transformed_order_df, master_df, order_columns)