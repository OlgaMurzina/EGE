'''(№ 7353) В файле электронной таблицы 9-228.xls в каждой строке записаны шесть натуральных чисел.
Назовём ячейку таблицы интересной, если выполняются следующие условия:
– число в данной ячейке больше не встречается в данной строке;
– число в данной ячейке встречается в данном столбце, включая данную ячейку, менее 170 раз.
Определите количество интересных ячеек в таблице. В ответе запишите только число.'''

data1 = open('9-228.csv').readlines()
print(data1[:5])
data = []
for s in data1:
    data.append([int(x) for x in s.split(';')])
# print(data[:5])

data_tr = []
for j in range(6):
    s = []
    for i in range(len(data)):
        s.append(data[i][j])
    data_tr.append(s)
print(data_tr[:1])

ans = []
for s in data:
    for j in range(len(s)):
        if s.count(s[j]) == 1:
            if data_tr[j].count(s[j]) < 170:
                ans.append(s[j])
print(len(ans))



