#Different types of function i array
vowels = ['a', 'e', 'i','i', 'o', 'u']
count = vowels.count('i')
print('The count of i is:', count)
count = vowels.count('p')
print('The count of p is:', count)

# FINDING THE MAXIMUM NUMBER IN A SET(M1)
# Initialize array
arr = [25, 11, 7, 75, 56,100]

# Initialize max with first element of array
max_num = arr[0]  # renamed from 'max' to avoid built-in function conflict

# Loop through the array
for i in range(len(arr)):
    # Compare elements of array with max
    if arr[i] > max_num:
        max_num = arr[i]

print("Largest element present in given array:", max_num)

# Using max function(M-2)
array = [456, 700, 200]
print("Max value element : ",max(array)) # Output: 700