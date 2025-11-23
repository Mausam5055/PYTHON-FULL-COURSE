print("Prime numbers from 2 to 1000 are:")

for n in range(2, 1001):  # Loop from 2 to 1000
    factors_of_n = 0
    for i in range(1, n+1):
        if n % i == 0:
            factors_of_n += 1
    if factors_of_n == 2:
        print(n, end=" ")

