# ----------------------------------------------
# 임소영 3일차 과제 - 2번 (마방진)
# ----------------------------------------------


def mabangzine(num):
    n = num

    # 0으로 채워진 2차원 리스트 생성 ================================================================================
    first_list = [[0 for col in range(n)] for row in range(n)]

    r = 0
    c = 0

    # x는 시작 위치의 열을 설정함 ==================================================================================
    x = n//2
    c = x
    first_list[r][c] = 1

    # 규칙에 따라 값을 채워나감 ====================================================================================
    for i in range(2, n*n+1):
        #행 변경 (y축) : r2는 변경할 행의 인덱스 번호를 말함
        if 0 <= r - 1 <= (n-1) :
            r2 = r-1
        else:
            r2 = r -1 + n

        #열 변경(x축) : c2는 변경할 열의 인덱스 번호를 말함
        if 0 <= c+1 <= (n-1):
            c2 = c+1
        else:
            c2 = 0

        # 이미 값이 있는 경우
        if first_list[r2][c2] != 0:
            r2 = r + 1
            c2 = c

        # 마방진 배열에 값 추가함
        r = r2
        c = c2
        first_list[r][c] = i

        #print(f'중간 점검{i}')
        #for k in range(n):
            #print(first_list[k])

    # 결과물 확인 ================================================================================================
    print(f"Magic Square ({n}x{n})")
    for k in range(n):
        for j in range(n):
            print(first_list[k][j], end = ' ')
        print()


while True:
    num = int(input('홀수차 배열의 크기를 입력하세요: '))
    if num % 2 == 0 :
        print('짝수를 입력함. 재입력하기')
    else:
        mabangzine(num)
        break









# ----------------------------------------------------------------------------------------------------------------------




'''
# 5로 했더니 적용이 불가능. 쓸수없는 코드. 
n = 5
first_list = [[0 for col in range(n)] for row in range(n)]
print('시작 전')
for k in range(5):
    print(first_list[k])


r = 0
c = 0

#x는 시작 위치의 열을 설정함
x = n//2
c = x

# 1~n 채우기 ---------------------------------------------------------------
first_list[r][c] = 1

for i in range(2, n+1):
    #행 변경 (y축)
    if 0 <= r - 1 <= (n-1) :
        r = r-1
    else:
        r = r -1 + n

    #열 변경(x축)
    if 0 <= c+1 <= (n-1):
        c = c+1
    else:
        c = 0
    first_list[r][c] = i

print(f"{n}까지 확인")
for k in range(5):
    print(first_list[k])


# n+1 ~ n*2 채우기 ---------------------------------------------------------
r = r + 1
first_list[r][c] = n+1

print(f"{n+1}까지 확인")
for k in range(5):
    print(first_list[k])


for i in range(n+2, n*2 + 1):
    r = r - 1
    c = (n-1) - r
    first_list[r][c] = i

print(f"{n*2}까지 확인")
for k in range(5):
    print(first_list[k])


# n*2 ~ n*n 채우기 ---------------------------------------------------------
r = r + 1
first_list[r][c] = n * 2 + 1
for i in range(n*2 + 1 , n*n +1):
    #행 변경 (y축)
    if 0 <= r - 1 <= (n-1) :
        r = r-1
    else:
        r = r -1 + n

    #열 변경(x축)
    if 0 <= c+1 <= (n-1):
        c = c+1
    else:
        c = 0
    first_list[r][c] = i


#결과물 확인
for k in range(5):
    print(first_list[k])
'''




'''
n = 3
first_list = [[0 for col in range(n)] for row in range(n)]
print(f"시작 전  => {first_list}\n")

r = 0
c = 0

#x는 시작 위치의 열을 설정함
x = n//2
c = x

# 1~3 채우기
first_list[r][c] = 1
print(f"   1번  => {first_list}")

for i in range(2,4):
    #행 변경 (y축)
    if 0 <= r - 1 <= 2 :
        r = r-1
    else:
        r = r -1 + 3

    #열 변경(x축)
    if 0 <= c+1 <= 2:
        c = c+1
    else:
        c = 0
    first_list[r][c] = i
    print(f"   {i}번  => {first_list}")



# 4~6 채우기
print(r, c)
r = r + 1
first_list[r][c] = 4
print(f"   4번  => {first_list}")

for i in range(5,7):
    r = r - 1
    c = (n-1) - r
    first_list[r][c] = i
    print(f"   {i}번  => {first_list}")



# 7~9 채우기
print(r,c)
r = r + 1
first_list[r][c] = 7
for i in range(8,10):
    #행 변경 (y축)
    if 0 <= r - 1 <= 2 :
        r = r-1
    else:
        r = r -1 + 3

    #열 변경(x축)
    if 0 <= c+1 <= 2:
        c = c+1
    else:
        c = 0
    first_list[r][c] = i
    print(f"   {i}번  => {first_list}")
    
'''

'''
# 1~3의 숫자까지는 정상입력 가능. 하지만 이미 값이 있는 경우에 그 위치의 값이 변경됨.
n = 3
first_list = [[0 for col in range(n)] for row in range(n)]
print(f"시작 전  => {first_list}\n")

r = 0
c = 0

#x는 시작 위치의 열을 설정함
x = n//2
c = x

for i in range(1, 10):

    first_list[r][c] = i

    #행 변경 (y축)
    if 0 <= r - 1 <= 2:
        r = r-1
    else:
        r = r -1 + 3

    #열 변경(x축)
    if 0 <= c+1 <= 2:
        c = c+1
    else:
        c = 0


    print(f"   {i}번  => {first_list}")

#print(first_list)


test = [[1,2],[3,4]]
if 3 in test:
    print('True')
else:
    print('False')

for i in range(2):
    if 3 in test[i]:
        print('True')
    else:
        print('False')
'''




'''
#first_list = [[0, 0, 0],
#              [0, 0, 0],
#              [0, 0, 0]]

x=0

#1
first_list[x][center] = 1

#2
if x-1 < 0:
    first_list[x-1 + 3][center+1] = 2
else:
    first_list[x-1][center+1] = 2

print(first_list)

#3
if x-1 + 3 -1 < 0:
    first_list[x-1 + 3 - 1][center+1 -3] = 3
else:
    first_list[x-1 + 3 - 1][center+1 +1] = 3
print(first_list)
'''