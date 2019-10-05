from utilities import factorial


f_dict = {0: 1}

for x in range(1, 10):
    f_dict[x] = factorial(x)


def fact_sum(n):
    """Returns the sum of the factorials of the digits of n."""
    fact = 0
    m = str(n)
    for digit in m:
        digit = int(digit)
        fact += f_dict[digit]

    return fact


c_nums = []
num = factorial(9) * 7

# it is impossible for the condition to be true for an 8-digit number
# because 9! * 8 is a 7 digit number
# and 9! * 7 is the largest value of a factorial sum of a 7-digit number

for a in range(1, num+1):
    f = fact_sum(a)
    if a == f:
        c_nums.append(a)


c_nums.remove(1)
c_nums.remove(2)
print(sum(c_nums))
