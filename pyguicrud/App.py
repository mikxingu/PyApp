from . import Users
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana" , "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.title = Label(self.container1, text="Informe os dados :")
        self.title["font"] = ("Calibri", "9", "bold")
        self.title.pack()

        self.lbluserid = Entry(self.container2, text="UserID", font=self.fonte, width=10)
        self.lbluserid.pack(side=LEFT)

        self.txtuserid = Entry(self.container2)
        self.txtuserid["width"] = 10
        self.txtuserid["font"] = self.fonte
        self.txtuserid.pack(side=LEFT)

        self.Findbtn = Button(self.container2, text="Find", font=self.fonte, width=10)
        self.Findbtn["commando"] = self.findUser
        self.Findbtn.pack(side=RIGHT)
        
        self.lblname = Label(self.container3, text="Name:", font=self.fonte, width=10)
        self.lblname.pack(side=LEFT)

        self.txtname = Entry(self.container3)
        self.txtname["width"] = 25
        self.txtname["font"] = self.fonte
        self.txtname.pack(side=LEFT)

        self.lblphone = Label(self.container4, text="Phone:", font=self.fonte, width=10)
        self.lblphone.pack(side=LEFT)

        self.txtphone = Entry(self.container4)
        self.txtphone["width"] = 25
        self.txtphone["font"] = self.fonte
        self.txtphone.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5) 
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lbluser = Label(self.container6, text="User:", font=self.fonte, width=10)
        self.lbluser.pack(side=LEFT)


        self.txtuser = Entry(self.container6)
        self.txtuser["width"] = 25
        self.txtuser["font"] = self.fonte
        self.txtuser.pack(side=LEFT)

        self.lblpassword = Label(self.container7, text="Password:", font=self.fonte, width=10)
        self.lblpassword.pack(side=LEFT)

        self.txtpassword = Entry(self.container7)
        self.txtpassword["width"] = 25
        self.txtpassword["show"] = "*"
        self.txtpassword["font"] = self.fonte
        self.txtpassword.pack(side=LEFT)

        self.btnInsert = Button(self.container8, text="Insert", font=self.fonte, width=12)
        self.btnInsert["command"] = self.insertUser
        self.btnInsert.pack(side=LEFT)

        self.btnChange = Button(self.container8, text="Change", font=self.fonte, width=12)
        self.btnChange["command"] = self.changeUser
        self.btnChange.pack(side=LEFT)

        self.btnExclude = Button(self.container8, text="Exclude", font=self.fonte, width=12)
        self.btnExclude["command"] = self.excludeUser
        self.btnExclude.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def insertUser(self):
        user = Users()

        user.name = self.txtname.get()
        user.phone = self.txtphone.get()
        user.email = self.txtemail.get()
        user.username = self.txtuser.get()
        user.password = self.txtpassword.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtuserid.delete(0, END)
        self.txtname.delete(0, END)
        self.txtphone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtuser.delete(0, END)
        self.txtpassword.delete(0, END)

    def changeUser(self):
        user = Users()
        user.userid = self.txtuserid.get()
        user.name = self.txtname.get()
        user.phone = self.txtphone.get()
        user.email = self.txtemail.get()
        user.username = self.txtuser.get()
        user.password = self.txtpassword.get()

        self.lblmsg["text"] = user.updateUser()
        
        self.txtuserid.delete(0, END)
        self.txtname.delete(0, END)
        self.txtphone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtuser.delete(0, END)
        self.txtpassword.delete(0, END)

    def excludeUser(self):
        user = Users()

        user.userid = self.txtuserid.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtuserid.delete(0, END)
        self.txtname.delete(0, END)
        self.txtphone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtuser.delete(0, END)
        self.txtpassword.delete(0, END)

    def findUser(self):
        user = Users()

        userid = self.txtuserid.get()

        self.lblmsg["text"] = user.SelectUser(userid)

        self.txtuserid.delete(0, END)
        self.txtuserid.insert(INSERT, user.userid)

        self.txtname.delete(0,END)
        self.txtname.insert(INSERT, user.name)

        self.txtphone.delete(0, END)
        self.txtphone.insert(INSERT, user.phone)

        self.txtemail.delete(0,END)
        self.txtemail.insert(INSERT, user.email)

        self.txtuser.delete(0, END)
        self.txtuser.insert(INSERT, user.username)

        self.txtpassword.delete(0, END)
        self.txtpassword.insert(INSERT, user.password)


    root = Tk()
    Application(root)
    root.mainloop()