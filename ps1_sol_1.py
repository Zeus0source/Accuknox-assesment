#fetching the data (used openlibrary api endpoint)
import requests 
response=requests.get("https://openlibrary.org/search.json?q=john+grisham")
data=response.json()
books=data["docs"][:10]
books1=[]
for book in books:
    title=book['title']
    author=book.get("author_name",["unknown"])[0]
    year=book.get("first_publish_year","unknown")
    books1.append((title,author,year))
print(books1)
#storing it in sqlite
import sqlite3
cx=sqlite3.connect("books.db")
cu=cx.cursor()  
cu.execute("create table if not exists books(title text ,author text, year integer )")
cu.execute("delete from books")
cu.executemany("insert into books values (?, ? ,?)",books1)
cx.commit()
print("Data Inserted in the table: ")
cu.execute("select * from books")
for row in cu.fetchall():
    print(row)
