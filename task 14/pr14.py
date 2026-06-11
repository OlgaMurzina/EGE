alf = '0123456789abcdefghijklmnopqrstuvwxyz'

for x in alf[:12]:
    for y in alf[:12]:
        z = int(f'7{x}{y}2', 12) + int(f'3{y}6{x}8', 12)
        if z % 107 == 0:
            y = 8
            z = int(f'7{x}{y}2', 12) + int(f'3{y}6{x}8', 12)
            print(x, y, z // 107)