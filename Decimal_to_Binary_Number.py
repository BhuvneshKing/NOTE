# Function header of the function decToBin() with the input parameter x
def decToBin(x):

# Returns the binary representation of the number x as an integer value. The bin() function normally returns a string in the following form: ‘0b11010’. Use the int() function to convert a number or string to an integer. Due to the [2:] notation the first two characters are ignored.    
    return int(bin(x)[2:])

# Calls the function decToBin() with the parameter 22 and prints the result
print(decToBin(22))

