'''
Here the product of the individual loop elements is output in a double nested loop.
'''

for i in range(3, 5):
    for j in range(1, 10):
        for k in range(1, 5):
            print(i * j * k, end=" ")
        print()
    print()