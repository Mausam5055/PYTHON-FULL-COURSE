def list_square(list):
    new_list = [x**2 for x in list]
    return new_list

list = list(map(int, input("Enter elements of list separated by spaces: ").split()))
print("The list with square of its items is: ", list_square(list))