'''(№ 7352) В файле электронной таблицы 9-228.xls в каждой строке записаны шесть натуральных чисел.
Назовём ячейку таблицы интересной, если выполняются следующие условия:
– число в данной ячейке больше не встречается в данной строке;
– число в данной ячейке встречается в данном столбце, включая данную ячейку, больше 180 раз.
Определите количество строк в таблице, содержащих более трёх интересных ячеек.
В ответе запишите только число.'''

data1 = open('/home/dmurzin/Downloads/9-228.csv').readlines()
data = []
for st in data1:
    data.append([int(x) for x in st.split(';')])
print(data[:5])
# транспонированная матрица
data2 = []
for j in range(6):
    s = []
    for i in range(len(data)):
        s += [data[i][j]]
    data2.append(s)
print(*data2, sep='\n')

ans = []
for st in data:
    # счетчик на строку
    k = 0
    for j in range(6):
        if st.count(st[j]) == 1:
            if data2[j].count(st[j]) > 180:
                k += 1
    if k > 3:
        ans.append(st)
print(len(ans))
