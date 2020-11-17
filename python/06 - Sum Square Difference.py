number_list = [x for x in range(1,101)]

n = len(number_list)

sum_of_squares = (1/6)*n*(n+1)*(2*n + 1)
square_of_sum = (0.5*n*(n+1))**2

print(int(square_of_sum - sum_of_squares))
