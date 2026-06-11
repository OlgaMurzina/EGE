from turtle import *

m = 20
tracer(100)

lt(90)

for _ in range(2):
    fd(7 * m)
    rt(90)
    fd(8 * m)
    rt(90)
up()
fd(2 * m)
rt(90)
fd(3 * m)
lt(90)
down()
for _ in range(2):
    fd(4 * m)
    rt(90)
    fd(2 * m)
    rt(90)
up()
for x in range(0, 10):
    for y in range(0, 10):
        goto(x * m, y * m)
        dot(3, 'red')
done()