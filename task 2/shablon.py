# (¬x ∧ y ∧ z) ∨ (¬x ∧ ¬z)
#  (x →(y →z)) ∧ (y →(z ≡ ¬w))
alf = [0, 1]
print('x y z w')
for x in alf:
    for y in alf:
        for z in alf:
            for w in alf:
                if ((x <= (y <= z)) and (y <= (z == (not w)))) == 0:
                    print(x, y, z, w)