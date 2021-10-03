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

# To insert multiple records create a list of tuples
many_customers = [('Dave', 'Wygmans', 'dave@email.com'),
     ('Hugh','Wygmans', 'hugh@email.com'),
     ('Marty','Wygmans', 'martha@email.com'),]

# Put the list of data into table customers of customer.db
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

print("Command executed successfully...")

# Commit to the database
conn.commit()

# close the database
conn.close()