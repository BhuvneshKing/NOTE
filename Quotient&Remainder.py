'''

In division with remainder, the first number is not exactly divisible by the second number. This is because the divisor (the second number) is not a divisor of the dividend (the first number). The dividend is not a multiple of the divisor. Therefore, a remainder remains, which is smaller than the divisor, by which it is divided.


'''
dividend = int(input("Please enter dividend: "))
divisor = int(input("Please enter divisor: "))

quotient = dividend / divisor
remainder = dividend % divisor

print("Quotient is: " + repr(quotient))
print("Remainder is: " + repr(remainder))