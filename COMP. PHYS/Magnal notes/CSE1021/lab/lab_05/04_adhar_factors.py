def find_factors(number):
    factors = []  
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)  
    return factors

num = int(input("Enter the last 4 digits of your aadhar card : "))
factors = find_factors(num)
print(f"The factors of {num} are :", factors)