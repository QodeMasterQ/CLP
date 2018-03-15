import sqlite3
from sqlite3 import Error
import time
import random

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






conn = sqlite3.connect('tuto.db')
c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS Rewards_Program (first TEXT, last TEXT, email TEXT, points REAL)')

def dynamic_data_entry():
    c.execute("INSERT INTO Rewards_Program (first, last, email, points) VALUES (?, ?, ?, ?)",
              (fname, lname, email,points))
    conn.commit()




for i in range(1):
    dynamic_data_entry()
time.sleep(1)

c.close()
conn.close()
