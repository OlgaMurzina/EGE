'''(№ 8227) (О. Лысенков) Сколько существует чисел, пятеричная запись которых содержит 9 знаков и
в которых ровно два раза чётные цифры стоят рядом, при этом никакие три четные цифры не стоят рядом?'''

from itertools import product, repeat

alf = range(5)
ans = []
for s in product(alf, repeat=9):
    sl = ''.join([str(x) for x in s]).replace('2', '0').replace('4', '0')
    if s[0] != 0:
        if sl.count('00') == 2 and sl.count('000') == 0:
            ans.append(s)
print(len(ans), ans[-1000:-950])
