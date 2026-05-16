data = [int(x) for x in open("17_2.txt").readlines()]

max_42 = [int(x) for x in data if abs(x) % 100 == 42]
max_42 = sorted(max_42)[-1]

k = 0
ans = []
for i in range(len(data) - 2):
    s = data[i: i + 3]
    for x in s:
        if 100 <= abs(x) <= 999 and x % 10 == 9:
            k += 1
            if sum(s) > max_42:
                ans.append(sum(s))
print(k, max(ans))