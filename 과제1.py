import pandas as pd
import json
from collections import OrderedDict
from numpyencoder import NumpyEncoder


path = "../source/Task1.xlsx"
task = pd.read_excel(path, sheet_name='물류')
task = task.fillna("")

data_list = []
column_list = task.columns.tolist()

for i in range(len(task)):
    data = OrderedDict()
    for j in range(len(column_list)):
        data[column_list[j]] = task.loc[i][j]
    data_list.append(data)

with open('task1.json', 'w') as make_file:
    json.dump(data_list, make_file,ensure_ascii=False, indent='\t', cls=NumpyEncoder)