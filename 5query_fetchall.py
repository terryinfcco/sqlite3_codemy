import sqlite3

# Connect to database
# if you want to just have a db in memory that disappears after the program ends
# conn = sqlite3.connect(':memory:')
# if customer.db exists this will just connect to it rather than recreate it.
conn = sqlite3.connect("customer.db")

# Tables inside database contains all the data in the database
# row and columns like a spreadsheet

# Need to create cursor first - used to talk to the database
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")
# c.fetchone()    # fetches last item in table
# c.fetchmany(3)  # fetches 3 items (from where?)
all_customers = c.fetchall()  # fetches everything in the table
# Returns a list of tuples

print(all_customers)

# print("Command executed successfully...")

# Commit to the database
conn.commit()

# close the database
conn.close()
