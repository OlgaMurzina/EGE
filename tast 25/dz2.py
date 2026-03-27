'''Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [397438; 443520], числа,
имеющие не менее 142 чётных различных натуральных делителей, не считая самого числа.
Для каждого найденного числа запишите в таблицу на экране количество делителей, подходящих под условие,
и максимальный из них с новой строки в порядке возрастания чисел.'''

def good(x):
    # поиск всех делителей числа
    de = []
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            if d % 2 == 0:
                de.append(d)
            if x // d not in de and x // d % 2 == 0:
                de.append(x // d)
    if len(de) >= 142:
        de = sorted(de)
        return len(de), de[-1]
    return ()

for x in range(397438, 443521):
    y = good(x)
    if y:
        print(*y)
print()

# решение Гриши
def good(n) -> list:
    de = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            if d % 2 == 0:
                de.append(d)
            if n // d not in de and (n // d) % 2 == 0:
                de.append(n // d)
    if len(de) >= 142:
        return sorted(de)
    return []

for x in range(397438, 443521):
    y = good(x)
    if y:
        print(len(y), max(y))