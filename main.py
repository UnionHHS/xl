import pandas as pd
import numpy as np

# trend_part1_ 점검결과 중 IoT 기기_ 분류_ 20220513.xlsx
excel = pd.read_excel("./xt/trend_part1_ 점검결과 중 IoT 기기_ 분류_ 20220513.xlsx", sheet_name=None)
excel_1 = pd.read_excel("./xt/IoT 기기_ 분류.xlsx",sheet_name=None)

tt = {}

partten = ['-','공유기','IP카메라','디지털복합기','PC','셋톱박스','스마트TV','안드로이드','인터넷전화','무선스피커']

pre_excel = excel['7.IoT기기식별']
pre_excel_1 = excel_1['reser_0516_user']

pre_excel = pre_excel.fillna('')
pre_excel_1 = pre_excel_1.fillna('')

excel_target1 = pre_excel.values
excel_target2 = pre_excel_1.values
# excel_target1 = excel['7.IoT기기식별'].values
# excel_target2 = excel_1['reser_0516_user'].values

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
            temp = []
            for l in partten:
                try:
                    if l in j[8]:
                        temp.append(l)
                except:
                    if j[8] == '':
                        pass
                    else:
                        temp.append('-')
            if len(temp) >= 2 and '-' in temp:
                temp.remove('-')
            elif temp == []:
                temp.append('-')
            j[7] = ', '.join(temp)
            j[3] = j[4].split('-')[1]
            tt[i[1]].append(list(j))

t = {"NO" : [], "점검 월" : [], "점검 일자" : [], "점검 시간" : [], "예약 번호" : [], "신청인" : [], "점검원" : [], "운영 체제" : [], "디바이스 종류" : [], "device 목록" : [],
 "iot 점검 결과1" : [], "iot 점검 결과2" : [], "iot 점검 결과3" : [], "iot 점검 결과4" : []}
# ind = 0
for i in tt.keys():
    # ind += 1
    for j in tt[i]:
        t['NO'].append(j[0])
        t['점검 월'].append(j[1])
        t['점검 일자'].append(j[2])
        t['점검 시간'].append(j[3])
        t['예약 번호'].append(j[4])
        t['신청인'].append(j[5])
        t['점검원'].append(i)
        t['운영 체제'].append(j[6])
        t['디바이스 종류'].append(j[7])
        t['device 목록'].append(j[8])
        t['iot 점검 결과1'].append(j[9])
        t['iot 점검 결과2'].append(j[10])
        t['iot 점검 결과3'].append(j[11])
        t['iot 점검 결과4'].append(j[12])
    # t["NO"] = [0]

data = pd.DataFrame(t)
data = data.set_index("NO")
data.to_excel("2201-2205_1Center_IoT_Check_Result.xlsx")

print(1)
