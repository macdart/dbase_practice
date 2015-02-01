#INSERT command

#Note that this demonstrates two different ways to populate a table, the first does not use the 'with' keyword; the second does

# import the sqlite3 library
import sqlite3

## create the connection object
#conn = sqlite3.connect("new.db")

## get a cursor object used to execute SQL commands
#cursor = conn.cursor()

## insert data
#cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
#cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

## commit the changes
#conn.commit()

## close the database connection 
#conn.close()

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('Toronto', 'ON', 521232)")
    c.execute("INSERT INTO population VALUES('Vancouver', 'BC', 2323423)")

