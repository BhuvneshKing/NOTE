'''
A number is called a neon number if the sum of the digits of its square is equal to the number itself.

'''
sum = 0
print("Enter the number to check:\n")
num = int(input())
square = num * num

while (square != 0):
    digit = square % 10
    sum = sum + digit
    square = square // 10

if (num == sum):
    print(str(num) + " is a neon number.")
else:
    print(str(num) + " is not a neon number.")