'''
Определите количество строк таблицы с числами, для которых выполнены все условия:
в строке есть два различных повторяющихся числа
сумма повторяющихся чисел (каждое учитывается один раз) меньше суммы неповторяющихся. Если неповторяющихся чисел нет,
их сумма считается равной нулю
В ответе запишите только число.
'''

data = open('9-5.csv').readlines()
a = list(map(lambda x: list(map(int, x[:-1].split(','))), data))
k = 0
for m in a:
    double = set(i for i in set(m) if m.count(i) > 1)
    uniq = [i for i in set(m) if m.count(i) == 1]
    if len(double) == 2:
        sum1 = sum(double)
        sum2 = sum(uniq)
        if sum1 < sum2:
            k += 1
print(k)