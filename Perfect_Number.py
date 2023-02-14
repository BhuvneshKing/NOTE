'''

A number is called perfect if the number is equal to the sum of its divisors (the number itself is not considered a divisor in this case).

'''
sum = 0
number = int(input("Enter a number to check for perfect: \n"))

for i in range(1, number):
    if number % i == 0:
        sum = sum + i

if sum == number:
    print(str(number) + " is a perfect number")
else:
    print(str(number) + " is not a perfect number")