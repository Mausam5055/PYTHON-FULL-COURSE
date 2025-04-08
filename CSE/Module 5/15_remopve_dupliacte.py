# Method 1: Using reverse iteration
def remove_duplicates_method1():
    a = [1, 1, 1, 3, 4, 5, 5, 5, 5, 7, 7, 7, 9, 9]
    for i in range(len(a)-1, 0, -1):
        if a[i] == a[i-1]:
            del a[i]
    print("Method 1 result:", a)

# Method 2: Using forward iteration with while loop
def remove_duplicates_method2():
    a = [1, 1, 1, 3, 4, 5, 5, 5, 5, 7, 7, 7, 9, 9]
    i = 0
    l = len(a) - 1
    while i < l:
        if a[i] == a[i+1]:
            del a[i+1]
            l -= 1
        else:
            i += 1
    print("Method 2 result:", a)

# Call both methods
remove_duplicates_method1()
remove_duplicates_method2()
