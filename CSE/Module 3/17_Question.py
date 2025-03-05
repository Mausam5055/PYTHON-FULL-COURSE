#write a function using python that accepts a 2 digit number as a 
# parameter and return text in words(advanced)


num = int(input("Enter a two-digit number: "))

def two_digit_to_words(num):
    if num < 10 or num > 99:
        return "Please enter a two-digit number"

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if 10 <= num < 20:
        return teens[num - 10]
    else:
        return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")


print("In words:", two_digit_to_words(num))


# # Example usage
# print(two_digit_to_words(42))  # Output: "Forty Two"
# print(two_digit_to_words(10))  # Output: "Ten"