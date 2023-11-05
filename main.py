from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")

dishes = [
    {"id": 4, "name": "Italian pizza", "price": 150},
    {"id": 2, "name": "Bavarian pizza", "price": 100},
    {"id": 3, "name": "Hawaiian pizza", "price": 120},
    {"id": 1, "name": "Barbecue pizza", "price": 90}
]

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/menu/")
def menu():
    context = {
        "title": "Menu",
        "dishes": dishes
    }
    return render_template("menu.html", **context)

@app.route("/sumbit/", methods=["GET", "POST"])
def sumbit():
    if request.method == "POST":
        user_name = request.form["user_name"]
        prod_id = request.form["prod_id"]
        with sqlite3.connect("test.db") as db:
            cursor = db.cursor()
            cursor.execute("""INSERT INTO pizza
                                (user, product)
                                VALUES
                                (?, ?)""", (user_name, prod_id))
            db.commit()
            cursor.close()
            return render_template("index.html")
    else:
        return render_template("menu.html")

if __name__ == "__main__":
    app.run(debug=True)