'''

The following program calculates the permutation and combination of 2 numbers.

'''
def fact(val):
    if val == 0 or val == 1:
        return 1
    else:
        return val * fact(val - 1)


n = int(input("Enter value of n : "))
r = int(input("Enter value of r : "))

combination = int(fact(n) / (fact(r) * fact(n - r)))
permutation = int(fact(n) / fact(n - r))

print("\nCombination : " + str(combination))
print("Permutation : " + str(permutation))