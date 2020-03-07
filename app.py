from flask import Flask, jsonify, request, make_response, logging
import json
from main2 import *




app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'msg': 'hello', }), 200


@app.route("/a")
def helloa():
    return jsonify({'msg': 'hello world', }), 200




@app.route("/Askme", methods=['POST'])
def Askme():
    try:
        jsondata = request.get_data().decode("utf-8")
        jsondata = json.loads(jsondata)
        print(main_call(jsondata['msg']))

        return jsonify({'msg': (main_call(jsondata['msg'])) }), 200

    except Exception  as e:
        print(str(e))

        return jsonify({'msg': 'try Again', }), 401

