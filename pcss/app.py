from flask import Flask, request, jsonify, json, render_template
from database import database
from datetime import datetime
from mimetype import accept
from misc import *
from array import *

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
#@accept('text/html')
def home():
    con = database("172.28.0.19", "root", "EinZweiDrei", "pcss")

    now = datetime.now()
    dt_string = now.strftime("%Y.%m.%d")
    hm_string = now.strftime("%H:%M")
    print("date and time =", dt_string)

    data = (dt_string, hm_string, request.remote_addr)
    con.execute("INSERT INTO `odwiedziny`(`data`, `godzina`, `adres`) VALUES (%s,%s, %s);", data)

    con.queryAll("SELECT * FROM `odwiedziny`;", None)

    iplist = con.getResults()

    render = []
    for x in iplist[0]:
        render.append(TupleToArray(x))
        print(x)

    con.clearResult()
    con.clearMessages()
    return render_template("index.html", ip_list=render)

if __name__ == '__main__':
    app.run(debug=True)
