import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("bike_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Jawa')")
cursor.execute("insert into list (description) values ('RoyalEnfield')")
cursor.execute("insert into list (description) values ('Ducati')")
cursor.execute("insert into list (description) values ('BMW')")
cursor.execute("insert into list (description) values ('Truimph')")

connection.commit()
connection.close()

print("done.")
