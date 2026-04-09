'''Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [625681; 758641], числа,
имеющие ровно семь различных натуральных делителей, не считая единицы и самого числа. Среди этих делителей не
должно оказаться ни одного числа меньше 10.
Для каждого найденного числа запишите два наибольших делителя (не считая самого числа) в таблицу на экране с новой
строки в порядке возрастания.'''


def good(x):
    # поиск всех делителей числа
    de = []
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            de.append(d)
            if x // d not in de:
                de.append(x // d)
    if len(de) == 7:
        if all([a > 9 for a in de]):
            de = sorted(de)
            return de[-2:]
    return []


from datetime import datetime

# эффективно только через полные квадраты
t1 = datetime.now()
for x in range(round(6256810 ** 0.5) - 1, round(7586420 ** 0.5) + 1):
    y = good(x ** 2)
    if y:
        print(*y)
t2 = datetime.now()
print(t2 - t1)


# решение Гриши
def deldig(n):
    r = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            r.append(d)
            if (n // d) not in r:
                r.append(n // d)
    if len(r) == 7:
        if len([x for x in r if x > 9]) == 7:
            return sorted(r)[-2:]
    return 0


print()
t1 = datetime.now()
for x in range(6266810, 7586420):
    y = deldig(x)
    if y:
        print(*y)
t2 = datetime.now()
print(t2 - t1)
