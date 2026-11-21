'''(№ 8406) *(А. Сражаев) Назовём особым числом такое простое натуральное число, которое на 150 больше
ближайшего меньшего простого числа. Напишите программу, которая находит все особые числа на отрезке
[10 000 000; 30 000 000]. В ответе запишите все найденные особые числа, справа от каждого из них запишите сумму
всех делителей числа, полученного из найденного особого числа после удаления первой и последней цифр.'''

def isprime(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def good(x):
    de = {1, x}
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            de.add(d)
            de.add(x // d)
    if de:
        return sum(de)
    return 0

s = min(x for x in range(10_000_001, 10_000_100, 2) if isprime(x))
print(s)
prime = []
a = s
for x in range(s, 30_000_001, 2):
    if isprime(x):
        b = x
        if b - a == 150:
            prime.append(b)
            print(b)
        a = b

print(len(prime))
for x in prime:
    y = good(int(str(x)[1:-1]))
    if y:
        print(x, y)
