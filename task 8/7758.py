'''(№ 7758) (О. Лысенков) Определите количество чисел, 25-ричная запись которых содержит четыре цифры, причём
в этой записи чётные и нечётные цифры чередуются и сумма числовых значений цифр числа кратна 5.'''

from itertools import product, repeat

alf = range(25)
ans = []
for s in product(alf, repeat=4):
    if s[0] != 0:
        if sum(s) % 5 == 0:
            for i in range(3):
                if s[i] % 2 == s[i + 1] % 2:
                    break
            else:
                ans.append(s)
print(len(ans))