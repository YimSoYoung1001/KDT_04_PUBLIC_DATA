# ----------------------------------
# 임소영 2일차 과제 - 1번
# ----------------------------------

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

'''
분해
1) 파일 읽음
2) 한 호선을 기준으로 최대 하차역 및 하차인원 계산
   - 시간대는 고정, 호선도 고정
   - 먼저 시간대 2개를 합친 데이터 프레임을 생성함
   - 아무값이나 정해놓고 업데이트 하는 방식으로 짜기
   - 최대값이라고 업데이트 되면 역이랑 그 인원으로 각각 업데이트
   - 그거에 대한 함수를 만들어서 각 호선별로 적용
3) 최종 결과를 프린트문 (콤마 적용)
    - 이때 그래프에 그릴 수 있게 리스트에 담아둠
4) 모든 호선에 적용하도록 for 문
5) 그래프 그리기 
'''


# 각 노선별 최대 하차 인원을 print -----------------------------------------------------------------------------------
def func(num_name):
    with open('subwaytime.csv', encoding='utf-8-sig') as f:
        subway = csv.reader(f)
        next(subway)
        next(subway)

        df_list = []  # 1개의 호선 안에서의 지정시간내 하차인원의 총합을 답은 리스트
        people_max = 0  # 하차인원의 최대값
        station_max = ''  # 하차인원의 최대값의 역

        for row in subway:

            num = num_name

            if row[1] == num:
                df = int(row[11]) + int(row[13])
                df_list.append(df)
                if df > people_max:
                    people_max = df
                    station_max = row[3]

        print(f"출근 시간대 {num} 최대 하차역: {station_max}역, 하차인원: {people_max:,}명")
        x_data.append(num + ' ' + station_max)
        y_data.append(people_max)

x_data = []
y_data = []

func('1호선')
func('2호선')
func('3호선')
func('4호선')
func('5호선')
func('6호선')
func('7호선')

#print(x_data)
#print(y_data)

# 막대 그래프를 표시 -----------------------------------------------------------------------------------

plt.bar(x_data, y_data)
plt.xticks(rotation = 45)
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.show()
















'''
# 이 코드로 하면 분해 과정에서 3)번 단계까지 한거에 해당함 ---------------------------------------------------------------------
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    subway = csv.reader(f)
    next(subway)
    next(subway)

    df_list = []  # 1개의 호선 안에서의 지정시간내 하차인원의 총합을 답은 리스트
    people_max = 0  # 하차인원의 최대값
    station_max = ''  # 하차인원의 최대값의 역

    for row in subway:

        num = num_name

        if row[1] == num:
            df = int(row[11]) + int(row[13])
            df_list.append(df)
            if df > people_max:
                people_max = df
                station_max = row[3]

    print(f"출근 시간대 {num} 최대 하차역: {station_max}역, 하차인원: {people_max:,}명")

'''

'''
# 이렇게 하면 계속 초기값으로 해서 결과가 나온다.
with open('subwaytime.csv', encoding = 'utf-8-sig') as f:
    subway = csv.reader(f)
    next(subway)
    next(subway)

    for row in subway:
        #for num in ['1호선' , '2호선' , '3호선' ,'4호선' ,'5호선' , '6호선', '7호선']:
        for num in ['1호선']:
            df_list = []  # 1개의 호선 안에서의 지정시간내 하차인원의 총합을 답은 리스트
            people_max = 0  # 하차인원의 최대값
            station_max = ''  # 하차인원의 최대값의 역
            if row[1] == num:
                df = int(row[11]) + int(row[13])
                df_list.append(df)
                if df > people_max:
                    people_max = df
                    station_max = row[3]

            print(f"출근 시간대 {num} 최대 하차역: {station_max}역, 하차인원: {people_max:,}명")

'''
