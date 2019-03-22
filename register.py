#Python Tkinter and Sqlite3 Login Form
#Made By Namah Jain Form Youtube Channel All About Code
#Please Subscribe To Our Youtube Channel.
#https://www.youtube.com/channel/UCUGAq4ALoWW4PDU6Cm1riSg?view_as=subscriber

#imports
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import os

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (FirstName TEXT NOT NULL,LastName TEXT NOT NULL,Email TEXT NOT NULL,username TEXT NOT NULL ,password TEXt NOT NULL);')
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.Email = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.n_FirstName = StringVar()
        self.n_LastName = StringVar()
        self.n_Email = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(FirstName,LastName,Email,username,password) VALUES(?,?,?,?,?)'
        c.execute(insert,[(self.n_FirstName.get()),(self.n_LastName.get()),(self.n_Email.get()),(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_FirstName.set('')
        self.n_LastName.set('')
        self.n_Email.set('')
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid(row=2,column=1)
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=3,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'First Name: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_FirstName,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Last Name: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_LastName,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(self.crf,text = 'Email: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_Email,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=3,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=4,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=5,column=1)

    

#create window and application object
root = Tk()
#root.title("Login Form")
main(root)
root.mainloop()