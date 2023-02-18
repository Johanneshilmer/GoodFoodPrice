from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) #Flask instance

# Make a connection with SQLite database
c = sqlite3.connect("products.db")
cursor = c.cursor()

# Create the database table if it not exist already.
cursor.execute("""CREATE TABLE IF NOT EXISTS products
                (name text, price real)""")
c.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO products VALUES ('Product 1', 10)")
cursor.execute("INSERT INTO products VALUES ('Product 2', 20)")
cursor.execute("INSERT INTO products VALUES ('Product 3', 30)")
c.commit()


# Handle the home page
@app.route("/", methods=["GET", "POST"])
def home():
    product1_price = None
    product2_price = None
    c = sqlite3.connect("products.db")
    cursor = c.cursor()
    if request.method == "POST":
        product1 = request.form["product1"]
        product2 = request.form["product2"]
        cursor.execute("SELECT price FROM products WHERE name = ?", (product1,))
        product1_price = cursor.fetchone()[0]
        cursor.execute("SELECT price FROM products WHERE name = ?", (product2,))
        product2_price = cursor.fetchone()[0]
    c.close()
    return render_template("home.html", product1_price = product1_price, product2_price = product2_price)

if __name__ == "__main__":
    app.run(debug = True)