import psycopg2

def create_table():
    #steps
    #1 connect to databae
    #2create cursor, like a pointer to connect with rows columns
    #3write sql query
    #4commit changes
    # connect to database file db
    conn=psycopg2.connect("dbname='database1' user='postgres' password='posgres1234' host='localhost' port='5432'")
    cur=conn.cursor()
    #sql code always goes in brackets,CREATE TABLE to make table
    #item declared as TEXT, quantity AS INTERGER price as REAL
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    #add data to database
    
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='posgres1234' host='localhost' port='5432'")
    cur=conn.cursor()
    #?,?,? sql text then wite variables, then call function insert
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')"% (item,quantity,price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

# ("Coffee Cup",10,5)

# create function that views data

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='posgres1234' host='localhost' port='5432'")
    cur=conn.cursor()
    # sql SELECT * means all FROM store
    cur.execute("SELECT * FROM store")
    #fetch data
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='posgres1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='posgres1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))   
    conn.commit()
    conn.close()

#update(11,6,"Water Glass")
#delete("Wine Glass")
#print(view())
create_table() 
#insert("Apple",10,15)
#delete("Apple")
update(20,15.0,'Apple')   
print(view())