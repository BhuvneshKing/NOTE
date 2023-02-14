'''
In Python there are also multiple branches represented by the elif statement

The if-conditions are evaluated in sequence until one of them is true. Then finally the code section belonging to this condition is executed and the multiple branching handling is finished. The else-part is only executed if none of the conditions is true.

'''
# Prompts the user to enter a number. This is stored in the variable firstNumber
firstNumber = input("Please enter first number: ")

# Prompts the user to enter a number. This is stored in the variable secondNumber
secondNumber = input("Please enter second number: ")

# If the value of the variable firstNumber is greater than the value of the variable secondNumber, the string “value_first_variable > value_second_variable” is output
if (firstNumber > secondNumber):
    print(firstNumber + " > " + secondNumber)

# If firstNumber is smaller than secondNumber, the string “value_first_variable < value_second_variable” is output
elif (firstNumber < secondNumber):
    print(firstNumber + " < " + secondNumber)

# Otherwise the string “value_first_variable = value_second_variable” is output    
else:
    print(firstNumber + " = " + secondNumber)