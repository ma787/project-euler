from functools import reduce


num_list = [2]
sign = []
num = 2000000
i = 1
x = 0

while 1:
    x = 2 * i + 1
    if x >= num:
        break
    num_list.append(x)
    i += 1

for x in range(0, len(num_list)):
    sign.append(0)

num_dict = dict(zip(num_list, sign))

end = int(num**0.5)
p = 0
i = 1

while p < end:
    p = num_list[i]
    multi = p**2

    while multi < num:
        num_dict[multi] = 1
        multi += (2*p)

    i += 1

primes = [x for x,y in num_dict.items() if y == 0]

sum = reduce(lambda x,y: x+y,primes)

print(sum)
