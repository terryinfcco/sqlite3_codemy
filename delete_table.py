import sqlite3

# Connect to database
# if you want to just have a db in memory that disappears after the program ends
# conn = sqlite3.connect(':memory:')
# if customer.db exists this will just connect to it rather than recreate it.
conn = sqlite3.connect('customer.db')

# Tables inside database contains all the data in the database
# row and columns like a spreadsheet

# Need to create cursor first - used to talk to the database
c = conn.cursor()

# Drop Table
c.execute("DROP TABLE customers")
conn.commit()

# Query the database - Limits just limits to a certain number of records.
c.execute("SELECT rowid, * FROM customers")

all_customers = c.fetchall()    # fetches everything in the table
for cust in all_customers:
    print(cust)


# print("Command executed successfully...")

# Commit to the database
conn.commit()

# close the database
conn.close()