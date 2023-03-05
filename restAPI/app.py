from flask import Flask, request, jsonify, json

from database import database

app = Flask(__name__)

res = {'status': 'ok'}

@app.route('/healtz')
def healtz():
    return jsonify(res), 200

@app.route('/api/rating', methods = ['POST'])
def rating():
    rating_data = request.get_json()
    app.logger.info(rating_data)
    return jsonify(res), 200


@app.route('/api/stats', methods = ['GET'])
def stats():
    rating_data = request.get_json()
    app.logger.info(rating_data)
    return jsonify(res), 200


@app.route('/api/log', methods=['GET'])
def log(type=None):
    args = request.args
    print(args)
    if args == None:
        return jsonify({'status': 'wrong', 'message': 'Please provide type parameter to request'}), 404
    else:
        type = args.get('type')
        app.logger.info(type)
    return jsonify(res), 200

@app.route('/api/testConDataBase', methods=['GET','POST'])
def testConDataBase():
    con = database("172.28.0.19", "root", "EinZweiDrei", "pcss")
    con.execute("SELECT * FROM `odwiedziny`;")
    print(con.messages)
    json_message = json.dumps(con.messages)
    res = {'status': 'ok'}
    return jsonify(json_message)

if __name__ == '__main__':
    # connect = DataBase("172.28.0.19", "root", "EinZweiDrei", "PULSkwa_database")
    # connect.execute("SELECT * FROM `Tokens`;")

    #### TU ZMIEN ADRES ###
    app.run(debug=True, host="172.28.0.22")

#    app.run(debug=True)
