# ----------------------------------------------
# 임소영 3일차 과제 - 1번
# ----------------------------------------------
'''
분해
(1) 데이터를 읽어옴
(2) 대구광역시 내 데이터를 처리함
    - 먼저 대구광역시 전체에만 뽑는다고 생각하고 코드를 짠다.
    - 그 다음 이거를 for 문을 돌린다. (각 구군별로 돌리게끔)
(3) subplot으로 그래프 구현한다.
'''

import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f = open('gender.csv', encoding = 'utf-8-sig')
data = csv.reader(f)

city_list = ['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구',
        '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', '대구광역시 달서구',
        '대구광역시 달성군']

graph_list = []

for city in city_list:

     for i in range(1, 10):
          for row in data:
               daegulist = []
               # 행정구역 1개에 대한 남성, 여성 인구수를 뽑는다.
               if city in row[0]:
                    male_num = int(row[104].replace(',', ''))
                    female_num = int(row[207].replace(',', ''))
                    print(male_num, female_num)
                    daegulist.append(male_num)
                    daegulist.append(female_num)

                    # 그래프 그린다.
                    plt.subplot(3, 3, i)
                    label = ['남성', '여성']
                    plt.pie(daegulist, labels=label, autopct='%1.1f%%', startangle=90)
                    cityname = city_list[i-1]
                    plt.title(cityname)
                    plt.suptitle('대구광역시 구별 남녀 인구 비율')
                    break

plt.show()






#-----------------------------------------------------------------------------------------------------------------------

'''
f = open('gender.csv', encoding='utf-8-sig')
data = csv.reader(f)

city_list = ['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구',
             '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', '대구광역시 달서구',
             '대구광역시 달성군']

graph_list = []

for city in city_list:
     for k in range(2):
          for i in range(2):
               for row in data:
                    daegulist = []
                    # 행정구역 1개에 대한 남성, 여성 인구수를 뽑는다.
                    if city in row[0]:
                         male_num = int(row[104].replace(',', ''))
                         female_num = int(row[207].replace(',', ''))
                         print(male_num, female_num)
                         daegulist.append(male_num)
                         daegulist.append(female_num)

                         # 그래프 그린다.
                         plt.subplot2grid((3,3), (k,i))
                         plt.figure(10, 5)
                         label = ['남성', '여성']
                         plt.pie(daegulist, labels=label, autopct='%1.1f%%', startangle=90)
                         plt.title(city)
                         break

plt.show()
'''

#-----------------------------------------------------------------------------------------------------------------------

'''
# 모든 행정구역의 그래프까지 그려진다. 이걸 subplot 해본다.
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f = open('gender.csv', encoding = 'utf-8-sig')
data = csv.reader(f)

city_list = ['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구',
        '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', '대구광역시 달서구',
        '대구광역시 달성군']

for city in city_list:
     for row in data:
          daegulist = []
          # 행정구역 1개에 대한 남성, 여성 인구수를 뽑는다.
          if city in row[0]:
               male_num = int(row[104].replace(',', ''))
               female_num = int(row[207].replace(',', ''))
               print(male_num, female_num)
               daegulist.append(male_num)
               daegulist.append(female_num)
               # 그래프 그린다.
               label = ['남성', '여성']
               plt.pie(daegulist, labels=label, autopct='%1.1f%%', startangle=90)
               plt.title(city)
               plt.savefig('hw_img/' + city + '.png', dpi=100)
               plt.close()

               break

'''

#-----------------------------------------------------------------------------------------------------------------------

'''
# 대구광역시 전체만 대상으로 했을 때의 결과가 나온다. 이걸 전체 행정구역별로 돌려본다.

f = open('gender.csv', encoding = 'utf-8-sig')
data = csv.reader(f)

city = '대구광역시'

for row in data:
    daegulist = []
    # 행정구역 1개에 대한 남성, 여성 인구수를 뽑는다.
    if city in row[0]:
         male_num = int(row[104].replace(',', ''))
         female_num = int(row[207].replace(',', ''))
         print(male_num, female_num)
         daegulist.append(male_num)
         daegulist.append(female_num)
         # 그래프 그린다.
         label = ['남성', '여성']
         plt.pie(daegulist,labels = label, autopct = '%1.1f%%', startangle = 90)
         plt.title(city)
         plt.savefig('hw_img/' + city + '.png', dpi=100)
         plt.close()

         break
'''