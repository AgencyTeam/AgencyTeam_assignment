import pandas as pd

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

def address_combine(df):
    fixed_address = [f"{a} {b} {c}" for a, b, c in zip(df["province"], df["city"], df["area"])]
    df = df.drop(["province", "city", "area"], axis=1)
    df["fixed address"] = fixed_address
    return df
    
def df_transform(df, need_columns):
    for column in df:
        if (column in need_columns):
            continue
        else:
            df = df.drop(column, axis=1)
    df = address_combine(df)
    return df

def generate_df(transformed_order_df, master_df, order_columns):
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
    customer_price = []
    delivery_price = []
    for product_code in order_dict["상품코드"]:
        is_code = master_df["자체 상품코드"] == product_code
        value1 = list(master_df[is_code]["판매가"])
        value2 = list(master_df[is_code]["배송비"])
        customer_price.append(value1[0]) if value1 != [] else customer_price.append(0)
        delivery_price.append(value2[0]) if value2 != [] else delivery_price.append(0)
    order_dict["소비자가"] = customer_price
    order_dict["베송비"] = delivery_price
    order_dict["실판매가-배송비"] = [a - b for a, b in zip(order_dict["실판매가"], order_dict["베송비"])]
    order_dict["발주가"] = [b if a > b else a for a, b in zip(order_dict["실판매가-배송비"], order_dict["소비자가"])]
    order_dict["발주가(최종)"] = list(map(lambda x: x - x%10, map(int, order_dict["발주가"])))
    order_dict["총주문금액"] = order_dict["발주가(최종)"]
    new_df = pd.DataFrame(order_dict)
    for column in order_columns:
        if (column in new_df.columns):
            continue
        else:
            new_df[column] = ""
    new_df = new_df[order_columns]
    return new_df

def order2order(file_path):
    sheet_name = {'발주': '발주파일', '물류': '물류파일', '상품': 'commodity', '주문[영문]': 'secoo주문영문', '주문[중문]': 'secoo주문중문', '마스터': '마스타파일'}
    need_columns = ['product model', 'vendor product No.', 'product quantity', 'order No.', 'create time', 'customer name', 'customer phone',
    'province', 'city', 'area', 'detailed address', 'settle price']

    order_form_df = excel2df(file_path, sheet_name=sheet_name['발주'])
    order_columns = list(order_form_df.columns)

    order_df = excel2df(file_path, sheet_name=sheet_name['주문[영문]'])
    master_df = excel2df(file_path, sheet_name=sheet_name['마스터'])

    transformed_order_df = df_transform(order_df, need_columns)
    new_order_df = generate_df(transformed_order_df, master_df, order_columns)
    return new_order_df
    
df = pd.DataFrame({'A':[1,2,3,4], 'B':[5,6,7,8], 'C':[9,10,11,12]})
is_A = df["B"] == 5
print(df)
a = list()
print(df[is_A]["A"][0])
a.append(list(df[is_A]["A"]))
print(a)