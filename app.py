import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def get_breakfast():
    breakfast = list(mongo.db.breakfast.find({"type": "breakfast"}))
    return render_template("index.html", breakfast=breakfast)
    

@app.route("/") 
def get_lunch():
    lunch = list(mongo.db.lunch.find({"type": "lunch"}))
    return render_template("index.html", lunch=lunch)
    

@app.route("/")
def get_dinner():
    dinner = list(mongo.db.dinner.find({"type": "dinner"}))
    return render_template("index.html", dinner=dinner)

if __name__ == "__main":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

