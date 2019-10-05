from utilities import factors

num_factors = {}
am_numbers = []

for x in range(1, 10001):
    fact_x = factors(x)
    fact_x.remove(x)
    num_factors[x] = sum(fact_x)

pairs = [[x, y] for x, y in num_factors.items()]

for x in pairs:
    reverse = list(reversed(x))
    if reverse in pairs and x[0] != x[1]:
        if x[0] not in am_numbers and x[1] not in am_numbers:
            am_numbers.append(x[0])
            am_numbers.append(x[1])

for x in am_numbers:
    if am_numbers.count(x) > 1:
        am_numbers.remove(x)

print(sum(am_numbers))
