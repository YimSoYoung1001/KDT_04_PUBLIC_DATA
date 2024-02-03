# ----------------------------------
# 임소영 2일차 과제 - 2번
# ----------------------------------

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd

sDict = {}

'''
이렇게도 가능함
f = open('subwaytime.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
next(data)
'''

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    subway = csv.reader(f)
    next(subway)
    next(subway)

    for row in subway:
        # 지하철역 뽑음
        keydata = row[3]
        # 하차인원 뽑음
        data = int(row[35]) + int(row[37])

        if keydata in sDict:
            sDict[keydata] = sDict[keydata] + data
        else:
            sDict[keydata] = data

    print(sDict)
    sDict = sorted(sDict.items(), key =(lambda x: x[1]), reverse = True)
    print(sDict)


top5_dict = sDict[:5]
print(top5_dict)

xList = []
yList = []

for t in top5_dict:
    xList.append(t[0])
    yList.append(t[1])

plt.bar(xList, yList)
plt.show()
plt.title('서울 지하철 퇴근 시간대 하차 인원 비교')











'''
#이르케 하면 동일한 이름의 열을 고려할 수 없음

sDict = {}
maxpeople = 0 # 키에 대한 값은 리스트 형식으로 담을 예정


with open('subwaytime.csv', encoding='utf-8-sig') as f:
    subway = csv.reader(f)
    next(subway)
    next(subway)

    for row in subway:
        keydata = row[3]                           # 지하철역 뽑음
        data = int(row[35]) + int(row[37])         # 하차인원 뽑음
        if data > maxpeople:
            sDict[keydata] = data
    print(sDict)
'''