import pandas as pd

def excel2df(file_path, sheet_name = None):
    if sheet_name:
        try:
            df = pd.read_excel(file_path, sheet_name)
            return df
        except:
            print("엑셀파일을 불러오는데 실패했습니다.")
            return 0

    try:
        df = pd.read_csv(file_path)
        return 0
    except:
        print("csv파일을 불러오는데 실패했습니다.")
        return 0

def address_combine(df):
    fixed_address = [f" {a} {b} {c}" for a, b, c in zip(df["province"], df["city"], df["area"])]
    df = df.drop(["province", "city", "area"], axis=1)
    df["fixed address"] = fixed_address
    return df

def df_transform(df,need_columns):
    for column in df:
        if (column in need_columns):
            continue
        else:
            df = df.drop(column, axis=1)
    df = address_combine(df)
    return df

def generate_df(transformed_order_df, order_columns):
    order_dict = dict()

    for column in transformed_order_df.columns:
        data = transformed_order_df[column]
        if (column == "order No."):
            order_dict["Shipment Reference No."] = data
        elif (column == "customer name"):
            order_dict["Receiver Contact Name"] = data
        elif (column == "customer phone"):
            order_dict["Receiver Tel"] = data
        elif (column == "detailed address"):
            order_dict["Receiver Address"] = data
        elif (column == "city"):
            order_dict["Receiver City"] = data
        elif (column == "province"):
            order_dict["Receiver Province"] = data
        elif (column == "certificates NO."):
            order_dict["Receiver Credentials No"] = data
        elif (column == "vendor remark"):
            order_dict["Receiver Postal Code"] = data

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
    need_columns = ['order No.', 'customer name', 'customer phone', 'detailed address', 'city', 'province', 'province', 'certificates NO.', 'vendor remark']

    order_form_df = excel2df(file_path, sheet_name=sheet_name['물류'])
    order_columns = list(order_form_df.columns)

    order_df = excel2df(file_path, sheet_name=sheet_name['주문[영문]'])

    transformed_order_df = df_transform(order_df, need_columns)
    new_order_df = generate_df(transformed_order_df, order_columns)
    return new_order_df

