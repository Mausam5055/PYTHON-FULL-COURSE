def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):  # Outer loop: Number of passes
        for j in range(i):  # Inner loop: Compare adjacent elements
            if nums[j] > nums[j + 1]:  # If left element is greater than right
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap

nums = [2, 8, 4, 61, 45, 23, 1, 0, 5, 3, 7]
bubble_sort(nums)
print(nums)


# In the Bubble Sort code, i and j are loop variables used for controlling the
# sorting process. Let's break it down:

#             Role of i (Outer Loop):
# 1.i represents the number of passes we make through the list.
# 2.It starts from len(nums) - 1 (last index) and goes down to 1, decreasing in 
# each iteration.
# 3.This ensures that after each pass, the largest remaining element is correctly placed at the end.

# Role of j (Inner Loop):
# 1.j iterates through the unsorted part of the list.
# 2.It starts from 0 and goes up to i - 1 (meaning it only goes through unsorted
# elements).
# 3.It compares nums[j] with nums[j + 1] and swaps them if they are in the 
# wrong order.

