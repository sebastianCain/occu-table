from flask import Flask, render_template
from utils.util import getTableMatrix, getRandom
import random
app = Flask(__name__)

@app.route("/")

def route1():
	return render_template("index.html", title = "Occu-Table Central")

@app.route("/occupations")

def route2():
	return render_template("table.html", title = "data/occupations", tableData = getTableMatrix(), occupation = getRandom())

if __name__ == "__main__":
    app.debug = True
    app.run()
