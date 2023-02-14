# Function header of the function decToOct() with the input parameter x
def decToOct(x):
    
# Returns the octal representation of the number x. The oct() function normally returns a string in the following form: ‘0o….’. The function .split() removes the substring 0o from the string
    return oct(x).split('o')[-1]

# Calls the function decToOct() with the parameter 125 and prints the result
print(decToOct(125))

