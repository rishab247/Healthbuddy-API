from flask import Flask, jsonify, request, make_response, logging
import json
from main2 import *
import random as rd
import emotion as em
import Suggestionfunc as s
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from chatbot import Chat, register_call
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'msg': 'hello', }), 200


@app.route("/a")
def helloa():
    return jsonify({'msg': 'hello world', }), 200


chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Example.template"))


@app.route("/Bot", methods=['POST'])
def Bot():
    try:
        jsondata = request.get_data().decode("utf-8")
        jsondata = json.loads(jsondata)
        first_question = jsondata['msg']
        # print(chat.say(first_question,jsondata['id']))

        return jsonify({'msg': chat.say(first_question),"score":sentiment_analyzer_scores( jsondata['msg'])}), 200

    except Exception  as e:
        print(str(e))

        return jsonify({'msg': 'try Again', }), 401




def sentiment_analyzer_scores(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    return (  str(score["compound"]))

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

@app.route("/suggestiontest", methods=['GET'])
def suggestiontest():
    list1=list([["How was your day today?","Superb","Satisfied","Regular (As usual)","Worst"],["Turnout of the quarrel?", "I won the debate","compromised for peace","forgot the fight and started talking","fight led to complications in relationship"],["Anticipation of next morning?","Excited (big day)","As usual (regular stuffs)","Nothing much","Exhausted"],["Do I like and enjoy my current physical state?","Absolutely","Look to improve everyday","Do look for motivation","low self-esteem"]])
    i = rd.randint(0,len(list1)-1)
    print(list1[i])
    return jsonify({'msg': list1[i]}), 200


@app.route("/suggestion", methods=['POST'])
def suggestion ():
    try:
        jsondata = request.get_data().decode("utf-8")
        jsondata = json.loads(jsondata)
        result = s.activity_tracker(em.emotion(jsondata['score']))
        print(result)
        return jsonify( result), 200
    except Exception as e:
        return jsonify({'msg':str(e)}), 404


