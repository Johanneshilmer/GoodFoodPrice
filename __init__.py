from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) #Flask instance

# Make a connection with SQLite database
c = sqlite3.connect("products.db")
cursor = c.cursor()

# Create the database table if it not exist already. "For store 1 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS ica
                (name text, price real)""")
c.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO ica VALUES ('mjölk', 13.50)")
cursor.execute("INSERT INTO ica VALUES ('ost', 90)")
cursor.execute("INSERT INTO ica VALUES ('bröd', 32.50)")
cursor.execute("INSERT INTO ica VALUES ('ägg', 32)")
cursor.execute("INSERT INTO ica VALUES ('fisk', 99)")
cursor.execute("INSERT INTO ica VALUES ('kött', 130)")
c.commit()

# Create the database table if it not exist already. "For store 2 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS coop
                (name text, price real)""")
c.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO coop VALUES ('mjölk', 13)")
cursor.execute("INSERT INTO coop VALUES ('ost', 86)")
cursor.execute("INSERT INTO coop VALUES ('bröd', 33.50)")
cursor.execute("INSERT INTO coop VALUES ('ägg', 31)")
cursor.execute("INSERT INTO coop VALUES ('fisk', 89)")
cursor.execute("INSERT INTO coop VALUES ('kött', 140)")
c.commit()

# Create the database table if it not exist already. "For store 3 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS maxi
                (name text, price real)""")
c.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO maxi VALUES ('mjölk', 15.50)")
cursor.execute("INSERT INTO maxi VALUES ('ost', 100)")
cursor.execute("INSERT INTO maxi VALUES ('bröd', 33.50)")
cursor.execute("INSERT INTO maxi VALUES ('ägg', 34)")
cursor.execute("INSERT INTO maxi VALUES ('fisk', 85)")
cursor.execute("INSERT INTO maxi VALUES ('kött', 120)")
c.commit()


# Handle the home page
@app.route("/", methods=["GET", "POST"])
def home():
    store1 = None
    store2 = None
    product = None
    product1_price = None
    product2_price = None
    c = sqlite3.connect("products.db")
    cursor = c.cursor()
    if request.method == "POST":
        # Handles all the sql queries.
        product = request.form["product"]
        store1 = request.form["store1"]
        store2 = request.form["store2"]
        print(product,store1,store2)
        try:
            cursor.execute("SELECT price FROM {} WHERE name = ?".format(store1), (product,))
            result = cursor.fetchone()
            if result is not None:
                product1_price = result[0]
            else:
                raise ValueError("Product not found in store.")
        except sqlite3.Error as e:
            print("Database error", e)
        except ValueError as e:
            print("Value error", e)
            return render_template("home.html", product1_price=product1_price, store1=store1, store2=store2, product_error="error")
        try:
            cursor.execute("SELECT price FROM {} WHERE name = ?".format(store2), (product,))
            result = cursor.fetchone()
            if result is not None:
                product2_price = result[0]
            else:
                raise ValueError()
        except sqlite3.Error as e:
            print("Database error", e)
        except ValueError as e:
            print("Value error", e)
            return render_template("home.html", product1_price=product1_price, store1=store1, store2=store2, product_error="error")
    c.close()
    return render_template("home.html", product1_price=product1_price, product2_price=product2_price, store1=store1, store2=store2, product=product)



if __name__ == "__main__":
    app.run(debug = True)