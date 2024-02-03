import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

label = ['유임승차', '유임하차', '무임승차', '무임하차']
pic_count = 0
with open('subwayfee.csv', encoding ='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)

    for row in data:
        for i in range(4,8):
            row[i] = int(row[i])
        print(row)
        plt.figure(dpi=100)
        plt.title(row[3] + ' ' + row[1])
        plt.pie(row[4:8], labels = label, autopct = '%.1f%%')
        plt.savefig('img/' + row[3] + ' ' + row[1] + '.png')
        plt.close()

        pic_count +=1
        if pic_count >= 10:
            break
