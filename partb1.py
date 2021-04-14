import os
import re
import pandas as pd
root_book = []
title_list = []
id_list = []
for r,dirs,files in os.walk('cricket'):
    for file in files:
        f = os.path.join(r,file)
        root_book.append(f)
for root in root_book:
    txt = open(root).read()
    first_line = open(root).readline()
    if re.findall(r'[A-Z]{4}-\d{3}[A-Z]', txt):
        title_list.append(first_line)
        id_list.append(re.findall(r'[A-Z]{4}-\d{3}[A-Z]', txt)[0])
data = {'filename': title_list, 'documentID': id_list}
dataframe = pd.DataFrame(data)
dataframe.to_csv('partb1.csv')
