'''Пусть R — сумма всех делителей числа, оканчивающихся на 8, не считая самого числа. Если таких делителей
у числа нет, то значение R считается равным нулю.
Напишите программу, которая среди натуральных чисел на отрезке [114578, 114616] ищет все числа, для которых
значение R оканчивается на 6.
Для каждого найденного числа в отдельной строке таблицы запишите само число, а также значение R.'''

def good(x):
    # поиск всех делителей числа
    de = []
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            if d % 10 == 8:
                de.append(d)
            if x // d % 10 == 8 and x // d not in de:
                de.append(x // d)
    if sum(de) % 10 == 6:
        return sum(de)
    return 0

for x in range(114578, 114617):
    y = good(x)
    if y:
        print(x, y)
print()

# решение Гриши
def deldig(n):
    r = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            if d % 10 == 8:
                r.append(d)
            if n // d not in r and (n // d) % 10 == 8:
                r.append(n // d)
    if sum(r) % 10 == 6:
        return sum(r)
    return []

for x in range(114578, 114617):
    z = deldig(x)
    if z:
        print(x, z)