from utilities import factorial


num = factorial(100)
digits = [int(x) for x in str(num)]
print(sum(digits))