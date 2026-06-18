'''Для какого наименьшего натурального числа A формула
(y > 10) ∨ (x · A > y + x)
тождественно истинна, то есть принимает значение 1 при любых x и y ?'''

ans = []
for a in range(1, 500):
    f = 1
    for x in range(1, 1000):
        for y in range(500):
            if ((y > 10) or (x * a > y + x)) == 0:
                f = 0
                break
        if not f:
            break
    if f:
        ans.append(a)
        break
print(min(ans))