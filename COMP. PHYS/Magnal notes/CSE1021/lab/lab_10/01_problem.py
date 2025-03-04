# Original array for all operations
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# 1. Reversing the Order of the Array
reversed_array = array[::-1]
print("Reversed Array:", reversed_array)

# 2. Removing Duplicates in an Array
unique_array = list(set(array))
print("Array without duplicates:", unique_array)

# 3. Array Partitioning
partition_size = 3
partitioned_array = [array[i:i + partition_size] for i in range(0, len(array), partition_size)]
print("Partitioned Array:", partitioned_array)

# 4. Finding the Kth Maximum Element in the Array
k_max = 3  # Example: Finding 3rd maximum
sorted_array_desc = sorted(array, reverse=True)
kth_maximum = sorted_array_desc[k_max - 1]
print(f"The {k_max}rd Maximum Element:", kth_maximum)

# 5. Finding the Kth Minimum Element in the Array
k_min = 3  # Example: Finding 3rd minimum
sorted_array_asc = sorted(array)
kth_minimum = sorted_array_asc[k_min - 1]
print(f"The {k_min}rd Minimum Element:", kth_minimum)
