# for loop with the range 1 to 9 and a counter variable called i
for i in range(1, 9):

#  A second for loop, nested in the first one with the range 9 to i and the counter variable j. j is decremented by 1 in each loop pass   
    for j in range(9, i, -1):

# The counter variable i of the first for loop is output
        print(i, end="")

# Each time the second for loop is processed, the print() method is called to print a new line       
    print()
