year = 1901
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 2
count = 0

while year < 2001:
    if year % 100 == 0:
        if year % 400 == 0:
            months[1] = 29
        else:
            months[1] = 28

    elif year % 4 == 0:
        months[1] = 29

    else:
        months[1] = 28

    for x in months:
        if day % 7 == 0:
            count += 1
        day += (x-28)

    year += 1

print(count)
