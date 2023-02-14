'''
This Python program converts Celsius to Fahrenheit. First, the user is asked to enter a temperature in Celsius of type float. After that the value is converted to Fahrenheit.

The formula for the conversion is:
fahrenheit = celsius * 1,8 +32

'''
c = float(input("Please enter temperature in celsius: "))

f = c * 1.8 + 32

print("Temperature in fahrenheit: " + str(f))