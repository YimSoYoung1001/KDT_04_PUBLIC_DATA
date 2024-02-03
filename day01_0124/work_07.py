data_string1 = '2024-01-01'
print(data_string1.split())

data_string2 = '2023-12-31'
split_date_string = data_string2.split('-')
print(split_date_string)

year = split_date_string[0]
month = split_date_string[1]
day = split_date_string[2]

print(f'연도:{year}, 월:{month}, 일:{day}')
