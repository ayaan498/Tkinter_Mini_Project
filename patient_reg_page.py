from tkinter import *
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('patient_database.db')
c = conn.cursor()
c.execute("""
        CREATE TABLE if not exists Patient
        (
            username text,
            password varchar(20)
        )
        """
)
conn.commit()
conn.close()

root = Tk()
root.resizable(0,0)
root.configure(bg='#8EAAF3')
root.title('Virtual Health Assistant')
root.geometry('1500x1400')

def clear():
    e1.delete(0,END)

    e3.delete(0,END)

def doctor_reg_page():
    root.destroy()
    import doctor_reg_page

def submit():
    conn = sqlite3.connect('patient_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Patient VALUES(:username,:password)",
    {
        'username':e1.get(),
        'password':e3.get()
    })
    conn.commit()
    conn.close()
    root.destroy()
    import patient_login_page

def queries():
    conn = sqlite3.connect('patient_database.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM Patient")
    records = c.fetchall()
    print_records = ''
    for i in range(len(records)):
        print_records += str(records[i]) + " \n"
    query_label = Label(root,text=print_records,font=('Gabriola',13,'bold'),bg='#8EAAF3')
    query_label.place(x = 700, y = 650)
    conn.commit()
    conn.close()

# Widgets
l5 = Label(root,text='Join Virtual Health Assistant',font=('Gabriola',28,'bold'),bg='#8EAAF3')
l1 = Label(root,text='Full Name',font=('Gabriola',26,'bold'),bg='#8EAAF3')
l6 = Button(root,text='Are you a Doctor? Register Here',font=('',12,'bold'),bg='#8EAAF3',command = doctor_reg_page, width = 29)

l4 = Label(root,text='Password',font=('Gabriola',26,'bold'),bg='#8EAAF3')
e1 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=2)

e3 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=2,show='*')
e4 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=2)
b1 = Button(root,text='Submit',font=('time',14),bg='#8EAAF3',command=submit,width=8)
b2 = Button(root,text='Clear',font=('time',14),bg='#8EAAF3',command=clear,width=8)

# Location
l1.place(x=550,y=100)
e1.place(x=700,y=120)
e3.place(x=700,y=195)
l4.place(x=550,y=180)
l5.place(x=650,y=0)
b1.place(x=660,y=285)
b2.place(x=820,y=285)
l6.place(x=640,y=365)
root.mainloop()
