'''(№ 8899) Сколько существует чисел, четырнадцатеричная запись которых содержит пять цифр, среди которых есть
только две нечётные цифры, причём они равны между собой и между ними стоит только одна цифра.'''

from itertools import product, repeat

alf = range(14)
ans = []
for s in product(alf, repeat=5):
    if s[0] != 0:
        odd = set([x for x in s if x % 2])
        if len(odd) == 1:
            for i in range(3):
                if s[i] == s[i + 2] and s[i + 1 ] != s[i] and s[i] % 2 and s.count(s[i]) == 2:
                    ans.append(s)
print(len(ans))
