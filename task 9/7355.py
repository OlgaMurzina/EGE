'''(№ 7355) В файле электронной таблицы 9-228.xls в каждой строке записаны шесть натуральных чисел. Назовём ячейку
таблицы интересной, если выполняются следующие условия:
– число в данной ячейке больше не встречается в данной строке;
– число в данной ячейке встречается в данном столбце, включая данную ячейку, менее 170 раз.
Определите количество строк в таблице, содержащих не менее одной, но не более четырёх интересных ячеек.
В ответе запишите только число.'''

data1 = open('/home/dmurzin/Downloads/9-228.csv').readlines()
print(data1[:5])
data = []
for st in data1:
    data.append(list(map(int, st.split())))
print(data[:5])
data_tr = []
for j in range(6):
    s = []
    for i in range(len(data)):
        s.append(data[i][j])
    data_tr.append(s)
print(data_tr[:1])

ans = []
for st in data:
    k = 0
    for x in st:
        if st.count(x) == 1:
            if data_tr[st.index(x)].count(x) < 170:
                k += 1
    if 1 <= k <= 4:
        ans.append(st)
print(len(ans), ans[:5])

