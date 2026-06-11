from turtle import *

tracer(100)
m = 5
lt(90)

a = 2496
fd(2 * m)
for i in range(5):
    fd(a * m)
    rt(90)
    fd(3 * m)
    rt(90)
    fd(a * m)
    lt(90)
    fd(1 * m)
    lt(90)

fd(-2 * m)
up()

k = 0
for x in range(1, 20):
    for y in range(1, a + 2):
        goto(x * m, y * m)
        dot(2, 'blue')
        k += 1

done()
print(k)