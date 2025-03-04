# --------DICTIONARY MERGE & UPDATE OPERATORS--------

# New operators | and |= allow for merging and updating dictionaries.


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}


# ---------MULTIPLE CONTEXT MANAGER--------

# You can now use multiple context managers in a single "with"
# statement more cleanly using the parenthesised context manager
with (

open('file1.txt') as f1,
open('file2.txt') as f2
):
    
# # Process files