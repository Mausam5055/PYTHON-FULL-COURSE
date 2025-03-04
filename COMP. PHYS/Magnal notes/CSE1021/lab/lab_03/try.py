def armstrong_check(num):
    
    ori_num = num
    l = len(str(num))
    sum = 0
    while num > 0:
        sum += ((num%10)**l)
        num = num//10
    if sum == ori_num:
        print("The number is  an armstrong number")
    else:
        print("The number is not an armstrong number")

num = int(input("Enter a number: "))
armstrong_check(num)