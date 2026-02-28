'''Откройте файл электронной таблицы, в каждой строке которой шесть натуральных чисел.
Каждое означает количество определённого вида подарков (конфеты, мандарины, шоколадки,
игрушки, книги, наборы для творчества). Определите количество строк таблицы с числами,
для которых работают не менее двух из трёх условий:
в строке одно число повторяется трижды, остальные различны
чётных чисел больше, чем нечётных
сумма двух наибольших значений больше, чем в два раза превышает сумму остальных значений
В ответе запишите только число.'''

data1 = open('9__6.csv').readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
# print(data)

ans = []
for i in range(len(data)):
    st = sorted(data[i])
    tr = [x for x in st if st.count(x) == 3]
    unq = [x for x in st if st.count(x) == 1]
    odd = [x for x in st if x % 2 != 0]
    edd = [x for x in st if x % 2 == 0]
    usl = [len(tr) == 3 and len(unq) == 3,
           len(odd) < len(edd),
           sum(st[-2:]) > 2 * sum(st[:-2])]
    if usl.count(1) >= 2:
        ans.append(st)
print(len(ans))
# print(ans)
