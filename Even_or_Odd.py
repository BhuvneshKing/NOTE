'''

Check the number is even or odd :-
This Python program checks if a number is even or odd. The modulo operator performs an integer division and returns the remainder

'''
x = int(input("Enter a value for x: "))

if x % 2 == 0:
    print("Number " + str(x) + " is even")
else:
    print("Number " + str(x) + " is odd")
