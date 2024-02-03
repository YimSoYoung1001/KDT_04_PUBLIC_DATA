# ------------------------------------------
# 임소영 _ 공공데이터 1일차 과제 1번
# ------------------------------------------

import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib
import pandas as pd


# 그래프를 읽어옴 ---------------------------------------------------------------------------------------------------------
weather_df = pd.read_csv('daegu-utf8-df.csv', encoding ='utf-8-sig')
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format = '%Y-%m-%d')


# 일교차 계산 ------------------------------------------------------------------------------------------------------------
weather_df['일교차'] = weather_df['최고기온'] - weather_df['최저기온']


# 각 년도별로 일교차가 가장 큰 달 선정 ---------------------------------------------------------------------------------------
#diff_max = -99

total_diff = []
month_list = []


for y in range(2014, 2024):
    list_diff = []
    diff_max = -99
    month_max = 0
    for m in range(1, 13):
        data_df = weather_df[(weather_df['날짜'].dt.year == y)
                             & (weather_df['날짜'].dt.month == m)]
        mydata = data_df['일교차']
        avg = round(mydata.mean(), 1)  # 그 달의 일교차 평균값 계산
        list_diff.append(avg)         #각 달의 평균값을 리스트에 담음

        if avg > diff_max:
            diff_max = avg
            month_max = m


    month_list.append(f'{y}.{month_max}')

    max_month = max(list_diff)        # 각 달의 일교차 평균값 중 가장 큰 값을 지정함
    total_diff.append(max_month)

print(total_diff)
print(month_list)

plt.bar(month_list, total_diff)
plt.show()


'''
for y in range(2014, 2024):
    for m in range(1, 13):
        df = weather_df[(weather_df['날짜'].dt.year == y) & (weather_df['날짜'].dt.month == m)]
        diff = df['일교차'].mean() # 1
        list_diff()
'''

'''
# 이렇게 하면 y축 값은 나오지만 그에 해당하는 월은 나오지 않는다.

total_diff = []
month_list = []


for y in range(2014, 2024):
    list_diff = []
    for m in range(1, 13):
        data_df = weather_df[(weather_df['날짜'].dt.year == y)
                             & (weather_df['날짜'].dt.month == m)]
        mydata = data_df['일교차']

        avg = round(mydata.mean(), 1)          #그 달의 일교차 평균값 계산
        list_diff.append(avg)                  #각 달의 평균값을 리스트에 담음

    max_month = max(list_diff)        # 각 달의 일교차 평균값 중 가장 큰 값을 지정함
    total_diff.append(max_month)

print(total_diff)
'''

