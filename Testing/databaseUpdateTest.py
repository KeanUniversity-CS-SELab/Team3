"""
Keith Estrella
Python Test Program to test if the MySQL database has been updated daily
"""
import os
import mysql.connector
from os import path

#Creates a text file called "today" that pulls and saves the entries on the database to a text file stored locally
def createToday():
    connec = mysql.connector.connect(user='tester1', password='tester1@Team3', host='18.218.249.217',port='3306',database='iexcloud') #Connects to the MySQL database
    cursor = connec.cursor() #Creates a cursor to search the database

    query = ("SELECT * FROM iexcloud.master") #Search terms
    cursor.execute(query) #Cursor performs the query given
    with open("today.txt", "w", newline='\n') as f: #Writes the results to a text file named "today"
        for row in cursor:
            print(row, file=f)
    connec.close() #Closes the connection

#Reads in both "today" and "yesterday" text files in order to compare them
def compareDays():
    with open("today.txt") as f:
        listA = f.read().splitlines(0)
    with open("yesterday.txt") as g:
        listB = g.read().splitlines(0)
    return list(set(listA) ^ set(listB))

#Main method
def main():
    if path.exists("today.txt"): #Checks if there is an existing "today" file
        if path.exists("yesterday.txt"): #Checks if there is an existing "yesterday" file
            os.remove("yesterday.txt") #If there is an existing "yesterday" file, delete it
        os.rename("today.txt","yesterday.txt") #If there is an existing "today" file, rename it to "yesterday"
        createToday() #Calls to create a new "today" file
        compared = compareDays() #Calls compareDays which returns a list containing entries that were added or removed or is completely empty
        if not compared: #Checks to see if the list returned is empty
            print("Both today and yesterday's values are the same") #The list was empty meaning all entries on both lists were the same
        else:
            print("These values are not found in both lists") #The list wasn't empty which means the database was updated
            print(compared) #Prints the list in the Kernel
    else:
        createToday() #Since there wasn't a "today" file, make one
        print("Check back tomorrow") #Because there wasn't a "today" file, there can't be a "yesterday" file unless "today" was manually deleted
        


if __name__=="__main__": #Invokes a main method
    main()
