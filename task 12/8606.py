ans = []
for x in range(700):   # 2
    for y in range(700):  # 3
        z = 699 - x - y   # 4
        if x + y + z == 699 and z >= 0:
            s = x * '2' + y * '3' + z * '4'
            s1 = s.replace('2', '0').replace('3', '1').replace('4', '2')
            if sum(int(x) for x in s1) + 1 == 400:
                print(x, y, z)
                ans.append(sum(int(x) for x in s))
print(max(ans))
