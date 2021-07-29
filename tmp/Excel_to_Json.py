import pandas as pd
import json
from collections import OrderedDict
from numpyencoder import NumpyEncoder


path = os.getcwd()  + "/tmp/발주파일.xlsx"
data = pd.read_excel(path)
data = data.fillna("")

data_list = []
column_list = data.columns.tolist()

for i in range(len(data)):
    d = OrderedDict()
    for j in range(len(column_list)):
        d[column_list[j]] = data.iloc[i,j]
    data_list.append(d)

with open('발주파일.json', 'w') as make_file:
    json.dump(data_list, make_file,ensure_ascii=False, indent='\t', cls=NumpyEncoder)
