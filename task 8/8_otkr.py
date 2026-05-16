from itertools import *

alf = sorted('апрель')
ans = []
k = 0
for x in product(alf, repeat=6):
    sl = ''.join(x)
    k += 1
    if k % 2 == 1:
        if sl[0] not in 'ал':
            if sl.count('п') >= 2:
                ans.append((k, sl))
print(ans[0], ans[-1])
