'''
The following Python code example represents a simple login process. The user is prompted to enter his username and password. Subsequently, the user entries are checked. If they match the stored data, the user receives the message “successfully logged in”.
'''
def checkUserInput(username, password):
    name, pw = "user", "123456"

    if name == username and pw == password:
        return True
    else:
        return False


username = input("Enter username: ")
password = input("Enter password: ")

if checkUserInput(username, password):
    print("Successfully logged in")
else:
    print("Wrong username or password")