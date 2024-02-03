import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib
import math

def draw_scatter(city, male_list, female_list, bubble_size_list):
    plt.figure(figsize =(8,4), dpi = 100)
    plt.scatter(male_list, female_list, s=bubble_size_list, c=range(101), alpha = 0.5, cmap = 'jet')
    plt.colorbar()
    plt.plot(range(max(male_list)), range(max(male_list)), 'g--')

    plt.title(city + ' 지역의 남녀 인구수 비교')
    plt.xlabel('남성 인구수')
    plt.ylabel('여성 인구수')
    plt.show()


def calculate_population():
    f = open('gender.csv', encoding = 'utf-8-sig')
    data = csv.reader(f)
    male_list = []
    female_list = []
    bubble_size_list = []
    city = input('찾고싶은 지역의 이름: ')

    for row in data:
        if city in row[0]:
            for i in range(106, 207):
                male_num = int(row[i].replace(',',''))
                female_num = int(row[i + 103].replace(',',''))

                bubble_size_list.append(math.sqrt(male_num + female_num))

                male_list.append(male_num)
                female_list.append(female_num)
            break

    f.close()
    print(f"[여성인구]: {female_list}")
    print(f"[남성인구]: {male_list}")
    draw_scatter(city, male_list, female_list, bubble_size_list)

calculate_population()