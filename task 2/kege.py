from itertools import *

def v(x, y, z, w):
    return (x and (not z) and (not w)) or (x and (not z) and y)

for a,b,c,d,e,f,g in product([0,1], repeat=7):
    t = ((1,a,b,c),
         (0,d,1,e),
         (f,g,0,0))
    if len(set(t)) == 3:
        for p in permutations('wzyx'):
            if all(v(**dict(zip(p, r))) == 1 for r in t):
                print(*p, sep='')


def u(x,y,z,w):
    return (x or y) and (not(y == z)) and (not w)

for a,b,c,d in product([0,1], repeat=4):
    t =((1,a,1,b),
        (0,1,c,0),
        (d,1,1,0))
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if all(u(**dict(zip(p, r))) == 1 for r in t):
                print(*p, sep='')
