import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('daegu-utf8.csv', encoding ='utf-8-sig')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))
f.close()
plt.hist(aug, bins = 100, color = 'tomato', label = 'Aug')
plt.hist(jan, bins = 100, color = 'b', label = 'Jan')

plt.xlabel("temperature")
plt.rc('axes', unicode_minus=False)

plt.legend()
plt.show()