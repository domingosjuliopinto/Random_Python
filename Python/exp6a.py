import pymysql

connection=pymysql.connect(
    host="localhost",
    user="root",
    db="experiment"
    )

cur=connection.cursor()

s='''create table Employee(
empno integer primary key,
EmpName varchar(20),
Salary integer,
DOJ varchar(20)
)'''

cur.execute(s)

connection.close()
