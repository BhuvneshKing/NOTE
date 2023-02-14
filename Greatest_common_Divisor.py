'''
The gcd of two numbers is the greatest common divisor of these numbers, that is the greatest number by which both numbers are divisible.
'''
"""                          RECURSIVE             """
def gcd(a, b):
    if a == 0:
      return b
    elif b == 0:
      return a
    elif a > b:
      return gcd(a - b, b)
    else:
      return gcd(a, b - a)


a, b = 200, 60

print("Greatest common divisor is: " + str(gcd(a, b)))