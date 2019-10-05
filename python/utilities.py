def get_integer(message="Please enter a number: "):
    """Asks the user to enter a number and returns an integer."""
    number = input(message)
    while 1:
        try:
            number = int(number)
            break
        except ValueError:
            number = input("Please enter a number: ")
    return number


def factors(n):
    """Returns the factors of a natural number."""
    divisors = []
    m = int(n**0.5)

    for x in range(1,m+1):
        if n%x == 0:
            divisors.append(x)
            if int(n/x) not in divisors:
                divisors.append(int(n/x))

    return divisors

def prime_factors(n):
    """Returns the prime factors of a natural number."""
    if n < 0:
        return 0

    factors = []
    d = 2

    while n % d == 0:
        factors.append(d)
        n /= d

    d += 1

    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 2

    return factors


def prime_number_check(n):
    """Checks if an integer is prime."""
    if n <= 1:
        return 1

    sqrt = int(n ** 0.5)
    factors = [x for x in range(2, sqrt + 1) if n % x == 0]

    if not factors:
        return 0

    else:
        return 1


def factorial(n):
    """Finds the factorial of a natural number."""
    f = 1

    if n == 0:
        return f

    for x in range(1, n + 1):
        f *= x

    return f


def gcd(a, b):
    """Finds the greatest common divisor of 2 natural numbers."""
    while 1:
        q = a // b
        r = a - (b * q)

        if r == 0:
            return b

        else:
            a = b
            b = r
