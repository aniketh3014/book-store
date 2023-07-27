from flask import Flask, render_template, request, session
from flask_session import Session
import sqlite3

app =Flask(__name__)

db = sqlite3.connect("store.db", check_same_thread=False)
cur = db.cursor()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    books=cur.execute("SELECT * FROM books")
    return render_template("books.html", books=books)