# Function header of the function decToHex() with the input parameter x
def decToHex(x):

# Returns the hexadecimal representation of the number x. The hex() function normally returns a string in the following form: ‘0x….’. The function .split() removes the substring 0x from the string    
    return hex(x).split('x')[-1]

# Calls the function decToHex() with the parameter 140 and prints the result
print(decToHex(140))
