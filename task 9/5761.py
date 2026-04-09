'''(№ 5761) (Д. Статный) В файле электронной таблицы 9-177.xls в каждой строке содержатся восемь
неотрицательных чисел. Определите количество строк таблицы, для которых выполнены оба условия:
– квадрат суммы максимального и минимального числа больше суммы квадратов других чисел;
– в строке есть хотя бы одно повторяющееся число.'''

data1 = open('/home/dmurzin/Downloads/9-177.csv').readlines()
data = []
for st in data1:
    data.append([int(x) for x in st.split(';')])
print(data[:5])

ans = []
for st in data:
    a = sorted(st)
    if (a[0] + a[-1]) ** 2 > sum([x ** 2 for x in a[1:-1]]) :
        b = [x for x in st if st.count(x) > 1]
        if len(b) > 0:
            ans.append(st)
print(len(ans))