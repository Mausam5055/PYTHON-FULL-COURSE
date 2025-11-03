# Write a program to calculate the sum of numbers from 1 to 20 which are not divisible
# 2, 3 or 5.
total_sum = 0
for i in range(1, 21):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        total_sum += i
print("The sum of numbers from 1 to 20 that are not divisible by 2, 3, or 5 is:", total_sum)
