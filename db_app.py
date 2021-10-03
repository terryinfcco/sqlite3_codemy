import db_template

not_done = True
# Loop until x is menu choice

while not_done:

    # Create a menu so we can use the database
    print ()
    print ("Menu - Select an Option")
    print ("-----------------------")
    print ("S - Show All Records")
    print ("A - Add a Record")
    print ("D - Delete a Record")
    print ("F - Find a record by Email Address")
    print ("X - Exit Database Program")
    print ()
    option = input("Enter your selection: ")
    print()

    if option.lower() == 'x':
        not_done = False
    elif option.lower() == 's':
        db_template.show_all()
        print()
        input ("Press Enter to Continue")
    elif option.lower() == 'a':
        print ("Adding a customer:")
        first = input("Enter First Name: ")
        last = input("Enter Last Name: ")
        email = input("Enter Email Address: ")

        # Add the record
        db_template.add_one(first, last, email)
    elif option.lower() == 'd':
        print ("Deleting a customer:")
        id = input("Enter Primary Key: ")
        
        # Delete a record - rowid has to be passed as a string even though it's an integer
        db_template.delete_one(id)
    elif option.lower() == 'f':
        email = input("Enter Email Address: ")
        db_template.email_lookup(email)
        print()
        input ("Press Enter to Continue")


# Add many records

#people = [
#    ('Marty', 'Wygmans', 'martha@email.com'),
#    ('Amberly', 'Parnell', 'amberly@email.com')
#]

#db_template.add_many(people)




