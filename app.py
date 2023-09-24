#Starting app creation using api like SE,NER AND EMOTION DETECTION 
from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import Api


class NLPApp:
    def __init__(self):
        #create a db obj
        self.dbo=Database()
        self.apio=Api()

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

        self.password=Entry(self.root,width=50,show='*')
        self.password.pack(pady=(5,10),ipady=4)
        
        #Login
        login=Button(self.root,text='login',width=30,height=2,command=self.perform_login)    #Button class to create login 
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
            messagebox.showinfo('success','Registration successful')
        else:
            messagebox.showerror('Error','Email Already exists')

    def perform_login(self):
        email=self.email_input.get()
        password=self.password.get()

        response=self.dbo.search(email,password)
        if response==1:
            messagebox.showinfo('success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password')

    def home_gui(self):

        self.clear()
        self.root.configure(bg='#7393B3')

        heading=Label(self.root,text='NLPApp',bg='#7393B3',fg='#E5E4E2')
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))

        #Sentiment Analysis
        sentiment_btn=Button(self.root,text="Sentiment Analysis",width=30,height=2,command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))
       
        #Named Entity Recognition
        ner_btn=Button(self.root,text='Named Entity Recognition',width=30,height=2)
        ner_btn.pack(pady=(10,10))
        
        #Emotion Prediction
        emotion_btn=Button(self.root,text='Emotion Prediction',width=30,height=2)
        emotion_btn.pack(pady=(10,10))

        #Logout button
        logout_btn=Button(self.root,text="logout",command=self.login_gui)
        logout_btn.pack(pady=(10,10))


    def sentiment_analysis(self):
        self.clear()
        self.root.configure(bg='#8A9A5B')

        heading=Label(self.root,text='NLP APP',bg='#8A9A5B',fg='white')
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#8A9A5B', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))
        
        #Enter box
        label1=Label(self.root,text='Enter the text')
        label1.pack(pady=(10,10))

        self.text=Entry(self.root,width=50)
        self.text.pack(pady=(20,10),ipady=3)

        #Sentiment analyse button
        sentiment_btn=Button(self.root,text='Analyze Sentiment',width=30,height=2,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))
     
        #Result section
        self.sentiment_result=Label(self.root,text=' ',bg='#8A9A5B',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',14))

        goback_btn=Button(self.root,text='Go back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))


    def do_sentiment_analysis(self):

        text=self.text.get()    #to get the text inputed from user
        result=self.apio.sentiment_analysis(text)   #we're providing text to sentiment_analysis function of myapi class

        




nlp=NLPApp()



