'''(№ 7351) В файле электронной таблицы 9-228.xls в каждой строке записаны шесть натуральных чисел.
Назовём ячейку таблицы интересной, если выполняются следующие условия
– число в данной ячейке больше не встречается в данной строке;
– число в данной ячейке встречается в данном столбце, включая данную ячейку, больше 180 раз.
Определите количество интересных ячеек в таблице. В ответе запишите только число.'''

data1 = open('/home/dmurzin/Downloads/9-228.csv').readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
# print(data[:10])

data_tr = []
for j in range(6):
    for i in range(len(data)):
        s += [data[i][j]]
        data_tr.append(s)

ans = []
for i in range(len(data)):
    st = data[i]
    for j in range(6):
        if st.count(st[j]) == 1:
            if data_tr[j].count(st[j]) > 180:
                ans.append(st[j])
                print(st[j])
print(len(ans))