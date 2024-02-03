import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0
rate = 0

#pdf 2- 6페이지.
# for row in data :
#     for i in range(4, 8) :
#         row[i] = int(row[i]) # 4, 5, 6, 7 컬럼값을 정수로 변환
#     rate = row[4] / row[6] # [6]컬럼 값이 0인 행 확인 용도.
#     if rate > max_rate :
#         max_rate = rate
# print(max_rate)
# f.close()

# ▲ 위 for문은 에러 나야 정상임(ZeroDivisionError = 0으로 나눠서 생기는 Error 발생)

# 무임승차 인원이 0인 역 찾기.
# for row in data :
#     for i in range(4, 8) :
#         row[i] = int(row[i])
#     rate = row[4] / (row[4]+row[6])
#     if row[6] == 0 : # 무임승차 인원(row[6])이 없는 역 출력
#         print(row) # 디버깅 용도의 프린트문.(계산하는데 필요는 없지만 확인 용도.)
# print(max_rate)
# f.close()

# 최대 무임 승차 비율 확인
for row in data :
    for i in range(4, 8) :
        row[i] = int(row[i])
    if row[6] != 0 :
        #무임승차(%) = (무임 승차 수 * 100) / (유임 승차 수 + 무임 승차 수 )
        rate = (row[6] * 100) / (row[4]+row[6])
        if rate > max_rate :
            max_rate = rate
            print(row, round(rate, 2), '%')
f.close()
# 이것은 주석이다.