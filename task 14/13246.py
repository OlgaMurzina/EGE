alf = '0123456789abcdefghijklmnopqrstuvwxyz'
for p in range(10, 37):
    for x in alf[:p]:
        for y in alf[:p]:
            if int(f'24{x}9', p) + int(f'{y}{x}{y}3', p) == int(f'{x}4{y}0', p):
                print(p, int(f'{x}{y}{y}', p))
                break