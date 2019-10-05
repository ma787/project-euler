from functools import reduce
from utilities import factors
import math


p_factors = {2: 4, 3: 4, 5: 4, 7: 1, 11: 1}
n_factors = [x ** y for x, y in p_factors.items()]
num = reduce(lambda x, y: x * y, n_factors)

a = 0.5
b = 0.5
c = -1 * num

n = -b + (((b ** 2) - (4 * a * c)) ** 0.5)
diff = math.modf(n)

if diff[0] == 0:
    print(num)

n = math.ceil(n)
num = 0.5*n*(n+1)

while 1:
    factor_list = factors(num)
    div_count = len(factor_list)

    if div_count > 500:
        print(num)
        break
    else:
        num += (n + 1)
        n += 1