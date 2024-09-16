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

# Create a table - Use a docstring just to make it more readable - could be all on one
# line but this is easier to read. Docstring is recommended by the developers of SQLite3
# SQLite3 is case sensitive.
# sqlite3 has only 5 datatypes: text, integer, real, null, blob (images, music file - stored exactly as is)
c.execute(
    """CREATE TABLE customers (
        first_name text, 
        last_name text,
        email text
    )"""
)

# example of same thing on one line
# c.execute("CREATE TABLE customers (first_name text, last_name text, email text)")

# Commit to the database, required for database changes
conn.commit()

# close the database
conn.close()
