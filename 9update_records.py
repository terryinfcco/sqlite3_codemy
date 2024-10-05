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

# Update Records

c.execute("""UPDATE customers SET first_name = 'Terry'
        WHERE rowid == 1
""")

conn.commit()

# Query the database
# c.execute("SELECT * FROM customers WHERE last_name = 'Dutcher'")
# for numeric fields can use < and > like salary > 50000 and salary < 100000
# Or use % as wildcard - so here get all starting with W
c.execute("SELECT rowid, * FROM customers ")

all_customers = c.fetchall()    # fetches everything in the table
for cust in all_customers:
    print(cust)


# print("Command executed successfully...")

# Commit to the database
conn.commit()

# close the database
conn.close()