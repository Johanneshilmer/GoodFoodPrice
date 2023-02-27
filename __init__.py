from flask import Flask, render_template, request
from database import sqlite3

app = Flask(__name__, template_folder="templates")

# Handle the home page
@app.route("/", methods=["GET", "POST"])
def home():

    #Creating a new connection to SQLite3 db.
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    store1 = None
    store2 = None
    product = None
    product1_price = None
    product2_price = None
    if request.method == "POST":
        # Handles all the sql queries.
        product = request.form["product"]
        store1 = request.form["store1"]
        store2 = request.form["store2"]
        try:
            cursor.execute("SELECT price FROM {} WHERE name = ?".format(store1), (product,))
            result = cursor.fetchone()
            if result is not None:
                product1_price = result[0]
            else:
                raise ValueError("Product not found in store.")
        except sqlite3.Error as e:
            print("Database error", e) #If there is a error this will print in the console.
        except ValueError as e:
            print("Value error", e) #If there is a error this will print in the console.
            return render_template("home.html", product1_price=product1_price, store1=store1, store2=store2, product_error="error")
        try:
            cursor.execute("SELECT price FROM {} WHERE name = ?".format(store2), (product,))
            result = cursor.fetchone()
            if result is not None:
                product2_price = result[0]
            else:
                raise ValueError()
        except sqlite3.Error as e:
            print("Database error", e) #If there is a error this will print in the console.
        except ValueError as e:
            print("Value error", e) #If there is a error this will print in the console.
            return render_template("home.html", product1_price=product1_price, store1=store1, store2=store2, product_error="error")
    conn.close()
    return render_template("home.html", product1_price=product1_price, product2_price=product2_price, store1=store1, store2=store2, product=product)

@app.route("/info", methods=["GET", "POST"])
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug = True)