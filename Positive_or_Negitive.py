'''
A simple Python program that shows the functionality of an if-else statement.


'''
# Initializes a variable called num with the value taken by the user
num = int(input("Enter the value :-\n"))

# If the value of the variable num is less than 0, the string “number is negative” is output
if num < 0:
    print("number is negative")

# If the value of the variable num is 0, the string “0” is output
elif num == 0:
    print("0")

# Otherwise the string “number is positiv” is output
else:
    print("number is positiv")