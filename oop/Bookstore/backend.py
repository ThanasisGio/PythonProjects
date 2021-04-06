import sqlite3


class Database:

    def __init__(self,db):

        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer) ")
        self.conn.commit()
        

    #have to call function so it can execute,if i run frontend connect() fun will run too
    # pass for items in insert function
    def insert(self,title,author,year,isbn):
        #then i need to connect to database
       
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        


    def view(self):
        
        #then i need to connect to database
        
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        #self.conn.commit()
        #self.conn.close()
        #data stored in row variable so i return that
        return rows
    # pass empty values just in case user only passes on variable 
    def search(self,title="",author="",year="",isbn=""):
       
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        #self.conn.commit()
        #self.conn.close()
        return rows

    def delete(self,id):
        
        self.cur.execute("DELETE FROM book WHERE id=?",(id,) )
        self.conn.commit()
        

    def update(self,id,title,author,year,isbn):
        
        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id) )
        self.conn.commit()
        self.conn.close()

    def __del__(self):
        self.conn.close()



#connect()
#insert("The Big","John woo",1914,888899)
#delete(4)
#update(4,"The moon","John Smooth",1917,999999)
#print(view())
#print(search(author="John Smith"))