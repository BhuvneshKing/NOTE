'''
The term ASCII (American Standard Code for Information Interchange) refers to a defined character encoding. It assigns certain codes to characters such as letters, digits and punctuation marks. The ASCII code is used to specify how the characters are displayed by electronic devices – such as PCs or smartphones. This is an important part of many programming operations.

'''
# Prompts the user to enter a character that will be treated as an integer value. The value is stored in the variable named character
character = input("Please enter character: ")

# The ord() function returns an integer representing the unicode character
asciiValue = ord(character)

# The chr() function returns the character that represents the specified unicode
originalValue = chr(asciiValue)

# Outputs the ASCII value of character by representing the variable asciiValue
print("ASCII value of the character " + repr(originalValue)
      + " is: " + repr(asciiValue))


