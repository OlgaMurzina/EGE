'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [625681; 758641], числа,
имеющие ровно семь различных натуральных делителей, не считая единицы и самого числа. Среди этих делителей
не должно оказаться ни одного числа меньше 10.
Для каждого найденного числа запишите два наибольших делителя (не считая самого числа) в таблицу на экране
с новой строки в порядке возрастания.
'''


def good(x):
    de = []
    for d in range(2, round(x**0.5)+ 1):
        if x%d== 0:
            if d!=x:
                de.append(d)
                if x // d not in de and x//d != x:
                    de.append(x // d)
    de = sorted(de)
    des = [d for d in de if d >=10]
    if len(des)==7 and len(de)==7:
        return des
    return[]

from datetime import datetime

t1 = datetime.now()
for x in range(625681, 758642):
    y = good(x)
    if y:
        print(y[-2], y[-1])
t2 = datetime.now()
print(t2 - t1)

t1 = datetime.now()
for x in range(round(625681 ** 0.5) - 1, round(758642 ** 0.5) + 1):
    y = good(x ** 2)
    if y:
        print(y[-2], y[-1])
t2 = datetime.now()
print(t2 - t1)