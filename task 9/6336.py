'''(№ 6336) *В файле электронной таблицы 9-202.xls в каждой строке записаны 6 неотрицательных целых чисел.
Определите количество строк таблицы, содержащих хотя бы одну ячейку со следующими свойствами:
– число в данной ячейке не повторяется в ячейках этой строки;
– число в данной ячейке встречается ровно 7 раз в других ячейках всей таблицы.'''

data1 = open('9-202.csv').readlines()
data = []
data_all = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
    data_all.extend(s)
print(data[:5])
print(data_all[:30])

'''
ans = []
for st in data:
    k = 0
    for y in st:
        if st.count(y) == 1:
            if data2.count(y) == 8:
                k += 1
    if k > 0:
        ans.append(st)
print(len(ans))'''
