# min S = 100_000
minn = 10 ** 12
z = 0
for x in range(15_000): # 6
    for y in range(290, 500): # 3
        st = '8' * x + '7' * y
        s = sum(int(a) for a in st)
        if s < 100_000:
            z = (100_000 - s) // 3
            if y + z >= 300:
                s = s + 3 * z
                if s >= 100_000:
                    minn = min(s + x + y + z, minn)
                elif s + 3 >= 100_000:
                    minn = min(s + 3 + x + y + z, minn)
            else:
                break
        else:
            if y >= 300:
                minn = min(s + x + y + z, minn)
            else:
                break
    print(minn)
print(minn)




