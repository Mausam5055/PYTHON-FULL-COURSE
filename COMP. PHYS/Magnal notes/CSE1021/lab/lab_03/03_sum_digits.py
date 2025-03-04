def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10 
        total += digit 
        number = number // 10  
    return total

num = int(input("Enter the number whose sum of digits is to be calculated : "))
total = sum_of_digits(num)
print(f"The sum of digits of {num} is  {total}")