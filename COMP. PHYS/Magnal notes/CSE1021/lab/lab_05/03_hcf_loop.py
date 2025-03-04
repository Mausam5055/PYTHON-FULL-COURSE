def find_hcf(a, b):
    # hcf = 1 
    m = min(a,b)+1
    for i in range(1, m):
        if a % i == 0 and b % i == 0:
            hcf = i 
    return hcf

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

print("The HCF of the two given numbers is : ", find_hcf(a,b))