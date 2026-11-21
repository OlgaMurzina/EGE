'''(№ 8934) *(А. Сражаев) Напишите программу, которая перебирает целые числа, превышающие 9 200 000,
которые можно представить в виде произведения a**3·b**3 = (a * b) ** 3, где a и b – два различных простых натуральных числа,
причём хотя бы одно из которых содержит цифру 3. В ответе запишите в первом столбце первые 5 найденных чисел
в порядке возрастания, а во втором столбце — сумму чисел a и b.'''

def isprime(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

from datetime import datetime

t1 = datetime.now()
prime = [x for x in range(2, 1000) if isprime(x)]
prime3 = [x for x in range(3, 1000, 2) if isprime(x) and '3' in str(x)]

ans = set()
for a in prime:
    for b in prime3:
        if a != b:
            x = (a * b) ** 3
            if x > 9_200_000:
                # print(x)
                ans.add((x, a + b))
ans = sorted(ans)
print(*ans[:5], sep='\n')
t2 = datetime.now()
print(t2 - t1)
