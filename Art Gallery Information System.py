import sqlite3

try:
    connection = sqlite3.connect('Gallery.db')
except Error:
    print(Error)
c = connection.cursor()

try:
    c.execute("CREATE TABLE Gallery ( Artwork Name text PRIMARY KEY,  text, Artist Name text,  Year integer)")
    connection.commit()
except:
    print("Error Tables already exist ")

def insert():
    c.execute(' INSERT INTO Gallery(Artwork Name, Artist Name, Year) VALUES(?, ?, ?)', entity)
    connection.commit()
    c.execute('SELECT * FROM Gallery ')
    rows = c.fetchall()
    print(rows)
    
def update(con, field, old, new):
    field.lower()
    if field == "":
        c.execute('''UPDATE Gallery SET Artwork Name = ? WHERE Artwork Name = ?''', (new, old))
        connection.commit()
        c.execute('SELECT * FROM Gallery')
        rows = c.fetchall()
        print(rows)
    elif field == "Artist Name":
        c.execute('''UPDATE Gallery SET Artist Name = ? WHERE Artist Name = ?''', (new, old))
        connection.commit()
        c.execute('SELECT * FROM Gallery')
        rows = c.fetchall()
        print(rows)
    elif field == "Artwork Name":
        c.execute('''UPDATE Gallery SET Artwork Name = ? WHERE Artwork Name = ?''', (new, old))
        connection.commit()
        c.execute('SELECT * FROM Gallery')
        rows = c.fetchall()
        print(rows)
    else:
        c.execute('''UPDATE Gallery SET Year = ? WHERE Year = ?''', (new, old))
        connection.commit()
        c.execute('SELECT * FROM Gallery')
        rows = c.fetchall()
        print(rows)

def delete(con, dele):
    sql_state = 'DELETE FROM Gallery WHERE Artist Name = ?'
    c.execute(sql_state, (dele,))
    connection.commit()
    c.execute('SELECT * FROM Gallery')
    rows = c.fetchall()
    print(rows)

def search(con, name):
    sql_state = 'SELECT * FROM Gallery WHERE Artwork Name = ? OR Artist Name = ?'
    c.execute(sql_state, (name,name,))
    rows = c.fetchall()
    print(rows)
while True:
    start = input("Enter an option : Insert, Update, Delete, Search, Q to quit ")
    start.lower()
	if start == "q":
        break
    
    elif start == "insert":
        AN = input("Enter Artwork Name ")
        ArN = input("Enter Artist Name ")
        Yr = input("Enter Year ")
		entity = (AN, ArN,Yr)
        insert()

    elif start == "update":
        field = input("Choose what you want to update: Artwork Name, Artist Name, Year ")
        old = input("Enter {} name you want to change ".format(field))
        new = input("Enter the new {} name ".format(field))

        update(connection, field, old, new)

    elif start == "delete":
        dele = input("Enter Artist name you want to delete ")

        delete(connection, dele)

    else:
        s = input("Enter Artwork/Artist name you want ")
        search(connection, s)