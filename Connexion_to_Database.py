import mysql.connector


class Fetch:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port=3306,
        passwd="",
        database="electronics")
    c = mydb.cursor()
    c.execute("SELECT user FROM testeur")
    users = c.fetchall()
    c.execute("SELECT categorie FROM met")
    categories = c.fetchall()
    c.execute("SELECT email FROM testeur")
    emails = c.fetchall()
    print(emails)
    if ("youcef@gmail.com",) in emails:
        print('yes')
    else:
        print('no')



