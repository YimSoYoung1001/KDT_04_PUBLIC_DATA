# 람다 ---------------------------------------------------
import operator
names = {'Mary':10999, 'Sams':2111,	'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}

print("[lambda] dict 정렬 : key 기준 오름차순")
res = sorted(names.items(), key = (lambda x: x[0]))
print(res)
print("[lambda] dict 정렬 : value 기준, 내림차순")
res = sorted(names.items(), key = (lambda x: x[1]), reverse = True)
print(res)
print('\n')

# operator ---------------------------------------------------
sorted_x = sorted(names.items(), key = operator.itemgetter(0))
print("[operator] dict 정렬 : key 기준, 오름차순")
print(sorted_x)

sorted_x = sorted(names.items(), key = operator.itemgetter(1), reverse = True)
print("[operator] dict 정렬 : value 기준, 내림차순")
print(sorted_x)

