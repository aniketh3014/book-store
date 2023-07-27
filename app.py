from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import sqlite3

app =Flask(__name__)

db = sqlite3.connect("store.db", check_same_thread=False)
cur = db.cursor()
#configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    books=cur.execute("SELECT * FROM books")
    db.commit()
    return render_template("books.html", books=books)

@app.route("/cart")
def cart():
    if "cart" not in session:
        session["cart"] = []
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect("/cart")
    for ID in session["cart"]:
        books = cur.execute("SELECT * FROM books WHERE id IN (?)",ID)
    return render_template("cart.html", books=books)
    

