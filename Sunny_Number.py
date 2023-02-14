'''
A number is called a sunny number if the number next to the given number is a perfect square.

'''
import math

def perfectSqaure(n): 
    square_root = math.sqrt(n)
    return((square_root - math.floor(square_root)) == 0);      


def isSunnyNumber(n):
    if (perfectSqaure(n + 1)):  
        print(str(n) + " is a sunny number!")
    else:
        print(str(n) +  " is not a sunny number!")

print("Enter a number to check for sunny number:") 
sunnyNumber = int(input()) 

isSunnyNumber(sunnyNumber)