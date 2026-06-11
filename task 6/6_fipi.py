"""

"""
from turtle import *

m = 10

lt(90)

rt(45)
for _ in range(3):
    rt(45)
    fd(10 * m)
    rt(45)
rt(315)
fd(10 * m)
rt(90)
fd(20 * m)
rt(90)
for _ in range(2):
    fd(10 * m)
    rt(90)
up()
# не черепаха!!!
tracer(100)
k = 0
for x in range(-9, 10):
    for y in range(-9, 10):
        if x >= 0 and y < 0 or x < 0:
            goto(x * m, y * m)
            dot(5, 'green')
            k += 1
print(k)

done()
