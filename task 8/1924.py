'''(№ 1924) Артур составляет 5-буквенные коды перестановкой букв слова ВОРОН. При этом нельзя ставить рядом две гласные.
Сколько различных кодов может составить Артур?'''
from itertools import *

alf = 'ВОРОН'
ans = []
for s in permutations(alf):
    sl = ''.join(s)
    if 'ОО' not in sl:
        ans.append(sl)
print(len(ans), len(set(ans)))