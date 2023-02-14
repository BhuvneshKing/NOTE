"""           ITERATIVE                  """
def crossSum(n):
    total = 0
    while 0 != n:
        total = int(total + (n % 10))
        n = n / 10

    return total


print(crossSum(123))

"""           RECURSIVE                  """
def crossSum(n):
    return n if n <= 9 else (n % 10) + int(crossSum(n / 10))


print(crossSum(555))