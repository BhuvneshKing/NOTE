'''
When an if-else statement is executed in the body of another if-else statement, it is called nested.

'''
# Initializes the variable number with the value
number = int(input("Enter the NUmber:-\n"))

# If the value of number is less than or equal to 100
if (number <= 100):

# If the value of number is less than 50, print the string “Value is smaller than 50”    
    if (number < 50):
        print("Value is smaller than 50")

# If the value of number is less than 50, print the string “Value is 50”
    elif (number == 50):
        print("Value is 50")

# Otherwise the string “Value is between 51 und 100“ is output        
    else:
        print("Value is between 51 und 100")

# If the value of number is greater than 100 output the following string “Value is greater than 100”        
else:
    print("Value is greater than 100")