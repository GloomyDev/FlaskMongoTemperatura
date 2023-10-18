from flask import Flask, render_template
import subprocess as sp  # Import subprocess
from pymongo import MongoClient
from mongopass import mongopass

def create_app():
    app = Flask("__main__")

    # MongoDB Configuration
    client = MongoClient(mongopass)
    db = client.PicoDB
    myCollection = db.Temperature

    @app.route("/")
    def my_home():
        date = sp.getoutput("date /t")
        latest_document = myCollection.find_one(sort=[("$natural", -1)])
        latest_value = latest_document.get("readings", None) if latest_document else None
        return render_template("home.html", date=date, data=latest_value)

    return app
