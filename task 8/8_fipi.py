"""

"""
from itertools import *

alf = sorted('АПРЕЛЬ')
ans = []
k = 0
for s in product(alf, repeat=6):
    sl = ''.join(s)
    k += 1
    if k % 2 == 1:
        if sl[0] not in 'АЛ' and sl.count('П')>= 2:
            ans.append((k, sl))
print(min(ans))
