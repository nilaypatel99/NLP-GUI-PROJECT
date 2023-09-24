#Starting app creation using api like SE,NER AND EMOTION DETECTION 
from tkinter import *
from mydb import Database
from tkinter import messagebox


class NLPApp:
    def __init__(self):
        #create a db obj
        self.dbo=Database()

        #login ka qui load karna
        self.root=Tk()   #tk class object
        self.root.title('sway')
        self.root.iconbitmap('images/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='gray')
        self.login_gui()
        self.root.mainloop()
    
    def login_gui(self):
        
        self.clear()
        self.root.configure(bg='gray')

        heading=Label(self.root,text='NLP APP',bg='gray',fg='white')
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))
        
        #Email
        label1=Label(self.root,text='Enter email')    #label for email 
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50) #used entry class to create a box and self cuz we'll use it somewhere
        self.email_input.pack(pady=(5,10),ipady=4)
        
        #Password
        label2=Label(self.root,text="Enter password")
        label2.pack(pady=(10,10))

        password=Entry(self.root,width=50,show='*')
        password.pack(pady=(5,10),ipady=4)
        
        #Login
        login=Button(self.root,text='login',width=30,height=2)    #Button class to create login 
        login.pack(pady=(10,10))

        label3=Label(self.root,text='Not a user ?')
        label3.pack(pady=(10,10),ipady=4)
        
        #Register
        redirect_btn=Button(self.root,text='Register Now',width=30,height=2,command=self.register_gui)
        redirect_btn.pack(pady=(10,10))
        
    def register_gui(self):

        self.clear()
        self.root.configure(bg='#34495E')

        heading=Label(self.root,text='NLP APP',bg='#34495E',fg='white')
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))
        
        #Name
        label0=Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))

        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        #Email
        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(10,10),ipady=4)

        #Password
        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password=Entry(self.root,width=50,show='*')
        self.password.pack(pady=(10,30),ipady=4)

        #Button
        register_btn=Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        #login
        label3=Label(self.root,text='Already a user?')
        label3.pack(pady=(10,10))

        redirect_btn=Button(self.root,text='Login Now',width=30,height=2,command=self.login_gui)
        redirect_btn.pack(pady=(10,10))
        
    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name=self.name_input.get()   #get function get the data from gui
        email=self.email_input.get()
        password=self.password.get()

        response=self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('success','Login successful')
        else:
            messagebox.showerror('Error','Email Already exists')

nlp=NLPApp()



