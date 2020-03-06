from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'msg': 'Fuck Off', }), 401


@app.route("/Askme", methods=['POST'])
def Askme():
    data = request.get_data().decode("utf-8")
    data = json.loads(data)
    print(data)

    return jsonify({'msg': 'Fuck Off! Again', }), 401

