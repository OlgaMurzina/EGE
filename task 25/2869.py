'''(№ 2869) (Д.Ф. Муфаззалов) Найдите в диапазоне [2; 10000000] числа, каждое из которых имеет максимальное
количество простых делителей среди всех чисел этого отрезка. Выведите минимальное из найденных чисел и через
пробел количество его простых делителей.'''

def is_prime(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def good(n):
    if is_prime(n):
        de = [n]
    else:
        de = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            if is_prime(d):
                de.append(d)
            if is_prime(n // d) and n // d not in de:
                de.append(n // d)
    return len(de)

ans = []
for x in range(2, 10_000_000 + 1):
    y = good(x)
    if y:
        ans.append((y, x))
print(sorted(ans)[::-1][:10])