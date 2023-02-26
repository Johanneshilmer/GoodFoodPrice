import sqlite3

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()

cursor = conn.cursor()

# Create the database table if it not exist already. "For store 1 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS ica
                (name text, price real)""")
conn.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO ica VALUES ('mjölk', 13.50)")
cursor.execute("INSERT INTO ica VALUES ('ost', 90)")
cursor.execute("INSERT INTO ica VALUES ('bröd', 32.50)")
cursor.execute("INSERT INTO ica VALUES ('ägg', 32)")
cursor.execute("INSERT INTO ica VALUES ('fisk', 99)")
cursor.execute("INSERT INTO ica VALUES ('kött', 130)")
conn.commit()

# Create the database table if it not exist already. "For store 2 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS coop
                (name text, price real)""")
conn.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO coop VALUES ('mjölk', 13)")
cursor.execute("INSERT INTO coop VALUES ('ost', 86)")
cursor.execute("INSERT INTO coop VALUES ('bröd', 33.50)")
cursor.execute("INSERT INTO coop VALUES ('ägg', 31)")
cursor.execute("INSERT INTO coop VALUES ('fisk', 89)")
cursor.execute("INSERT INTO coop VALUES ('kött', 140)")
conn.commit()

# Create the database table if it not exist already. "For store 3 of 3."
cursor.execute("""CREATE TABLE IF NOT EXISTS maxi
                (name text, price real)""")
conn.commit()

# Insert some exemple data into the table.
cursor.execute("INSERT INTO maxi VALUES ('mjölk', 15.50)")
cursor.execute("INSERT INTO maxi VALUES ('ost', 100)")
cursor.execute("INSERT INTO maxi VALUES ('bröd', 33.50)")
cursor.execute("INSERT INTO maxi VALUES ('ägg', 34)")
cursor.execute("INSERT INTO maxi VALUES ('fisk', 85)")
cursor.execute("INSERT INTO maxi VALUES ('kött', 120)")
conn.commit()

conn.close()

