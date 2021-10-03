import db_template

# Add a record
# db_template.add_one("Marty","Wygmans","martha@email.com")

# Delete a record - rowid has to be passed as a string even though it's an integer
# db_template.delete_one("6")

# Add many records

#people = [
#    ('Marty', 'Wygmans', 'martha@email.com'),
#    ('Amberly', 'Parnell', 'amberly@email.com')
#]

#db_template.add_many(people)

db_template.email_lookup("martha@email.com")

# db_template.show_all()

