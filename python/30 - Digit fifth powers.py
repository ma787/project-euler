from functools import reduce


values = []
lim = 7 * 9**5

for x in range(0, lim+1):
    y = str(x)
    digits = []
    for a in y:
        z = int(a)
        digits.append(z)

    powers = [x**5 for x in digits]

    num = reduce(lambda p, q: p+q, powers)

    if x == num:
        values.append(num)

values.remove(1)
print(sum(values))