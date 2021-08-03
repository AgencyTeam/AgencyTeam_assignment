import pandas as pd

# excel file -> df
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

# 주문정보 df 정제
def df_transform(order_df, master_df, need_columns):
    for column in order_df:
        if (column in need_columns):
            continue
        else:
            order_df = order_df.drop(column, axis=1)

    # 주소 combination
    fixed_address = [f"{a} {b} {c}" for a, b, c in zip(order_df["province"], order_df["city"], order_df["area"])]
    order_df = order_df.drop(["province", "city", "area"], axis=1)
    order_df["fixed address"] = fixed_address

    # 판매가, 배송비 column 생성
    customer_price = []
    delivery_price = []
    for product_code in order_df["product model"]:
        is_code = master_df["자체 상품코드"] == product_code
        value1 = list(master_df[is_code]["판매가"])
        value2 = list(master_df[is_code]["배송비"])
        customer_price.append(value1[0]) if value1 != [] else customer_price.append(0)
        delivery_price.append(value2[0]) if value2 != [] else delivery_price.append(0)
    order_df["소비자가"] = customer_price
    order_df["배송비"] = delivery_price

    return order_df


# 정제된 발주파일 df 생성
def generate_df(transformed_order_df, order_columns):
    order_dict = dict()

    for column in transformed_order_df.columns:
        data = transformed_order_df[column]
        if (column == "product model"):
            order_dict["상품코드"] = data
        elif (column == "vendor product No."):
            order_dict["사이즈코드"] = list(map(lambda x: x[-3:], data))
        elif (column == "product quantity"):
            order_dict["주문수량"] = data
        elif (column == "order No."):
            order_dict["외부몰주문번호"] = data
            order_dict["주문 메모"] = data
        elif (column == "create time"):
            tmp = []
            for date in data:
                ymd = date.split(' ')
                tmp.append(ymd[0])
            order_dict["결제일시"] = tmp
        elif (column == "customer name"):
            order_dict["주문자성명"], order_dict["수령자 이름"] = data, data
        elif (column == "customer phone"):
            order_dict["주문자 전화번호"], order_dict["주문자 휴대폰"], order_dict["수령자 전화번호"], order_dict["수령자 휴대폰"] = data, data, data, data
        elif (column == "fixed address"):
            order_dict["주문자 고정주소"], order_dict["수령자 고정주소"] = data, data
        elif (column == "detailed address"):
            order_dict["주문자 상세주소"], order_dict["수령자 상세주소"] = data, data
        elif (column == "settle price"):
            data = list(map(int, data))
            order_dict["실판매가"] = list(map(lambda x: x/67*100, data))
        elif (column == "소비자가"):
            order_dict["소비자가"] = data
        elif (column == "배송비"):
            order_dict["배송비"] = data
    order_dict["실판매가-배송비"] = [a - b for a, b in zip(order_dict["실판매가"], order_dict["배송비"])]
    order_dict["발주가"] = [b if a > b else a for a, b in zip(order_dict["실판매가-배송비"], order_dict["소비자가"])]
    order_dict["발주가(최종)"] = list(map(lambda x: x - x%10, map(int, order_dict["발주가"])))
    order_dict["총주문금액"] = order_dict["발주가(최종)"]

    # 만든 dict -> df로 변환
    new_df = pd.DataFrame(order_dict)
    
    # 얻지 못하는 값들은 빈 값 처리
    for column in order_columns:
        if (column in new_df.columns):
            continue
        else:
            new_df[column] = ""
    
    # 발주파일 column 순서대로 정렬
    new_df = new_df[order_columns]

    return new_df

def order2order(file_path):
    sheet_name = {'발주': '발주파일', '물류': '물류파일', '상품': 'commodity', '주문[영문]': 'secoo주문영문', '주문[중문]': 'secoo주문중문', '마스터': '마스타파일'}
    need_columns = ['product model', 'vendor product No.', 'product quantity', 'order No.', 'create time', 'customer name', 'customer phone',
    'province', 'city', 'area', 'detailed address', 'settle price']
    order_columns = ['상품코드', '사이즈코드', '주문수량', '외부몰주문번호', '총주문금액', '결제일시', '상점ID', '주문자성명', '주문자 전화번호',
    '주문자 휴대폰', '주문자 이메일', '주문자 우편번호', '주문자 고정주소', '주문자 상세주소', '수령자 이름', '수령자 전화번호', '수령자 휴대폰',
    '수령자 이메일', '수령자 우편번호', '수령자 고정주소', '수령자 상세주소', '주문 메모', '업체 코드', '외부몰 부주문 코드', '환율', 165, 
    'LF CJ운송장', 'SF EXPRESS 운송장', '소비자가', '실판매가', '배송비', '실판매가-배송비', '발주가', '발주가(최종)']

    order_df = excel2df(file_path, sheet_name=sheet_name['주문[영문]'])
    master_df = excel2df(file_path, sheet_name=sheet_name['마스터'])

    transformed_order_df = df_transform(order_df, master_df, need_columns)
    
    new_order_df = generate_df(transformed_order_df, order_columns)

    return new_order_df
