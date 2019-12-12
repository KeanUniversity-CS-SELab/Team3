import flask, pymysql
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<!-- Font Awesome -->
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
<!-- Bootstrap core CSS -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
<!-- Material Design Bootstrap -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.11/css/mdb.min.css" rel="stylesheet">
<!-- JQuery -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
<script>alert("API CREATION SUCCESSFUL");</script>
<div class="container m-auto mt-3">
<h1>GOOGL, RFEM, AND APLE COMPANY INFORMATION</h1>
<p><a href="http://127.0.0.1/SoftEng/home.php"><button class="btn btn-info">Go to Graphic User Interface</button></a><p>
<p><a href="http://127.0.0.1:5000/api/v1/resources/company/all"><button class="btn btn-info">Check it out</button></a></p> 
<div>For our Restful api:
<ul>
<li>http://127.0.0.1:5000/api/v1/resources/company/all: show all company info</li>
<li>parameters are symbol, employees and isstype</li>
<li>the symbols are REFM, APLE, AND GOOGL</li>
<li>To find the different isstypes and employees use the company/all link</li>
<li>To find thirty day records use /api/v1/resources?symbol (symbols are aple,googl,rfem) or add /all for all symbols</li>
</ul></div>
<div>
<button class="btn"onclick="tog()"><h2>List of possible URLS:
</h2></button>
<ul id="list" class="list" style="display:none;">
	<li><a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company/all">http://127.0.0.1:5000/api/v1/resources/company/all</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company?symbol=GOOGL">http://127.0.0.1:5000/api/v1/resources/company?symbol=GOOGL</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company?symbol=REFM">http://127.0.0.1:5000/api/v1/resources/company?symbol=REFM</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company?symbol=APLE">http://127.0.0.1:5000/api/v1/resources/company?symbol=APLE</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company?employees=0">http://127.0.0.1:5000/api/v1/resources/company?employees=0</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company?employees=62">http://127.0.0.1:5000/api/v1/resources/company?employees=62</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company?employees=98771">http://127.0.0.1:5000/api/v1/resources/company?employees=98771</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company?isstype=cs">http://127.0.0.1:5000/api/v1/resources/company?isstype=cs</a></li>
	<li><a href="http://127.0.0.1:5000/api/v1/resources/company?isstype=cs">http://127.0.0.1:5000/api/v1/resources/company?isstype=et</a></li>
		<li><a href="http://127.0.0.1:5000/api/v1/resources/all">http://127.0.0.1:5000/api/v1/resources/all</a></li>
		<li><a href="http://127.0.0.1:5000/api/v1/resources?symbol=googl">http://127.0.0.1:5000/api/v1/resources?symbol=googl</a></li>
		<li><a href="http://127.0.0.1:5000/api/v1/resources?symbol=rfem">http://127.0.0.1:5000/api/v1/resources?symbol=rfem</a></li>
		</a></li>
		<li><a href="http://127.0.0.1:5000/api/v1/resources?symbol=aple">http://127.0.0.1:5000/api/v1/resources?symbol=aple</a></li>
</ul>
</div></div>
<script>
function tog(){
var show = document.getElementById("list").style.display
if (show == "none"){
	document.getElementById("list").style.display="block";
}
else{
 document.getElementById("list").style.display="none";
}
}
</script>
<!-- JQuery -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js" type="text/javascript"></script>
<script src="https://cdn.datatables.net/1.10.20/js/dataTables.bootstrap4.min.js" type="text/javascript"></script>
<!-- Bootstrap tooltips -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script>
<!-- Bootstrap core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
<!-- MDB core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.11/js/mdb.min.js"></script>
<script src="https://kit.fontawesome.com/d99fb3df37.js" crossorigin="anonymous"></script>'''


@app.route('/api/v1/resources/company/all', methods=['GET'])
def api_all():
    con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'IEXCLOUD')
    cur = con.cursor()
    cur.execute('SELECT * FROM company;')
    results =cur.fetchall()
    collist = ['Symbol','companyName','exchange','industry','website','description','CEO','securityName','issueType','sector','employees','address','address2','state','city','zip','country','phone']
    listdict = []
    for i in results:
        listdict.append(dict(zip(collist,i)))
            
    return jsonify(listdict)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/company', methods=['GET'])
def api_filter():
    symb = request.args.get('symbol')
    emp = request.args.get('employees')
    iss = request.args.get('isstype')

    query = "SELECT * FROM company WHERE"
    to_filter = []

    if symb:
        query += ' symbol=%s AND'
        to_filter.append(symb)
    if emp:
        query += ' employees=%s AND'
        to_filter.append(emp)
    if iss:
        query += ' issueType=%s AND'
        to_filter.append(iss)
    if not (symb or emp or iss):
        return page_not_found(404)

    query = query[:-4] + ';'

    con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'IEXCLOUD')
    cur = con.cursor()
    cur.execute(query,tuple(to_filter))
    results = cur.fetchall()
    collist = ['Symbol','companyName','exchange','industry','website','description','CEO','securityName','issueType','sector','employees','address','address2','state','city','zip','country','phone']
    listdict = []
    for i in results:
        listdict.append(dict(zip(collist,i)))
            
    return jsonify(listdict)
@app.route('/api/v1/resources/all', methods=['GET'])
def api_master():
    
    query = "SELECT * FROM master ORDER BY DATE DESC LIMIT 30;"
    con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'IEXCLOUD')
    cur = con.cursor()
    cur.execute(query)
    results = cur.fetchall()
    collist = ['Date','Volume','Open','Close','High','Low','symbol']
    listdict = []
    for i in results:
        listdict.append(dict(zip(collist,i)))
            
    return jsonify(listdict)
@app.route('/api/v1/resources', methods=['GET'])
def api_mastersmb():
    symb = request.args.get('symbol')
    query = "SELECT * FROM master WHERE symbol =%s ORDER BY DATE DESC LIMIT 30;"
    to_filter = []
    to_filter.append(symb)
    if not (symb):
       return page_not_found(404)

    con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'IEXCLOUD')
    cur = con.cursor()
    cur.execute(query,tuple(to_filter))
    results = cur.fetchall()
    collist = ['Date','Volume','Open','Close','High','Low','symbol']
    listdict = []
    for i in results:
        listdict.append(dict(zip(collist,i)))
            
    return jsonify(listdict)
app.run()
