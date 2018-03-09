import sys 
from sys import exit
import sqlite3
from sqlite3 import Error
import time
import random


conn = sqlite3.connect('data2.db')
c = conn.cursor()


print("Welcome to your Loyalty Point Program !")
answer = input("Are you 'signing up', or 'viewing': ")

while True:
    if answer == "signing up":
        fname =  input("What is your first name: ")
        lname = input("What is your last name: ")
        points = random.randrange(0,10000)
        print("..."*15)
        time.sleep(3)
        print (f" {fname} {lname}, Welcome ! ")
        print(f"For signing up, you get {points} points! ")
        time.sleep(2)
        choose = input("Would you like to earn extra points? y/n ? ")
        if choose =='y':
            print("We just need to get a little more information from you. ")
            time.sleep(2)
            cell = input("What is your phone number: ")
            email = input("What is your email address: ")
            pw = input("Please enter a 4 digit pin: ")
            points = points + 50
            print("---" * 15)
            print(f"Thank you, you have {points} points !")
            break


        elif choose == 'n':
            print("Okay. Thank you for the information you have provided.")
            print("These are your points ... ")
            time.sleep(2)
            print(points)
            break
        else:
            print("TRY AGAIN LATER ! ")
            sys.exit()
    elif answer == "viewing":
        email = input("What is your email adress? ")
        pin = input("What is your pin?")
        time.sleep(2)
            
        c.execute("SELECT * FROM Rewards_Program")
        print(c.fetchall())
        #data = (c.fetchall)
        #print(data)


        sys.exit()

    else:
        print("Okay, goodbye !")


c.execute('CREATE TABLE IF NOT EXISTS Rewards_Program (first TEXT, last TEXT, email TEXT, points REAL)')

def dynamic_data_entry():
    fname =  input("What is your first name: ")
    lname = input("What is your last name: ")
    points = random.randrange(0,10000)
    email = input("What is your email address: ")
    
    c.execute("INSERT INTO Rewards_Program (first, last, email, points) VALUES (?, ?, ?, ?)",
              (fname, lname, email,points))
    conn.commit()

for i in range(1):
    dynamic_data_entry()
time.sleep(1)

time.sleep(1)

c.close()
conn.close()