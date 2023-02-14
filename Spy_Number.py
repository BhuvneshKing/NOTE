'''

A number is known as a spy number if the sum of its digits is exactly equal to the product of its digits.

'''
def checkSpy(number):
    sum, mul = 0, 1

    while number > 0:
        rem = number % 10
        sum += rem
        mul *= rem
        number = int(number / 10)

    if sum == mul:
        return True
    else:
        return False


number = int(input("Enter a number to check for spy number: "))

if checkSpy(number) == True:
    print(str(number) + " is a spy number")
else:
    print(str(number) + " is not a spy number")