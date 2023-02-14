'''
The following code snippet calculates the average of 3 numbers. The average is rounded by different rounding methods.

'''
# Function header of the function roundDouble() with the input parameters value and decimalPoints
def roundDouble(value, decimalPoints):

# The pow() method calculates the power of a number by raising the first argument (10) to the second argument (decimalPoints)
    d = pow(10, decimalPoints)

# Returns the rounded value
    return round(value * d) / d

# Initializes the variables a, b and c with the values 11.54, 7.73 and 10.54
a = 11.54
b = 7.73
c = 10.54

# Calculates the average of variable a, b and c
avg = (a + b + c) / 3

# Outputs the 3 numbers and the average value (without rounding)
print("Average of " + repr(a) + ", " + repr(b) + " and " + repr(c) + " is: " + repr(avg))

# Outputs the mean value via the round() function. Since no decimal places were specified, the number is rounded to 0 decimal places. In addition, the rounded value is output with 2 decimal places via the roundDouble() function
print("Rounded value:\n" + repr(round(avg)) + "\n" + repr(roundDouble(avg, 2)) + "\n")
