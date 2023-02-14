'''
The user is first prompted to enter a radius. Then the circumference and the area of the circle are calculated, rounded and output on the screen

'''
# Import the math module to access the mathematical functions and numbers, in this case the number PI
import math

# Prompts the user to enter a radius as an integer value. The value is stored in the variable named r
r = int(input("Please enter radius: "))

# Calculates the circumference of the circle with the formula 2 * math.pi * r. The number PI can be retrieved via the math module. The result of this calculation is stored in the variable circumference
circumference = 2 * math.pi * r

# Calculates the circular area of the circle with the formula math.pi * pow(r, 2). The pow() function calculates the power of a number by raising the first argument to the second argument. The result of this calculation is stored in the variable area
area = math.pi * pow(r, 2)

# Outputs the circumference rounded to 2 decimal places
print("Circumference: " + repr(round(circumference, 2)))

# Outputs the circular area rounded to 2 decimal places
print("Circular Area: " + repr(round(area, 2)))

