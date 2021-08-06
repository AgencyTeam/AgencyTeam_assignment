# from AgencyTeam_assignment_1.tmp.data_transform import df_transform
import pandas as pd

##주문정보->물류파일 변환
#파일 불러오기
def order_info(file_path, sheet_name = None):
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

def distribution_df(order_info_df):
    New_distribution_df = pd.DataFrame({'Shipment Reference No.': order_info_df["order No."],
                                    'Shipment Reference No.2' : order_info_df["order No."],
                                    'Customer Account No.' : " ",
                                    'Company Name' : "LF corp",
                                    'Contact Name' : "Jiyeon song",
                                    'Tel' : "821033117252",
                                    'Address' : "Room 1319, Mirabell tower 13F, 362-2, Yeongcheon-dong",
                                    'City' : "Hwaseong-si",
                                    'Province': "Gyeonggi-do",
                                    'Country/Region' : "Korea",
                                    'Email':" ",
                                    'Postal Code':"18469", #공백, 복붙 임의로 기입
                                    'Receiver Contact Name': order_info_df["customer name"],
                                    'Receiver Chinese Name': '',
                                    'Receiver Tel': order_info_df["customer phone"],
                                    'Receiver Address': order_info_df["detailed address"],
                                    'Receiver Province': order_info_df["province"],
                                    'Receiver Email': '',
                                    'Receiver Country/Region': 'China',
                                    'Receiver Credentials Type': 'ID',
                                    'Receiver Credentials No': order_info_df["certificates NO."],
                                    'Receiver Postal Code': order_info_df["vendor remark"],
                                    'Currency': 'CNY',
                                    'Shipment Type': 'International Economy Express – Parcel',
                                    'Add Service 1': '',
                                    'Add Service Account1': '',
                                    'Add Service Amount1': '',
                                    'Add Service2': '',
                                    'Add Service Account2': '',
                                    'Add Service Amount2': '',
                                    'Total Package': '1',
                                    'Self Pickup': '',
                                    'Payment Method': 'Shipper',
                                    'Account No.': '0825004317',
                                    'Third Party District Code': '',
                                    'Tax payment': 'Shipper',
                                    '(PCS)1': '',
                                    '(L)1': '',
                                    '(W)1': '',
                                    '(H)1': '',
                                    'Term of Trade': '',
                                    'Reason for Sending 1': '',
                                    'Reason for Sending 2': '',
                                    'Remarks': '',
                                    'AWB Remarks': '',
                                    'Tax Account': '',
                                    'Add Service3': '',
                                    'VAT': '',
                                    'EORI': '',
                                    'Traceability label': '',
                                    'PO Number': '',
                                    "Shipper's Tax ID No.": '',
                                    'Appointment Time': '',
                                    'Personal baggage': '',
                                    'Importer Company Name': '',
                                    'Importer Tel No.': '',
                                    'Importer Address': '',
                                    'Customs Clearance': '',
                                    'Shipper County': '',
                                    'Receiver County': '',
                                    'Shipper Credentials Type': '',
                                    'Shipper Credentials No.': '',
                                    'Notify to pick up': 'NO',
                                    'Formal Customs Declaration For import': ''
                                    })
    return New_distribution_df

def distributon_from_orderinfo(file_path):
    order_info_df = order_info(file_path, sheet_name = "secoo주문영문")
    New_distribution_df = distribution_df(order_info_df)

    return New_distribution_df