import sqlite3

# Connect to database
# if you want to just have a db in memory that disappears after the program ends
# conn = sqlite3.connect(':memory:')
# if customer.db exists this will just connect to it rather than recreate it.

def show_all():
    conn = sqlite3.connect('customer.db')

    # Need to create cursor first - used to talk to the database
    c = conn.cursor()

    # Query the database - Limits just limits to a certain number of records.
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit to the database
    conn.commit()

    # close the database
    conn.close()

# Add a new record to the Table
def add_one(first, last, email):
    # Have to connect to and create a cursor everytime.
    conn = sqlite3.connect('customer.db')
    # Need to create cursor first - used to talk to the database
    c = conn.cursor()

    # The actual add / insert code.
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # Commit to the database
    conn.commit()

    # close the database
    conn.close()

# Add many records to the Table passed as a list of tuples
def add_many(list):
    # Have to connect to and create a cursor everytime.
    conn = sqlite3.connect('customer.db')
    # Need to create cursor first - used to talk to the database
    c = conn.cursor()

    # The actual add / insert code.
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    # Commit to the database
    conn.commit()
    # close the database
    conn.close()


# Delete a record from the Table
def delete_one(id):
    # Have to connect to and create a cursor everytime.
    conn = sqlite3.connect('customer.db')
    # Need to create cursor first - used to talk to the database
    c = conn.cursor()

    # The actual delete code.
    c.execute("DELETE FROM customers WHERE rowid == (?)", id)

    # Commit to the database
    conn.commit()

    # close the database
    conn.close()

# Lookup with Where
def email_lookup(email):
    # Have to connect to and create a cursor everytime.
    conn = sqlite3.connect('customer.db')
    # Need to create cursor first - used to talk to the database
    c = conn.cursor()

    # passing a tuple that only has one item so we have to put a comma after the one item.
    c.execute("SELECT * from customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)

    # close the database
    conn.close()