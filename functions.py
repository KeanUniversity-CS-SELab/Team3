import pymysql, requests, json, re
from datetime import datetime
from datetime import timedelta

print("Start date is 11-01-2019")
print("End date is 12-07-2019" + "\n")
temp =[]
#retrieve data, columns a list list of column names, sDate is the date to start the search and dure is how far back the user wants to retrieve
def getData(startDate,endDate, columns=['*'], symbolS=["googl","aple","rfem"], dure=1):
   con = pymysql.connect(host = '18.219.69.95',user = 'tester1',passwd = 'tester1@Team3',db = 'iexcloud')
   cursor = con.cursor()
   search = " ,".join(columns)
   dure = dure * len(symbolS)
   symb = "\'"+symbolS[0]+"\'"
   
   for i in symbolS:
      if i != symbolS[0]:
         symb = symb+" OR symbol =\'"+i+"\'"
         
   query ="SELECT "+search+" FROM master where (symbol = "+symb+") AND (DATE >='"+startDate+"') AND (DATE <='"+endDate+"')"
   cursor.execute(query)
   record = cursor.fetchall()
   
   if len(record) == 0:
      return 'failed'

   listOfLists = []
   for y in columns:
      mylist = []
      for x in record:
         mylist.append(record[record.index(x)][columns.index(y)])
      listOfLists.append(mylist)
            
   return listOfLists
 


def change(startDate,endDate,symb):
   recordList = getData(startDate,endDate,columns=['Close'], dure=30, symbolS=symb)
   print("Total number of records: " + str(len(unlist(recordList))))
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])
      change.append(mylist)
   print("Available records: " + str(recordList) + "\n")
   return change


def changePercent(startDate,endDate,symb):
   recordList = getData(startDate,endDate,columns=['Close'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(((recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])/recordList[recordList.index(x)][x.index(y)])*100)
      change.append(mylist)
   return change

def changeOverTime(startDate,endDate,symb):
   recordList = getData(startDate,endDate,columns=['Close'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(((recordList[recordList.index(x)][x.index(y)+1]-recordList[0][0])/recordList[0][0])*100)
      change.append(mylist)
   return(change)

def volumeChange(startDate,endDate,symb):
   recordList = getData(startDate,endDate,columns=['Volume'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])
      change.append(mylist)
   return change


def volumeChangePercent(startDate,endDate,symb):
   recordList = getData(startDate,endDate,columns=['Volume'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(((recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])/recordList[recordList.index(x)][x.index(y)])*100)
      change.append(mylist)
   return change

def volumeChangeOverTime(startDate,endDate,symb):
   recordList = getData(startDate,endDate,columns=['Volume'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(((recordList[recordList.index(x)][x.index(y)+1]-recordList[0][0])/recordList[0][0])*100)
      change.append(mylist)
   return change


def unlist(x):
   for i in x:
      if type(i)==list:
         unlist(i)
      else:
         temp.append(i)
   return temp

def minPrice(startDate,endDate, symb):
   recordList = getData(startDate,endDate,columns=['Close'], symbolS=symb)
   output = unlist(recordList)
   return min(output)


def maxPrice(startDate,endDate, symb):
   recordList = getData(startDate,endDate,columns=['Close'], symbolS=symb)
   output = unlist(recordList)
   return max(output)


def avgPrice(startDate,endDate, symb): 
   recordList = getData(startDate,endDate,columns=['Close'], symbolS=symb)
   output = unlist(recordList)
   return sum(output)/len(output)  

change1=change('2019-11-01','2019-12-07', ["googl"])
change2=changePercent('2019-11-01','2019-12-07', ["googl"])
change3=changeOverTime('2019-11-01','2019-12-07', ["googl"])



volume1=volumeChange('2019-11-01','2019-12-07', ["googl"])
volume2=volumeChangePercent('2019-11-01','2019-12-07', ["googl"])
volume3=volumeChangeOverTime('2019-11-01','2019-12-07', ["googl"])


min_value=minPrice('2019-11-01','2019-12-07', ["googl"])
max_value=maxPrice('2019-11-01','2019-12-07', ["googl"])
avg_value=avgPrice('2019-11-01','2019-12-07', ["googl"])


print("Price change between each day: " + str(change1) + "\n")
print("Price change percent each day: " + str(change2) + "\n")
print("Price change over time each day: " + str(change3) + "\n")
print("Volume change between each day: " + str(volume1) + "\n")
print("Volume change percent each day: " + str(volume2) + "\n")
print("Volume change over time each day: " + str(volume3) + "\n")
print("Min price: " + str(min_value) + "\n")
print("Max price: " + str(max_value) + "\n")
print("Avg price: " + str(avg_value) + "\n")
