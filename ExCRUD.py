def createDatabase():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678")
    mycur=mycon.cursor()
    nod=input("enter name of database to create :  ")
    q="create Database %s"%nod
    mycur.execute(q)
    print(nod,"database has been created!!")
createDatabase()

def deleteDatabase():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678")
    mycur=mycon.cursor()
    nod=input("Delete name of database!!  ")
    q="drop Database %s"%nod
    mycur.execute(q)
    print(nod,"database has been deleted!!")

def showDatabases():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678")
    mycur=mycon.cursor()
    q="show databases"
    mycur.execute(q)
    lod=mycur.fetchall()
    for i in lod:
        print(i)

def createTable():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678",database="hubnet")
    mycur=mycon.cursor()
    tn=input("Enter name of table:  ")
    q="create table %s(name text,uid varchar (10)primary key,password varchar(10)not null)"%tn
    mycur.execute(q)
    print("table has created!!")

def showTables():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678",database="hubnet")
    mycur=mycon.cursor()
    q="show tables"
    mycur.execute(q)
    lot=mycur.fetchall()
    for i in lot:
        print(i)

def deleteTable():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678",database="hubnet")
    mycur=mycon.cursor()
    dt=input("Enter name of table!!")
    q="drop table %s"%dt
    mycur.execute(q)
    print("table has deleted!!")

def showRecord():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678",database="hubnet")
    mycur=mycon.cursor()
    tn=input("Enter name of table !")
    q="select * from %s"%tn
    mycur.execute(q)
    rec=mycur.fetchall()
    for i in rec:
        print(i)

def insertRecord():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678",database="hubnet")
    mycur=mycon.cursor()
    un=input("Enter user name  : ")
    uid=input("Enter userId  : ")
    pas=input("Enter password  : ")
    q="insert into user values('{}','{}','{}')".format(un,uid,pas)
    mycur.execute(q)
    mycon.commit()
    print("one record has saved!!")

def updateTable():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678",database="hubnet")
    mycur=mycon.cursor()
    np=input("Enter new password  : ")
    uid=input("Enter userId  : ")
    q="update user set password='{}' where uid='{}'".format(np,uid)
    mycur.execute(q)
    mycon.commit()
    print("record update")


def deleteRecord():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="12345678",database="hubnet")
    mycur=mycon.cursor()
    uid=input("Enter useID  ")
    q="delete from user where uid='{}'".format(uid)
    mycur.execute(q)
    mycon.commit()
    print("one record delete!!")

          


    
    
    

    
             
    

    

    
    
          


