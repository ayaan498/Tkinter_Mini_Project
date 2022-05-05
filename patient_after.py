from tkinter import *
import sqlite3
root = Tk()
root.resizable(0,0)
root.configure(bg='#8EAAF3')
root.title('Virtual Health Assistant')
root.geometry('1500x1500')

conn = sqlite3.connect('applicant_database.db')
c = conn.cursor()
c.execute("""
        CREATE TABLE if not exists Applicant
        (
            username text,
            email text
        )
        """
)
conn.commit()
conn.close()

def submit():
    conn = sqlite3.connect('applicant_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Applicant VALUES(:username,:email)",
    {
        'username':e1.get(),
        'email':e2.get()
    })
    conn.commit()
    conn.close()
    root.destroy()
    import thank_you

def clear():
    e1.delete(0,END)
    e2.delete(0,END)

# Widgets
l1 = Label(root,text='Welcome',font=('Gabriola',28,'bold'),bg='#8EAAF3')
b3 = Button(root,text='Logout',font=('Gabriola',16,'bold'),bg='#8EAAF3',width = 15)

specialization = ["Dr.Batra"]
clicked = StringVar()
clicked.set("Dr.Batra")
# Widgets

l6 = Label(root,text='Full Name',font=('Gabriola',26,'bold'),bg='#8EAAF3')
l2 = Label(root,text='E-Mail',font=('Gabriola',26,'bold'),bg='#8EAAF3')
l7 = Label(root,text='Doctor',font=('Gabriola',26,'bold'),bg='#8EAAF3')
e1 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=3)
e2 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=3)
d1 = OptionMenu(root, clicked, *specialization)
b1 = Button(root,text='Submit',font=('time',14),bg='#8EAAF3',command=submit,width=8)
b2 = Button(root,text='Clear',font=('time',14),bg='#8EAAF3',command=clear,width=8)

# Location
l6.place(x=550,y=100)
e1.place(x=700,y=120)
l2.place(x=550,y=185)
e2.place(x=700,y=205)

l7.place(x=550,y=265)
d1.place(x=750,y=283)
b1.place(x=600,y=385)
b2.place(x=780,y=385)

# Location
l1.place(x=650,y=0)
b3.place(x=1350,y=0)
root.mainloop()
