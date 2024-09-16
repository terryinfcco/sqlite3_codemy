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

# Put a row of data into table customers of customer.db
# Need to use single quotes inside the double quotes
c.execute("INSERT INTO customers VALUES ('Izie', 'Wygmans', 'izie@email.com')")

print("Command executed successfully...")

# Commit to the database
conn.commit()

# close the database
conn.close()
