
from itertools import *

def v(x, y, z, w):
    return x <= ((w <= y) != z)

for a,b,c,d,e in product([0, 1], repeat=5):
    t = ((a, 1,1,1,1),
         (0,0,b,c,0),
         (d,0,e,0,0))
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if all(v(**dict(zip(p, r))) == r[-1] for r in t):
                print(''.join(p))