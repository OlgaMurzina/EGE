
ans = []
for x in range(500): # 1
    for y in range(700): # 0
        z = 700 - x - y # 2
        if z > 0:
            # print(x, y, z, x * 1 + z * 2, y * 2 + z * 1)
            if (x * 1 + z * 2) * 3 == (y * 2 + z * 1):
                # print(x, y, z, x * 1 + z * 2, y * 2 + z * 1)
                ans.append(z)
print(ans)

ans = []
for x in range(500): #1
    for y in range(700): #0
        for z in range(700): # 2
            if x + y + z == 700:
                if (x * 1 + z * 2) == (y * 2 + z * 1) / 3:
                    ans.append(z)
print(ans)