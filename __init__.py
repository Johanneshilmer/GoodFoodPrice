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
    food_store1 = None
    food_store2 = None
    product1_price = None
    product2_price = None
    c = sqlite3.connect("products.db")
    cursor = c.cursor()
    if request.method == "POST":
        # Handles all the sql queries.
        product1 = request.form["product1"]
        product2 = request.form["product2"]
        store1 = request.form["store1"]
        store2 = request.form["store2"]
        try:
            cursor.execute("SELECT price FROM {} WHERE name = ?".format(store1), (product1,))
            result = cursor.fetchone()
            if result is not None:
                food_store1 = result[0]
                product1_price = result[0]
            else:
                raise ValueError("Product not found in store.")
            cursor.execute("SELECT price FROM {} WHERE name = ?".format(store2), (product2,))
            result = cursor.fetchone()
            if result is not None:
                food_store2 = result[0]
                product2_price = result[0]
            else:
                raise ValueError("Product not found in store.")
        except sqlite3.Error as e:
            print("Database error:", e)
            return render_template("error.html", message="Database error occurred. Please try again later.")
        except ValueError as e:
            print("Value error:", e)
            return render_template("error.html", message="Invalid input. Please try again.")
    c.close()
    return render_template("home.html", product1_price = product1_price, product2_price = product2_price, food_store1 = food_store1, food_store2 = food_store2)


if __name__ == "__main__":
    app.run(debug = True)