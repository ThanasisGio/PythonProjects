import sqlite3



def connect():

    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer) ")
    conn.commit()
    conn.close()

#have to call function so it can execute,if i run frontend connect() fun will run too
# pass for items in insert function
def insert(title,author,year,isbn):
    #then i need to connect to database
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()


def view():
    
    #then i need to connect to database
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    #data stored in row variable so i return that
    return rows
# pass empty values just in case user only passes on variable 
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,) )
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id) )
    conn.commit()
    conn.close()



connect()
#insert("The Big","John woo",1914,888899)
#delete(4)
#update(4,"The moon","John Smooth",1917,999999)
#print(view())
#print(search(author="John Smith"))