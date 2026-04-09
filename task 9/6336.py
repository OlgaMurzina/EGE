'''(№ 6336) *В файле электронной таблицы 9-202.xls в каждой строке записаны 6 неотрицательных целых чисел.
Определите количество строк таблицы, содержащих хотя бы одну ячейку со следующими свойствами:
– число в данной ячейке не повторяется в ячейках этой строки;
– число в данной ячейке встречается ровно 7 раз в других ячейках всей таблицы.'''

data1 = open('/home/dmurzin/Downloads/9-202.csv').readlines()
data = []
for st in data1:
    data.append([int(x) for x in st.split(';')])
print(data[:5])

data2 = []
for st in data1:
    data2.extend([int(x) for x in st.split(';')])
print(data2[:25])

ans = []
for st in data:
    k = 0
    for y in st:
        if st.count(y) == 1:
            if data2.count(y) == 8:
                k += 1
    if k > 0:
        ans.append(st)
print(len(ans))
