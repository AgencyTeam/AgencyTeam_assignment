import pandas as pd
from pandas import DataFrame

excel_path_En = input("영문주문서 위치를 입력해 주세요 : ")
sheet_En = int(input("영문주문서 시트 위치를 입력해 주세요.(시트가 하나라면 1) : "))


# excel_path = '/Users/mingyu/PycharmProjects/210727_+/(주문작업)LF알레그리 작업시트_0000 복사본.xlsx'

result_col = ['Shipment Reference No.','Receiver Contact Name','Receiver Tel','Receiver Address',
              'Receiver City','Receiver Province','Receiver Country/Region','Receiver Credentials Type',
              'Receiver Postal Code','Currency','Shipment Type','Add Service1','Add Service Account1',
              'Add Service Amount1','Add Service2','Add Service Account2','Add Service Amount2',
              'Total Package','Self Pickup','Payment Method','Account No.','Third Party District Code',
              'Tax payment']

# masterf = pd.read_excel(excel_path_, sheet_name=5)
# masterf = masterf.drop(index = 0)
sale_En = pd.read_excel(excel_path_En, sheet_name=sheet_En-1)
# sale_Ch = pd.read_excel(excel_path, sheet_name=4)
result = DataFrame(columns = result_col)
orderNo = DataFrame()
# print(sale_En.loc[0][1])

# sale_En에서 order No. 먼저 가져오기. -> result 에 저장.
orderNo['Shipment Reference No.'] = sale_En['order No.'].values
# 만약 result의 Shipment Reference No.와 sale_En 에서 order No. 가 같다면,
for i in range(len(orderNo['Shipment Reference No.'])):
    for k in range(len(sale_En['order No.'])):
        if orderNo.loc[i][0] == sale_En.loc[k][0]:
            result= result.append({'Shipment Reference No.' : str(sale_En.loc[k][0]),
                                    'Receiver Contact Name': sale_En.loc[k][4],
                                    'Receiver Tel' : str(sale_En.loc[k][5]),
                                    'Receiver Address' : sale_En.loc[k][9],
                                    'Receiver City' : sale_En.loc[k][7],
                                    'Receiver Province' : sale_En.loc[k][6],
                                    'Receiver Country/Region': 'China',
                                    'Receiver Credentials Type': str(sale_En.loc[k][30]),
                                    'Receiver Postal Code': sale_En.loc[k][25],
                                    'Currency': 'CNY',
                                    'Shipment Type': 'International Economy Express – Parcel',
                                    'Add Service1': None,
                                    'Add Service Account1': None,
                                    'Add Service Amount1': None,
                                    'Add Service2' : None,
                                    'Add Service Account2': None,
                                    'Add Service Amount2': None,
                                    'Total Package': '1',
                                    'Self Pickup': None,
                                    'Payment Method': 'Shipper'
                                   },
                                  sort=False, ignore_index = True)



print(result)

save_fname = '/Users/mingyu/Downloads/rrrrr.csv'
result.to_csv(save_fname, encoding='utf-8-sig')
#   Receiver Contact Name

# data_insert =[]



# result_col = pd.read_excel(excel_path, sheet_name=1, usecols=[1, 2])

# masterf = pd.read_excel('(주문작업)LF알레그리 작업시트_0000 복사본.xlsx', sheet_name = 5)