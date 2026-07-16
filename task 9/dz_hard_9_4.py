'''Определите количество строк таблицы, для чисел которых выполнены оба условия:
в строке есть два числа, каждое из которых повторяется дважды, остальные три числа различны;
среднее арифметическое трёх неповторяющихся чисел строки не больше среднего арифметического
всех её чисел.
В ответе запишите только число.'''

data1 = open('9.csv').readlines()
data = []
data_all = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
    data_all.extend(s)
print(data[:7])
print(data_all[:7])
print(max(data), max(data_all))

'''
ans = []
for i in range(len(data)):
    st = sorted(data[i])
    dbl = [x for x in st if st.count(x) == 2]
    unq = [x for x in st if st.count(x) == 1]
    if len(dbl) == 4 and len(unq) == 3:
        avg = sum(st) / len(st)
        avg_unq = sum(unq) / len(unq)
        if avg_unq <= avg:
            ans.append(st)
print(len(ans))
# print(ans)'''