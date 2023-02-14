'''
Swap two values with third variable

'''
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

print("Before swapping:\nX: " + str(x) + "\nY: " + str(y))

# swapping numbers
temp = x
x = y
y = temp

print("After swapping:\nX: " + str(x) + "\nY: " + str(y))