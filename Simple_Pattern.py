# for loop with the range 0 to 9 and a counter variable called i
for i in range(0, 9):

# A second for loop, nested in the first one with the range 0 to i and the counter variable j
    for j in range(0, i):

# The counter variable i of the first for loop is output.
# In the first loop pass only a 1 is output, because the second loop has the range 0 – 1. On the second pass, the counter variable of the first loop (i) is 2. Consequently, the second for loop has the range 0 – 2, which is why the number 2, 2 times is output. The number 3, 3 times and so on
        print(i, end="")

# Each time the second for loop is processed, the print() method is called to print a new line
    print()