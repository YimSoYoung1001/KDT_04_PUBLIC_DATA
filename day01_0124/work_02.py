import csv

# encoding = 'utf-8-sig'로 '\ufeff' 제거
fin = open('daegu.csv', 'r', encoding ='utf-8-sig')
data = csv.reader(fin, delimiter = ',')

# newline = '': 한 라인씩 건너뛰며 저장되는 현상 없앰
fout = open('daegu-utf8.csv', 'w', newline ='', encoding ='utf-8-sig')
wr = csv.writer(fout)

for row in data:
    for i in range(len(row)):
        row[i] = row[i].replace('\t', '')
    print(row)
    wr.writerow(row)

fin.close()
fout.close()

print('파일저장완료')
