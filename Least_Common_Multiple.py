'''
The least common multiple of two integers a and b is the smallest number that is both an integer multiple of a and also an integer multiple of b.
'''
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def lcm(a, b):
    return a * b / gcd(a, b)


a, b = 20, 8

print("Least common multiple is: " + str(lcm(a, b)))