from random import choice
from time import sleep

small="qwertyuiopasdfghjklzxcvbnm"
cap="QWERTYUIOPASDFGHJKLZXCVBNM"
numbers="1234567890"
bajs="./!@#$%&*()_+"
password=""

password_length=input("welcome to the app.please give me your password length: ")
how_hard=input("how much do you want it complex? from 1 to 4 ? ")

if password_length.isdigit() and how_hard.isnumeric() and int(how_hard)<=4:
    if how_hard == "4":
        final_str = small + cap + numbers + bajs
    elif how_hard == "3":
        final_str = small + cap + numbers 
    elif how_hard == "2":
        final_str = small + cap
    else:
        final_str = small

    print("i am generating password ")

    for _ in range (3):
        print("*" , end=" " , flush=True)
        sleep(1)
        

    for i in range(int(password_length)):
        password+= choice(final_str)
    print(f"\nhere is your password = {password}")

    
else :
    print ("incorrect input")