import math

def prime_factors(n):
    factors = []  

    while n % 2 == 0:
        factors.append(2)
        n //= 2
    factor = 3
    while factor  <= math.sqrt(n):
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    if n > 2:
        factors.append(n)
    return factors

numbers = [64, 128, 10000]

for num in numbers:
    print(f"Prime factors of {num}: {prime_factors(num)}")
