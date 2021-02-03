# from chatterbot import ChatBot
#
# from chatterbot.trainers import ChatterBotCorpusTrainer
import json
import random as rd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def sentiment_analyzer_scores(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    return (  str(score))



f = open('question2.json', )
data = json.load(f)
data  = data["Question"]
print(data)
lis = rd.sample((data)   ,5)
jdata = dict()
for i in range(5) :
    jdata[i] = lis[i]
print(jdata)






# print(sentiment_analyzer_scores("Yes i Have helped someone who was feeling stressful"))
# trainer = ChatterBotCorpusTrainer(Chatbot)
# Create a new trainer for the chatbot
#
# # Train based on the english corpus
# trainer.train("chatterbot.corpus.english")
#
# # Train based on english greetings corpus
# trainer.train("chatterbot.corpus.english.greetings")
#
# # Train based on the english conversations corpus
# trainer.train("chatterbot.corpus.english.conversations")