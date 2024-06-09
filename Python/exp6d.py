import pymysql
from tkinter import *
def read(event):

    connection=pymysql.connect(
        host="localhost",
        user="root",
        db="experiment"
        )

    cur=connection.cursor()
    r=int(ro.get())
    s="select * from employee where empno='%d'"
    args=(r)
    cur.execute(s%args)
    results = cur.fetchall()
    for i in results:
        print(i)

    connection.commit()
    connection.close()

def delete(event):

    connection=pymysql.connect(
        host="localhost",
        user="root",
        db="experiment"
        )

    cur=connection.cursor()
    r=int(ro.get())
    s="delete from employee where empno='%d'"
    args=(r)

    try:
        cur.execute(s%args)
        print("delete")
    except:
        print("something went wrong")

    connection.commit()
    connection.close()

window=Tk()
window.geometry("500x500")

lbl=Label(window, text="empno")
lbl.place(x=60,y=50)
ro=Entry(window)
ro.place(x=180,y=50)

btn=Button(window, text="read")
btn.place(x=200,y=160)
btn.bind('<Button-1>',read)

btn=Button(window, text="delete")
btn.place(x=200,y=200)
btn.bind('<Button-1>',delete)

