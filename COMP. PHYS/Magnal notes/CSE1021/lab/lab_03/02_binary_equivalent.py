def decimal_to_binary(decimal_number):
    binary_result = ""
    
    if decimal_number == 0:
        return "0"
    
    while decimal_number > 0:
        remainder = decimal_number % 2 
        binary_result = str(remainder) + binary_result 
        decimal_number = decimal_number // 2  

    return binary_result

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"The binary equivalent of {decimal_number} is: {binary_number}")
