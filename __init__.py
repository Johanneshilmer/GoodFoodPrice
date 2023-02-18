from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) #Flask instance

# Make a connection with SQLite database
c = sqlite3.connect("products.db")
cursor = c.cursor()

# Create the database table if it not exist already. "For store 1 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS ICA_products
                (name text, price real)""")
c.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO ICA_products VALUES ('mjölk', 13.50)")
cursor.execute("INSERT INTO ICA_products VALUES ('ost', 90)")
cursor.execute("INSERT INTO ICA_products VALUES ('bröd', 32.50)")
cursor.execute("INSERT INTO ICA_products VALUES ('ägg', 32)")
cursor.execute("INSERT INTO ICA_products VALUES ('fisk', 99)")
cursor.execute("INSERT INTO ICA_products VALUES ('kött', 130)")
c.commit()

# Create the database table if it not exist already. "For store 2 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS COOP_products
                (name text, price real)""")
c.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO COOP_products VALUES ('mjölk', 13)")
cursor.execute("INSERT INTO COOP_products VALUES ('ost', 86)")
cursor.execute("INSERT INTO COOP_products VALUES ('bröd', 33.50)")
cursor.execute("INSERT INTO COOP_products VALUES ('ägg', 31)")
cursor.execute("INSERT INTO COOP_products VALUES ('fisk', 89)")
cursor.execute("INSERT INTO COOP_products VALUES ('kött', 140)")
c.commit()

# Create the database table if it not exist already. "For store 3 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS MAXI_products
                (name text, price real)""")
c.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO MAXI_products VALUES ('mjölk', 15.50)")
cursor.execute("INSERT INTO MAXI_products VALUES ('ost', 100)")
cursor.execute("INSERT INTO MAXI_products VALUES ('bröd', 33.50)")
cursor.execute("INSERT INTO MAXI_products VALUES ('ägg', 34)")
cursor.execute("INSERT INTO MAXI_products VALUES ('fisk', 85)")
cursor.execute("INSERT INTO MAXI_products VALUES ('kött', 120)")
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