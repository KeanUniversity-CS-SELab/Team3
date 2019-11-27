import pymysql, requests, json, re
from datetime import datetime
#json_data=open(file).read()
#json_obj = json.loads(json_data)
# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        elif type(val) is bytes:
            result = 0
            for b in val:
                result = result * 256 + int(b)
            return result
        else:
            return val
# connect to MySQL
con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'IEXCLOUD')
cursor = con.cursor()
# parse json data to SQL insert
notes = open('iexnotes.txt', 'w')
def getIEX(symb):
    file = requests.get('https://cloud.iexapis.com/v1/stock/'+symb+'/chart/1m?token=pk_c8a8370e394c49528e4c63007f10c7d1').json()
    cursor.execute("SELECT Date FROM master where symbol =%s ORDER BY DATE DESC LIMIT 1",(symb))
    record = cursor.fetchall()
    notes.write(str(record[0][0]))
    for i, item in enumerate(file):
        Date = validate_string(item.get("date", None))
        Date = datetime.strptime(Date, '%Y-%m-%d').date()
        if Date > record[0][0]:
            Open = item.get("open", None)
            Close = item.get("close", None)
            High = item.get("high", None)
            Low = item.get("low", None)
            Volume = item.get("volume", None)
            cursor.execute("INSERT INTO master (Date, Open, Close, High, Low, Volume, symbol) VALUES (%s,%s,%s,%s,%s,%s,%s)", (Date,Open,Close,High,Low,Volume,symb))

getIEX("googl")
notes.write('google success')
getIEX('rfem')
notes.write('rfem success')
getIEX('aple')
notes.write('aple success \n')
print('done')
notes.close()
con.commit()
con.close()
