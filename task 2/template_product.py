from itertools import product

print('x y z w')
a = [0, 1]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                if ((w or x or y) <= ((y or z) and x or y and (w or z))) == 0:
                    print(x, y, z, w)
print()                    
for x, y, z, w in product(a, repeat=4):
    if ((w or x or y) <= ((y or z) and x or y and (w or z))) == 0:
        print(x, y, z, w)