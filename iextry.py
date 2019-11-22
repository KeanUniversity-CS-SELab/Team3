import pymysql, requests, json, re
from datetime import datetime
# read JSON file which is in the next parent folder
googl = requests.get('https://cloud.iexapis.com/v1/stock/googl/chart/1m?token=pk_c8a8370e394c49528e4c63007f10c7d1').json()
rfem = requests.get('https://cloud.iexapis.com/v1/stock/rfem/chart/1m?token=pk_c8a8370e394c49528e4c63007f10c7d1').json()
aple = requests.get('https://cloud.iexapis.com/v1/stock/aple/chart/1m?token=pk_c8a8370e394c49528e4c63007f10c7d1').json()
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
def getIEX(file, symb):
    cursor.execute("SELECT Date FROM "+symb+" ORDER BY DATE DESC LIMIT 1")
    record = cursor.fetchall()
    print(record[0][0])
    for i, item in enumerate(file):
        Date = validate_string(item.get("date", None))
        Date = datetime.strptime(Date, '%Y-%m-%d').date()
        print('here')
        if Date > record[0][0]:
            Open = item.get("open", None)
            Close = item.get("close", None)
            High = item.get("high", None)
            Low = item.get("low", None)
            Volume = item.get("volume", None)
            print(Date, type(Date))
            print(Open, type(Open))
            print(Close, type(Close))
            print(High, type(High))
            print(Low, type(Low))
            print(Volume, type(Volume))
            input('done')
            print(cursor.execute("INSERT INTO "+symb+" (Date, Open, Close, High, Low, Volume) VALUES (%s,%s,%s,%s,%s,%s)", (Date,Open,Close,High,Low,Volume)))

input('googl')
getIEX(googl, "googl")
print('success')
input('rfem')
print('success')
getIEX(rfem, 'rfem')
print('success')
input('aple')
getIEX(aple, 'appl')
con.commit()
con.close()
