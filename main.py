from random import choice , shuffle
from time import sleep

default="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

password_length=input("welcome to the app.please give me your password length: ")
if password_length.isnumeric:
    print("i am generating password ")
    sleep(3)
    password=""
    for i in range(int(password_length)):
        password+= choice(default)
    print(f"here is your password = {password}")

    
else :
    print ("incorrect length")