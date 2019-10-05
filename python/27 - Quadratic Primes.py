from utilities import prime_number_check

a = 999
b = 999
n = 0
values = []

while b >= 2:
    num = n**2 + a*n + b
    if num < 0:
        values.append((a, b, n))
        a = 999
        b -= 1
        n = 0
    elif num % 2 == 0 and num > 2:
        values.append((a, b, n))
        if a < -999:
            a = 999
            b -= 1
        else:
            a -= 1
        n = 0
    elif prime_number_check(num) == 0:
        n += 1
    else:
        values.append((a, b, n))
        if a < -999:
            a = 999
            b -= 1
        else:
            a -= 1
        n = 0

numbers = [x[2] for x in values]
maxv = max(numbers)
point = numbers.index(maxv)
t = values[point]
product = t[0] * t[1]
print("""
a = {}
b = {}
n = {}
a*b = {}.""".format(t[0], t[1], t[2], product))
