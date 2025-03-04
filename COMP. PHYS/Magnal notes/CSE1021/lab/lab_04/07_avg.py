# pos_sum = 0
# neg_sum = 0
# pos_count = 0
# neg_count = 0
# while True :
#     num = float(input("Enter a number : "))
#     if num == -1 :
#         break
#     if num > 0:
#         pos_sum += num
#         pos_count += 1
#     elif num < 0:
#         neg_sum += num
#         neg_count += 1

# if pos_count > 0:
#     pos_avg = pos_sum/pos_count
# else :
#     pos_avg = 0

# if neg_count > 0:
#     neg_avg = neg_sum/neg_count
# else :
#     neg_avg = 0

# print(f"The average of positive numbers id {pos_avg} and the average of negative numbers is {neg_avg}")


#New Program
pos_sum = 0
neg_sum = 0
pos_count = 0
neg_count = 0

while True:
    num = float(input("Enter a number: "))
    
    if num == -1:
        break
    
    if num > 0:
        pos_sum += num
        pos_count += 1

    elif num < 0:
        neg_sum += num
        neg_count += 1

if pos_count > 0:
    pos_avg = pos_sum / pos_count
else:
    pos_avg = 0  

if neg_count > 0:
    neg_avg = neg_sum / neg_count  
else:
    neg_avg = 0  

print(f"The average of positive numbers is {pos_avg}")
print(f"The average of negative numbers is {neg_avg}")
