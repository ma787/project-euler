from functools import reduce
from utilities import prime_factors


factors = {x: prime_factors(x) for x in range(1, 21)}
common = []

for x in factors:
    for y in range(1, 21):
        if y in factors[x] and y not in common:
            common.append(y)

factor_count = {x: [] for x in common}

for x, y in factors.items():
    for z in common:
        num = y.count(z)
        if num > 0:
            factor_count[z].append(num)

for x, y in factor_count.items():
    power = max(y)
    factor_count[x] = power

factor_list = [x ** y for x, y in factor_count.items()]
lcm = reduce(lambda x, y: x * y, factor_list)

print(lcm)
