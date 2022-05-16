import pandas as pd
import numpy as np

# trend_part1_ 점검결과 중 IoT 기기_ 분류_ 20220513.xlsx
excel = pd.read_excel("./xt/trend_part1_ 점검결과 중 IoT 기기_ 분류_ 20220513.xlsx", sheet_name=None)
excel_1 = pd.read_excel("./xt/IoT 기기_ 분류.xlsx",sheet_name=None)

tt = {}

excel_target1 = excel['7.IoT기기식별'].values
excel_target2 = excel_1['reser_0516_user'].values

for i in excel_target2:
    if 'T1' in i[1] or 'T2' in i[1] or 'T3' in i[1]:
        if i[1] in tt.keys():
            pass
        else:
            tt[i[1]] = []
    else:
        continue
    for j in excel_target1:
        if i[2] == j[4]:
            tt[i[1]].append(list(j))

print(1)
