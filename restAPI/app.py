from flask import Flask, request, jsonify, json, render_template
from database import database
from datetime import datetime
from mimetype import accept
from misc import *
from array import *

app = Flask(__name__)

res = {'status': 'ok'}

@app.route('/api/testConDataBase', methods=['GET','POST'])
def testConDataBase():
    con = database("172.28.0.19", "root", "EinZweiDrei", "pcss")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    print("date and time =", dt_string)
    con.execute("SELECT * FROM `odwiedziny`;")
    print(con.messages)
    print("Adres: " + request.remote_addr)
    json_message = json.dumps(con.messages)
    res = {'status': 'ok'}
    return jsonify(json_message)

@app.route('/', methods=['GET','POST'])
#@accept('text/html')
def home():
    con = database("172.28.0.19", "root", "EinZweiDrei", "pcss")

    now = datetime.now()
    dt_string = now.strftime("%Y.%m.%d") #TODO godziny
    print("date and time =", dt_string)

    data = (dt_string, request.remote_addr)
    con.execute("INSERT INTO `odwiedziny`(`data`, `adres`) VALUES (%s,%s);", data)

    con.execute("SELECT * FROM `odwiedziny`;", None)


    iplist = con.getResults()

    print(len(iplist))
    #print(iplist[0])
    render = []
    for x in iplist[0]:
        render.append(TupleToArray(x))
        print(x)
    #iplist = TupleToArray(iplist)
    #print(iplist)

    con.clearResult()
    con.clearMessages()
    return render_template("index.html", ip_list=render)
   #

if __name__ == '__main__':

    app.run(debug=True)
