# SELECT statment, remove unicode characters

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # use a for loop to iterate through the database, printing the results line by line

#    for row in c.execute("SELECT firstname, lastname from employees"):
#       print row

    c.execute("SELECT firstname, lastname from employees")
 
    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # ourput the rows to the screen, row by row
    for r in rows:
        print r[0], r[1]
