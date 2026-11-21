'''(№ 8867) (Р. Косов) Напишите программу, которая перебирает числа, большие 9 590 000, в порядке возрастания
и находит первые 5 чисел, которые можно представить в виде произведения ровно семи различных простых сомножителей,
среди которых ровно 2 содержат цифру 7. Запишите эти 5 чисел в порядке возрастания, справа от каждого числа запишите
сумму его сомножителей, содержащих цифру 7.'''

def isprime(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

from datetime import datetime

t1 = datetime.now()
prime = [x for x in range(2, 50) if isprime(x)]
prime2 = [x for x in range(3, 5500, 2) if isprime(x)]
prime7 = [x for x in range(7, 100, 2) if isprime(x) and '7' in str(x)]
ans = set()
for x1 in prime7:
    for x2 in prime7:
        for x3 in prime:
            for x4 in prime:
                for x5 in prime:
                    for x6 in prime:
                        for x7 in prime2:
                            a = [x1, x2, x3, x4, x5, x6, x7]
                            if len(set(a)) == 7:
                                y = x1 * x2 * x3 * x4 * x5 * x6 * x7
                                if (y, x1 + x2) not in ans:
                                    if 9_590_000 < y <= 9_700_000:
                                        ans.add((y, x1 + x2))
                                        print(y, x1 + x2)
ans = sorted(ans)
print(*ans[:5], sep='\n')
t2 = datetime.now()
print(t2 - t1)