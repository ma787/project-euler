from functools import reduce
from utilities import gcd

top = []
bottom = []

for x in range(10, 99):
    for y in range(x+1, 100):
        num = [a for a in str(x)]
        den = [a for a in str(y)]

        if num[-1] == 0:
            pass

        elif num[-1] == den[0]:
            num.remove(num[-1])
            num = int("".join(num))

            den.remove(den[0])
            den = int("".join(den))

            if den == 0:
                pass

            else:
                check = num / den
                actual = x / y

                if check == actual:
                    top.append(x)
                    bottom.append(y)

top = reduce(lambda x, y: x*y, top)
bottom = reduce(lambda x, y: x*y, bottom)
div = gcd(top, bottom)

bottom /= div
print(bottom)