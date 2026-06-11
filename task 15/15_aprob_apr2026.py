ans = []
for a in range(0, 500):
    f = 1
    for x in range(0, 500):
        for y in range(0, 500):
            if ((x > a) or (y > a) or (x + 2 * y < 80)) == 0:
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        ans.append(a)
print(max(ans))