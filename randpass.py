import random

correctPassword = int(input())
wrongPasswords = []
password = ""
length = 4
chars = "1234567890"
run = True

while run:
    password = ""

    for i in range(length):
        password += random.choice(chars)

    if password not in wrongPasswords:
        if password != correctPassword:
            print(password)
            wrongPasswords.append(password)
        else:
            run = False
            break


print(password + " is correct")
