import pymysql, requests, json, re
from datetime import datetime
from datetime import timedelta

temp =[]
#retrieve data, columns a list list of column names, sDate is the date to start the search and dure is how far back the user wants to retrieve
def getData(sDate=datetime.now().date(), columns=['*'], symbolS=["googl","aple","rfem"], dure=1):
   con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'iex_cloud')
   cursor = con.cursor()
   search = " ,".join(columns)
   dure = dure * len(symbolS)
   symb = "\'"+symbolS[0]+"\'"
   
   for i in symbolS:
      if i != symbolS[0]:
         symb = symb+" OR symbol =\'"+i+"\'"
         
   query ="SELECT "+search+" FROM master where (symbol = "+symb+") AND (DATE <='"+sDate.strftime('%Y-%m-%d')+"') ORDER BY DATE DESC LIMIT "+str(dure)
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
 


def change(symb):
   recordList = getData(columns=['Close'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])
      change.append(mylist)
   return change


def changePercent(symb):
   recordList = getData(columns=['Close'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(((recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])/recordList[recordList.index(x)][x.index(y)])*100)
      change.append(mylist)
   return change

def changeOverTime(symb):
   recordList = getData(columns=['Close'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(((recordList[recordList.index(x)][x.index(y)+1]-recordList[0][0])/recordList[0][0])*100)
      change.append(mylist)
   return(change)

def volumeChange(symb):
   recordList = getData(columns=['Volume'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])
      change.append(mylist)
   return change


def volumeChangePercent(symb):
   recordList = getData(columns=['Volume'], dure=30, symbolS=symb)
   change = []
   for x in recordList:
      mylist =[]
      for y in x:
         if x.index(y) != len(x)-1:
            mylist.append(((recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])/recordList[recordList.index(x)][x.index(y)])*100)
      change.append(mylist)
   return change

def volumeChangeOverTime(symb):
   recordList = getData(columns=['Volume'], dure=30, symbolS=symb)
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

def minPrice(range, symb):
   recordList = getData(columns=['Close'], dure=range, symbolS=symb)
   output = unlist(recordList)
   return min(output)


def maxPrice(range, symb):
   recordList = getData(columns=['Close'], dure=range, symbolS=symb)
   output = unlist(recordList)
   return max(output)


def avgPrice(range, symb): 
   recordList = getData(columns=['Close'], dure=range, symbolS=symb)
   output = unlist(recordList)
   return sum(output)/len(output)  

change1=change(["googl","aple","rfem"])
change2=changePercent(["googl","aple","rfem"])
change3=changeOverTime(["googl","aple","rfem"])



volume1=volumeChange(["googl","aple","rfem"])
volume2=volumeChangePercent(["googl","aple","rfem"])
volume3=volumeChangeOverTime(["googl","aple","rfem"])


min_value=minPrice(range=30, symb=["googl","aple","rfem"])
max_value=maxPrice(range=30, symb=["googl","aple","rfem"])
avg_value=avgPrice(range=30, symb=["googl","aple","rfem"])

print (min_value, max_value, avg_value)