n=int(input("Enter the number:-\n"))
a, b, c1, c2 = n, (n+2), 0, 0

'''
In the following program, a nested loop is used to check how often the loops are run through.
'''

for i in range(20, a, -1):
    c1 = c1 + 1
    for j in range(0, b):
        c2 = c2 + 1
        if i == j:
            print("How many times the loops are run?")
            print(
                "first loop: "
                + str(c1)
                + "\nsecond loop: "
                + str(c2)
                + " ("
                + str(c1)
                + " * "
                + str(b)
                + ")"
                )