'''
A palindrome is a word that has the same meaning when read backwards as when read from the front. Examples of palindromes are: Anna, madam, level, racecar and many more.
Mathematics also knows palindromes. Here we talk about palindromes if the numbers do not change when the sequence of numbers is reversed, for example 22 or 141.

'''
rev = 0
x = int(input("Enter number to check palindrome or not: \n"))
temp = x


while x > 0:
    r = x % 10
    rev = rev * 10 + r
    x = x // 10

if temp == rev:
    print(str(temp) + " is palindrome number")
else:
    print(str(temp) + " is not palindrome number")