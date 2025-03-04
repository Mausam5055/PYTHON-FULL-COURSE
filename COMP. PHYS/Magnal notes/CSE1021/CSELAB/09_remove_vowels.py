def remove_vowels(s) :
    s_new = ""
    vowels = "aeiouAEIOU"
    for i in s:
        if i not in vowels: #
            s_new = s_new+i
    print(s_new)

s = input("Enter the string to remove the the vowels : ")
remove_vowels(s)