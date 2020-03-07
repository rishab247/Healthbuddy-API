import sys
import os
import threading as thread
from chatbot import *
import aiml
import time
import json
from difflib import get_close_matches
import datetime 
import random
from wikipedia import *
import webbrowser

def browser(query):
    try:
        webbrowser.open('www.'+query+'.com')
        return "Opening Browser"
    except:
        
        return "Please check your Internet connection!"
def search(query):
    try:
        webbrowser.open_new('www.google.com/search?q=' + query)
        return "Searching in Browser"
    except:
        
        return "Please check your Internet connection!"
def navigate(query):
    try:
        webbrowser.open_new('www.google.com/search?q=navigate+to+' + query)
        return "Okay!"
    except:
        return "Please check your Internet connection!"
def navigateing(query):
    try:
        webbrowser.open_new('www.google.com/search?q=' + query)
        return "Okay!"
    except:
        return "Please check your Internet connection!"

#normal wiki command
def wikip(n):
    try:
        q=wikipedia.summary(n, sentences=4)
        return q
    except:
        return "please rephrase your statement"


dice = ['1', '2', '3', '4', '5', '6']
coin = ['Heads', 'Tails']


def toss():
    random.choice(coin)
   
    return "You got "+ random.choice(coin)


def throw():

    return "You got "+random.choice(dice)

k = aiml.Kernel()
k.learn("database/std-startup.xml")
k.respond("load aiml b")
data = json.load(open("database/data.json"))


def extras_spam(n):
    q = k.respond(n)
    if q =="damm":
        q = response(n)
        return q
    else:
        return q

def dictionarry(w):  
    if w in data:
        return data[w][0]
    elif w.title() in data:
        return data[w.title()][0]
    elif len(get_close_matches(w, data.keys())) > 0:
        print(get_close_matches(w, data.keys())[0])
        return dictionarry(get_close_matches(w, data.keys())[0])
    else:
        return "The word doesn't exist. Please double check it."

def listToString(s):  
    str1 = ""   
    for ele in s:  
        str1 += ele   
    return str1  

def search_for_n(n):
    
        if "tell me the meaning of" in n:
                n = n.replace("tell me the meaning of ","")
                q = dictionarry(n)
                return q
        elif "how to" in n:
            search(n)
        elif "what is the meaning of" in n:
                n = n.replace("tell me the meaning of ","")
                q = dictionarry(n)
                return q
        elif "meaning of" in n:
                n = n.replace("meaning of ","")
                q= dictionarry(n)
                return q
        elif 'tell me about' in n:
                n = n.replace('tell me about ', '')
                q = wikip(n)
                return q
        elif 'throw a dice' in n:
                q = throw()
                return q
        elif 'what is the time' in n:
                now = datetime.datetime.now()
                real_time = now.strftime("%I:%M %p")
                return "It's"+real_time
        elif 'what is the date' in n:
                now = datetime.datetime.now()
                real_time = now.strftime("%d-%m-%Y")
                return "today is "+real_time
        elif 'toss a coin' in n:
                q = toss()
                return q
        else:
                q = extras_spam(n)
                return q     


                                
                                

                

def main_call(n):
    n = n.lower()
    return search_for_n(n)


 