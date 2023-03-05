from flask import Flask, request, jsonify, json, render_template
from database import database
from mimetype import accept

app = Flask(__name__)

res = {'status': 'ok'}

@app.route('/api/testConDataBase', methods=['GET','POST'])
def testConDataBase():
    con = database("172.28.0.19", "root", "EinZweiDrei", "pcss")
    con.execute("SELECT * FROM `odwiedziny`;")
    print(con.messages)
    print("Adres: " + request.remote_addr)
    json_message = json.dumps(con.messages)
    res = {'status': 'ok'}
    return jsonify(json_message)

@app.route('/')
#@accept('text/html')
def home():
    con = database("172.28.0.19", "root", "EinZweiDrei", "pcss")
    con.execute("SELECT * FROM `odwiedziny`;")
    allips = con.getResults()
    return render_template('./website/index.html', your_list=allips)

if __name__ == '__main__':
    app.run()
