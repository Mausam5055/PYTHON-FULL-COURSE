def to_binary(n):
    if n == 0:
        return '0'
    
    binary = ''
    is_negative = n < 0
    n = abs(n)
    
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return '-' + binary if is_negative else binary


def to_hexadecimal(n):
    if n == 0:
        return '0'

    hex_chars = "0123456789ABCDEF"
    hexadecimal = ''
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16

    return '-' + hexadecimal if is_negative else hexadecimal


def to_octal(n):
    if n == 0:
        return '0'
    
    octal = ''
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        octal = str(n % 8) + octal
        n //= 8

    return '-' + octal if is_negative else octal


# Menu-driven interface
num = int(input("Enter the Number: "))
p = int(input("Enter the Number between 1 and 3:\n1. Binary\n2. Hexadecimal\n3. Octal\n"))

if p == 1:
    print("Binary:", to_binary(num))
elif p == 2:
    print("Hexadecimal:", to_hexadecimal(num))
elif p == 3:
    print("Octal:", to_octal(num))
else:
    print("Enter a valid number.")