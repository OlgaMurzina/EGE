'''(№ 1925) Артур составляет 5-буквенные коды из букв А, П, О, Р, Т. Каждую букву нужно использовать ровно один раз,
при этом нельзя ставить рядом две гласные. Сколько различных кодов может составить Артур?'''

from itertools import *

alf = 'АПОРТ'
ans = []
for s in permutations(alf):
    sl = ''.join(s)
    if 'АО' not in sl and 'ОА' not in sl:
        ans.append(sl)
print(len(ans), len(set(ans)))
