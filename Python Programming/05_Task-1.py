# WAP python program for the following:
# Read the user input to enter a temperature in Celsius.
# The program should print a message based on the temperature:

# • If the temperature is less than -273.15, print that “The temperature is invalid” 
# because it is
# below absolute zero.
# • If it is exactly -273.15, print that “The temperature is absolute 0”.
# • If the temperature is between -273.15 and 0, print that “The temperature is below freezing”.
# • If it is 0, print that “The temperature is at the freezing point”.
# • If it is between 0 and 100, print that “The temperature is in the normal range”.
# • If it is 100, print that “The temperature is at the boiling point”.
# • If it is above 100, print that ”The temperature is above the boiling point”.

temp = float(input("Enter the temperature in Celsius: "))
if temp < -273.15:
    print("The temperature is invalid because it is below absolute zero.")
elif temp == -273.15:
    print("The temperature is absolute 0.")
elif temp < 0:
    print("The temperature is below freezing.")
elif temp == 0:
    print("The temperature is at the freezing point.")
elif temp < 100:
    print("The temperature is in the normal range.")
elif temp == 100:
    print("The temperature is at the boiling point.")
elif temp > 100:
    print("The temperature is above the boiling point.")
