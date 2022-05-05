from tkinter import *
from turtle import width
import sqlite3

root = Tk()
root.resizable(0,0)
root.configure(bg='#8EAAF3')
root.title('Virtual Health Assistant')
root.geometry('1500x1400')
conn = sqlite3.connect('doctor_database.db')
c = conn.cursor()
c.execute("""
        CREATE TABLE if not exists Doctor
        (
            username text,
            password varchar(20)
        )
        """
)
conn.commit()
conn.close()

def submit():
    conn = sqlite3.connect('doctor_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Doctor VALUES(:username,:password)",
    {
        'username':e1.get(),
        'password':e3.get()
    })
    conn.commit()
    conn.close()
    root.destroy()
    import doctor_login_page

def clear():
    e1.delete(0,END)

def patient_reg_page():
    root.destroy()
    import patient_reg_page

specialization = ["Eye Specialist","Dentist", "Cardiologist","General Physician"]
clicked = StringVar()
clicked.set("Eye Specialist")

# Widgets
l5 = Label(root,text='Join Virtual Health Assistant',font=('Gabriola',28,'bold'),bg='#8EAAF3')
l1 = Label(root,text='Full Name',font=('Gabriola',26,'bold'),bg='#8EAAF3')

l3 = Label(root,text='Gender',font=('Gabriola',26,'bold'),bg='#8EAAF3')
l6 = Button(root,text='Not a Doctor?',font=('',12,'bold'),bg='#8EAAF3', command = patient_reg_page, width = 20)
l7 = Label(root,text='Specialization',font=('Gabriola',26,'bold'),bg='#8EAAF3')
l4 = Label(root,text='Password',font=('Gabriola',26,'bold'),bg='#8EAAF3')
e1 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=3)

e3 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=3,show='*')
e4 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=3)
d1 = OptionMenu(root, clicked, *specialization)
b1 = Button(root,text='Submit',font=('time',14),bg='#8EAAF3',command=submit,width=8)
b2 = Button(root,text='Clear',font=('time',14),bg='#8EAAF3',command=clear,width=8)

# Location
l1.place(x=550,y=100)
e1.place(x=700,y=120)
l4.place(x=550,y=185)
e3.place(x=700,y=205)
b2.place(x = 800, y= 356)
b1.place(x = 600, y= 356)
l7.place(x=550,y=265)
d1.place(x=750,y=283)
l5.place(x=650,y=0)
l6.place(x=640,y=415)
#b2.place(x=820,y=415)
#l6.place(x=700,y=485)

root.mainloop()
