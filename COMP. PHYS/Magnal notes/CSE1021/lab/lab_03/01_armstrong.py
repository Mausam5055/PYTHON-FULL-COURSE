def armstrong_num(num):
    
    digits = str(num)  
    num_digits = len(digits)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    if sum_of_powers == num:
         print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

num = int(input("Enter a number: "))
armstrong_num(num)