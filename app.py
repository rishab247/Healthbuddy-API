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


@app.route("/question", methods=['POST'])
def question():
    # f = open('question.json', )
    # data = json.load(f)
    # print(data)
    # lis = rd.sample(dict(data).keys()   ,5)
    # jdata = dict()
    # for i in lis :
    #     jdata[i] = data[i]
    #
    #
    # return jsonify({'msg': json.dumps(jdata)}), 200
    f = open('question2.json', )
    data = json.load(f)
    data = data["Question"]
    lis = rd.sample((data), 5)
    jdata = dict()
    for i in range(5):
        jdata[i] = lis[i]
    return jsonify({'msg': json.dumps(jdata)}), 200



@app.route("/Checkquestionans", methods=['POST'])
def Checkquestionans():
    try:
        jsondata = request.get_data().decode("utf-8")
        jsondata = json.loads(jsondata)
        ans = jsondata['Ans']
        # print(chat.say(first_question,jsondata['id']))

        return jsonify({'msg':  float(sentiment_analyzer_scores(ans))}), 200

    except Exception  as e:
        print(str(e))

        return jsonify({'msg': 'try Again 1 '+str(e), }), 401



def getsuggutiondata(f):
    data = json.load(f)
    lis = rd.sample(dict(data).keys(), 5)
    jdata = dict()
    for i in lis:
        jdata[i] = data[i]
    # print(112211,jdata)
    f.close()
    return jdata

@app.route("/suggestion", methods=['POST'])
def suggestion ():
    f = open('testbook.json', )
    f1 = open('General.json', )
    f2 = open('audiobook.json', )


    # print(getsuggutiondata(f))
    # print( json.dumps(getsuggutiondata(f)))

    return jsonify({'testbook': json.dumps(getsuggutiondata(f)),'general': json.dumps(getsuggutiondata(f1)),'audiobook': json.dumps(getsuggutiondata(f2))},), 200



