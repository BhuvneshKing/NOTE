'''
A method for doubling the elements of an integer array is shown here. The referent passing changes the values of the array in the main program.
'''
def doubles(l):
    for i in range(0, len(l)):
        l[i] = 2 * l[i]


myList = [12, 20, 14, 4, 5, 44, 74]

doubles(myList)

print("values from array doubled: ")
for i in range(0, len(myList)):
    print(myList[i], end=' ')