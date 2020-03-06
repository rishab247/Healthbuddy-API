from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Fuck OFF!"

@app.route("/Askme")
def Askme():
    return "Fuck OFF! Again"
