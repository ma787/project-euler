import utilities

lim = 28123
num_list = list(range(1, lim+1))
a_nums = []

for x in range(12, lim+1):
    div_list = utilities.factors(x)
    div_list.remove(x)
    div_sum = sum(div_list)
    if div_sum > x:
        a_nums.append(x)

a_nums = set(a_nums)

for n in range(24, lim+1):
    for x in a_nums:
        if x > n:
            break
        else:
            diff = n - x
            if diff in a_nums:
                num_list.remove(n)
                break

summation = sum(num_list)
print(summation)
