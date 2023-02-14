n =  int(input("Enter the number:-\n"))

for i in range(0, n):
    for j in range(1, n - i):
        print(" ", end="")
    print("*", end="")
    for k in range(0, i):
        print("|", end="")
    for j in range(1, i):
        print("|", end="")
    if i > 0:
        print("*", end="")
    print()