from flask import Flask


app = Flask(__name__)



@app.route("/info")
def lw():
    return "Welcome to0000000000000000000 LW...."


app.run(host='0.0.0.0')
