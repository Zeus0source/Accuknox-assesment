#creating database and table
import sqlite3
cx=sqlite3.connect("sample.db")
cu=cx.cursor()
cu.execute("create table if not exists user(id integer,first_name text,last_name text,email text, gender text)")
#importing csv file
import csv
with open("MOCK_DATA.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    cu.execute("delete from user")
    for row in reader:
        cu.execute("insert into user values(?,?,?,?,?)",row)
    cx.commit()
cu.execute("select * from user")
for row in cu.fetchall():
    print(row)