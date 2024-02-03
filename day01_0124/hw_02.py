# ------------------------------------------
# 임소영 _ 공공데이터 1일차 과제 2번
# ------------------------------------------

import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib
import pandas as pd

'''
- 인풋 3개 입력
- 그 월의 최고기온 평균값 게싼
- 그 월의 최저기온 평균값 계산
- 프린트 문 출력
- 그래프 표현 : 타이틀에 월 적용
'''

# 시작연도, 마지막연도, 측정할 달 입력받음 ========================================================
startyear = int(input('시작 연도 입력: '))
endyear = int(input('마지막 연도 입력: '))
mymonth = int(input('기온변화 측정할 달 입력: '))



# 파일을 읽어와서 날짜열의 데이터는 datetime으로 변경 ==============================================
weather_df = pd.read_csv('daegu-utf8-df.csv', encoding ='utf-8-sig')
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format = '%Y-%m-%d')


# 기간 동안의 최저기온 평균값 계산 ===============================================================

def calc3(list_name):
    for y in range(startyear, endyear + 1):
        data_df = weather_df[(weather_df['날짜'].dt.year == y)
                             & (weather_df['날짜'].dt.month == mymonth)]
        mydata = data_df['최저기온']

        avg = round(mydata.mean(), 1)          #그 달의 최저기온 평균값 게산
        list_name.append(avg)                  #평균값을 리스트에 담음

        '''
        에러발생
        if year_df['날짜'].dt.month == mymonth:
            data = year_df[year_df['날짜'].dt.month == mymonth]
            mylist.append(data[i])
        '''


lowlist = []       # 매년 그 달의 최저기온 평균값을 계산한 것을 담은 리스트

calc3(lowlist)

# 출력하기
print(f'{startyear}부터 {endyear}까지 {mymonth}월의 기온 변화')
print(f'{mymonth}월 최저기온 평균')

for idx in lowlist:
    print(idx, end = ' ')

print()




# 기간 동안의 최고기온 평균값 계산 ================================================================


def calc4(list_name):
    for y in range(startyear, endyear + 1):
        data_df = weather_df[(weather_df['날짜'].dt.year == y)
                             & (weather_df['날짜'].dt.month == mymonth)]
        mydata = data_df['최고기온']

        avg = round(mydata.mean(), 1)          #그 달의 최저기온 평균값 게산
        list_name.append(avg)                               #평균값을 리스트에 담음


highlist = []  # 매년 그 달의 최고기온 평균값을 계산한 것을 담은 리스트
calc4(highlist)

# 출력하기
print( )
print(f'{mymonth}월 최고기온 평균')
for idx in highlist:
    print(idx, end = ' ')


'''
에러뜬 코드
for year in range(startyear, endyear+1):
    mylist = []
    if weather_df['날짜'].dt.month == mymonth:
        data = weather_df[4]
        mylist.append(data)
    avg = round((sum(mylist)/len(mylist)),1)
    highlist.append(avg)
'''






# 그래프 그리기 ================================================================================
# - 마이너스 기호 출력 꺠짐 방지
# - 입력된 월을 이용하여 그래프의 타이틀 내용 변경
# - 최고 온도는 빨간색, 최저 온도는 파란색으로 표시, 각가 마커 및 legend 표시

listRange = list(range(startyear, endyear+1))

plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10,4))
plt.plot(listRange, lowlist, marker = 's', markersize =6, color = 'blue', label = '최저기온')
plt.plot(listRange, highlist, marker = 's', markersize =6, color = 'red', label = '최고기온')
plt.title(f"{startyear}년부터 {endyear}년까지 {mymonth}월의 기온 변화")
plt.legend()
plt.show()