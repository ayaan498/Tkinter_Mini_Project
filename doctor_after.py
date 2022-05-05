from tkinter import *
from tkinter import ttk
root = Tk()
root.resizable(0,0)
root.configure(bg='#8EAAF3')
root.title('Virtual Health Assistant')
root.geometry('1500x1500')

def accept():
    root.destroy()
    import accept

def reject():
    root.destroy()
    import reject

# Widgets
l1 = Label(root,text='Welcome',font=('Gabriola',28,'bold'),bg='#8EAAF3')
b1 = Button(root,text='Accept Request',font=('Gabriola',20,'bold'),bg='#8EAAF3',width = 16,command=accept)
b2 = Button(root,text='Reject Request',font=('Gabriola',20,'bold'),bg='#8EAAF3',width = 16,command=reject)
l2 = Label(root,text='Your meeting link is - https://meet.google.com/kvd-tsvd-dqp',font=('Gabriola',20,'bold'),bg='#8EAAF3')
b3 = Button(root,text='Logout',font=('Gabriola',16,'bold'),bg='#8EAAF3',width = 15)


# Location
l1.place(x=650,y=0)
l2.place(x=450,y=470)
b1.place(x=460,y=260)
b2.place(x=760,y=260)
b3.place(x=1350,y=0)
root.mainloop()
