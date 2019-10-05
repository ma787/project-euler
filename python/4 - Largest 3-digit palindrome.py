def palindrome(start):
    for x in range(start, 99, -1):
        pd = str(start * x)
        if pd == pd[::-1]:
            return int(pd)


max_num = 999
p_list = []

while max_num >= 100:
    number = palindrome(max_num)
    if number:
        p_list.append(number)
    max_num -= 1

print(max(p_list))
