import pymysql, requests, json, re
from datetime import datetime
from datetime import timedelta


#retrieve data, columns a list list of column names, sDate is the date to start the search and dure is how far back the user wants to retrieve
def getData(sDate=datetime.now().date(), columns=['*'], symbolS=["googl","aple","rfem"], dure=1):
   con = pymysql.connect(host = '18.218.249.217',user = 'tester1',passwd = 'tester1@Team3',db = 'iexcloud')
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
 
recordList = getData(columns=['Close','Volume'], dure=30, symbolS=['googl'])
change = []
for x in recordList:
   mylist =[]
   for y in x:
      if x.index(y) != len(x)-1:
         mylist.append(recordList[recordList.index(x)][x.index(y)+1]-recordList[recordList.index(x)][x.index(y)])
   change.append(mylist)
print(change)
