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
    books=cur.execute("SELECT * FROM books").fetchall()
    return render_template("books.html", books=books)

@app.route("/cart", methods=["POST", "GET"])
def cart():
    if "cart" not in session:
        session["cart"] = []

    print("Cart Session:", session["cart"])  # Add this line for debugging

    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
            print("Added Book ID to Cart:", id)  # Add this line for debugging
        return redirect("/cart")
    
    books = cur.execute("SELECT * FROM books WHERE id IN ({})".format(','.join(session["cart"]))).fetchall()

    print("Cart Books:", books)  # Add this line for debugging

    return render_template("cart.html", books=books)
    

