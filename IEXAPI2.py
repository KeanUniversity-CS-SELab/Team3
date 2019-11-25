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
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


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

app.run()
