from tkinter import *
from dbhelper1 import DBhelper
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
import shutil,os


class Login :

    def __init__(self):
        self.db=DBhelper()
        self.root = Tk()

        self.root.title('My Login App')
        self.root.configure(background='#7D05FC')

        self.root.minsize(300, 500)
        self.root.maxsize(300, 500)
        self.load_gui()

    def load_gui(self) :
        self.clear()

        self.label1 = Label(self.root, text = 'Tinder',fg = 'white',bg = '#7D05FC')
        self.label1.configure(font = ('Times', 30,'bold'))
        self.label1.pack(pady = (10,10))

        self.label2 = Label(self.root, text = 'Email',fg = 'white',bg = '#7D05FC')
        self.label2.configure(font = ('Times', 30,'italic'))
        self.label2.pack(pady = (5,5))

        self.email = Entry (self.root)
        self.email.pack(pady = (0,10),ipadx= 30,ipady = 5)
        self.email.focus()
        self.email.bind("<Return>",lambda event :self.password.focus())

        self.label3 = Label(self.root, text = 'Password',fg = 'white',bg = '#7D05FC')
        self.label3.configure(font = ('Times', 30,'italic'))
        self.label3.pack(pady = (5,5))

        self.password = Entry (self.root)
        self.password.pack(pady = (0,10),ipadx= 30,ipady = 5)
        self.password.bind("<Return>",lambda event :self.btn_click())

        self.login = Button(self.root,text = 'Login',bg = 'white', command =lambda : self.btn_click())
        self.login.pack(pady=(5,10),ipadx=70,ipady = 4)

        self.label4=Label(self.root,text="Not a member? Sign Up",fg="white",bg="#7D05FC")
        self.label4.configure(font=('Times', 12, 'italic'))
        self.label4.pack(pady=(5, 5))

        self.register = Button(self.root, text='Sign Up', bg='white', command=lambda : self.register_gui())
        self.register.pack(pady=(5, 10), ipadx=40, ipady=2)

        self.root.mainloop()

    def register_gui(self):
        self.clear()

        self.label0 = Label(self.root, text='Tinder', fg='white', bg='#7D05FC')
        self.label0.configure(font=('Times', 30, 'bold'))
        self.label0.pack(pady=(10, 10))

        self.label1 = Label(self.root, text='Name', fg='white', bg='#7D05FC')
        self.label1.configure(font=('Times', 30, 'italic'))
        self.label1.pack(pady=(5, 5))

        self.name = Entry(self.root)
        self.name.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.name.focus()
        self.name.bind("<Return>",lambda event :self.email.focus())

        self.label2 = Label(self.root, text='Email', fg='white', bg='#7D05FC')
        self.label2.configure(font=('Times', 30, 'italic'))
        self.label2.pack(pady=(5, 5))

        self.email = Entry(self.root)
        self.email.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.email.bind("<Return>",lambda event :self.password.focus())

        self.label3 = Label(self.root, text='Password', fg='white', bg='#7D05FC')
        self.label3.configure(font=('Times', 30, 'italic'))
        self.label3.pack(pady=(5, 5))

        self.password = Entry(self.root)
        self.password.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.password.bind("<Return>",lambda event :self.reg_submit())

        self.filebtn=Button(self.root,text="Upload Profile Picture",command=lambda : self.upload_file())
        self.filebtn.pack(pady=(0, 5))

        self.filename=Label(self.root)
        self.filename.pack(pady=(0,5))

        self.register = Button(self.root, text='Sign Up', bg='white', command=lambda: self.reg_submit())
        self.register.pack(pady=(5, 10), ipadx=70, ipady=4)

        self.label4 = Label(self.root, text="Already a member? Login", fg="white", bg="#7D05FC")
        self.label4.configure(font=('Times', 12, 'italic'))
        self.label4.pack(pady=(5, 5))

        self.login = Button(self.root, text='Login', bg='white', command=lambda: self.load_gui())
        self.login.pack(pady=(5, 10), ipadx=40, ipady=2)

    def upload_file(self): 
        filename=filedialog.askopenfilename(initialdir="/images",title="Choose File")
        self.filename.configure(text=filename)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def btn_click(self):
        email = self.email.get()
        password = self.password.get()
        data = self.db.check_login(email,password)
        if len(data)>0:
            self.clear()
            self.user_data=data[0]
            self.user_id = self.user_data[0]
            self.user_email=self.user_data[2]
            self.user_password=self.user_data[3]
            self.load_user_info()
        else :
            messagebox.showerror("Error","Invalid Email/Password")

    def load_user_info(self):
        self.main_window(self.user_data)

    def main_window(self,data,mode=1,index=None,num=None):  
        self.clear()
        self.navbar()

        if mode ==3:
            self.label0=Label(self.root,text="Your Proposals Are : ",fg='black', bg='#7D05FC')
            self.label0.configure(font=('Times', 20, 'bold','underline'))
            self.label0.pack(pady=(10, 10))

        if mode ==4:
            self.label0=Label(self.root,text="Your Requests Are : ",fg='black', bg='#7D05FC')
            self.label0.configure(font=('Times', 20, 'bold','underline'))
            self.label0.pack(pady=(10, 10))

        if mode ==5:
            self.label0=Label(self.root,text="Your Matches Are : ",fg='black', bg='#7D05FC')
            self.label0.configure(font=('Times', 20, 'bold','underline'))
            self.label0.pack(pady=(10, 10))

        if data[8]!='':
            imageUrl="images/{}".format(data[8])

            load=Image.open(imageUrl)
            load=load.resize((200,200),Image.ANTIALIAS)
            render=ImageTk.PhotoImage(load)
            img=Label(image=render)
            img.image=render
            img.pack()

        self.label1=Label(self.root,text="Name : "+data[1],fg='white', bg='#7D05FC')
        self.label1.configure(font=('Times', 15, 'bold'))
        self.label1.pack(pady=(10, 10))

        if len(data[7])!=0:
            self.label2 = Label(self.root, text="From : " + data[7], fg='white', bg='#7D05FC')
            self.label2.configure(font=('Times', 15, 'bold'))
            self.label2.pack(pady=(10, 10))

        if len(data[6])!= 0:
            self.label3 = Label(self.root, text="Not interested in : " + data[6], fg='white', bg='#7D05FC')
            self.label3.configure(font=('Times', 15, 'bold'))
            self.label3.pack(pady=(10, 10))

        if len(data[4])!= 0:
            self.label4 = Label(self.root, text="About Me : " + data[4], fg='white', bg='#7D05FC')
            self.label4.configure(font=('Times', 15))
            self.label4.pack(pady=(10, 10))

        if mode!=1:
            frame=Frame(self.root)
            frame.pack()

            if index!=0:
                if mode==0:
                    previous=Button(frame,text="Previous",command=lambda :self.view_others(index=index-1))
                    previous.pack(side='left')
                elif mode==3:
                    previous=Button(frame,text="Previous",command=lambda :self.view_proposals(index=index-1))
                    previous.pack(side='left')
                elif mode ==4:
                    previous=Button(frame,text="Previous",command=lambda :self.view_requests(index=index-1))
                    previous.pack(side='left')
                elif mode ==5:
                    previous=Button(frame,text="Previous",command=lambda :self.view_matches(index=index-1))
                    previous.pack(side='left')

            if mode==0 or mode==4:
                propose=Button(frame,text='Propose',command=lambda :self.propose(self.user_id,data[0]))
                propose.pack(side='left')

            if index!=(num-1):
                if mode==0:
                    next1=Button(frame,text='Next',command=lambda :self.view_others(index=index+1))
                    next1.pack(side='left')
                elif mode==3:
                    next1=Button(frame,text='Next',command=lambda :self.view_proposals(index=index+1))
                    next1.pack(side='left')
                elif mode ==4:
                    next1=Button(frame,text='Next',command=lambda :self.view_requests(index=index+1))
                    next1.pack(side='left')
                elif mode ==5:
                    next1=Button(frame,text='Next',command=lambda :self.view_matches(index=index+1))
                    next1.pack(side='left')

        

    def navbar(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        filemenu = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile",command=lambda : self.main_window(self.user_data))
        filemenu.add_command(label="Edit Profile", command=lambda: self.edit_profile())
        filemenu.add_command(label="View Profile",command = lambda : self.view_others())
        filemenu.add_command(label="Update Profile Picture",command = lambda : self.update_dp())
        filemenu.add_command(label="Change Password", command=lambda: self.change_password())
        filemenu.add_command(label="LogOut", command=lambda: self.logout())

        helpmenu = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals",command=lambda :self.view_proposals())
        helpmenu.add_command(label="My Requests",command=lambda :self.view_requests())
        helpmenu.add_command(label="My Matches",command=lambda :self.view_matches())

    def logout(self):
        self.user_id=""
        self.user_data=""
        emptymenu=Menu(self.root)
        self.root.config(menu=emptymenu)
        self.load_gui()

    def edit_profile(self):
        self.clear()

        self.label0 = Label(self.root, text='Edit Profile :', fg='white', bg='#7D05FC')
        self.label0.configure(font=('Times', 15, 'bold'))
        self.label0.pack(pady=(10, 10))

        self.label1 = Label(self.root, text='Bio :', fg='white', bg='#7D05FC')
        self.label1.configure(font=('Times', 10, 'italic'))
        self.label1.pack(pady=(5, 5))

        self.bio = Entry(self.root)
        self.bio.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.bio.insert(0,self.user_data[4])
        self.bio.focus()
        self.bio.bind("<Return>",lambda event :self.age.focus())

        self.label2 = Label(self.root, text='Age :', fg='white', bg='#7D05FC')
        self.label2.configure(font=('Times', 10, 'italic'))
        self.label2.pack(pady=(5, 5))

        self.age = Entry(self.root)
        self.age.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.age.insert(0,self.user_data[5])
        self.age.bind("<Return>",lambda event :self.gender.focus())

        self.label3 = Label(self.root, text='Gender :', fg='white', bg='#7D05FC')
        self.label3.configure(font=('Times', 10, 'italic'))
        self.label3.pack(pady=(5, 5))

        self.gender = Entry(self.root)
        self.gender.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.gender.insert(0,self.user_data[6])
        self.gender.bind("<Return>",lambda event :self.city.focus())

        self.label4 = Label(self.root, text='City :', fg='white', bg='#7D05FC')
        self.label4.configure(font=('Times', 10, 'italic'))
        self.label4.pack(pady=(5, 5))

        self.city = Entry(self.root)
        self.city.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.city.insert(0,self.user_data[7])
        self.city.bind("<Return>",lambda event :self.update_profile())

        self.edit = Button(self.root, text='Edit', bg='white', command=lambda: self.update_profile())
        self.edit.pack(pady=(5, 10), ipadx=70, ipady=4)

    def update_profile(self):
        bio=self.bio.get()
        age=self.age.get()
        gender=self.gender.get()
        city=self.city.get()

        info=[bio,age,gender,city]
        response = self.db.update_profile(self.user_id,info)

        if response ==1:
            messagebox.showinfo("Success","Profile Updated")
            data=self.db.check_login(self.user_email,self.user_password)
            self.user_data=data[0]
            self.main_window(self.user_data)
        else :
            messagebox.showerror("Error","Some Error occured!")
    
    def update_dp(self):
        self.clear()
        self.filebtn=Button(self.root,text="Choose File",command=lambda : self.upload_file())
        self.filebtn.pack(pady=(10, 20))

        self.filename=Label(self.root,bg='#7D05FC',fg='white')
        self.filename.pack(pady=(5,10))

        self.btn=Button(self.root,text="Update",bg='white',fg='black',command=lambda :self.update_btn())
        self.btn.pack(pady=(5,10))

    def update_btn(self):
        filename=self.filename['text'].split("/")[-1]

        if filename!='':
            response=self.db.update_dp(self.user_id,filename)
            if response==1:
                messagebox.showinfo("Successfull","Profile Picture Successfully Updated")
                shutil.copyfile(self.filename['text'],'C:\\Users\\admin\\PycharmProjects\\finder\\images\\'+ filename)
                if self.user_data[8]!='':
                    os.remove("C:/Users/admin/PycharmProjects/finder/images/"+self.user_data[8])
                data=self.db.check_login(self.user_email,self.user_password)
                self.user_data=data[0]
                self.main_window(self.user_data)
            else :
                messagebox.showerror("Error","Some Database Error Occured")
        else:
            messagebox.showwarning("Sorry","Select a Picture First")
    
    def view_others(self,index=0):
        data=self.db.fetch_others(self.user_id)
        data1=self.view_proposals(mode=6)
        if data1==[]:
            num=len(data)
            self.main_window(data[index],mode=0,index=index,num=num)
        else :
            new_data=[]
            for i in data:
                if i not in data1:
                    new_data.append(i)
            num=len(new_data)
            self.main_window(new_data[index],mode=0,index=index,num=num)

    def propose(self,romeo_id,juliet_id):
        response=self.db.propose(romeo_id,juliet_id)

        if response==1:
            messagebox.showinfo("Success",'Proposal sent successfully.Fingers Crossed')
            data=self.db.check_login(self.user_email,self.user_password)
            self.user_data=data[0]
            self.view_others()
        elif response==-1:
            messagebox.showerror("Sorry","You Have Already Proposed This User")
        else :
            messagebox.showerror("Error","Some Error Occured")

    def view_proposals(self,index=0,mode=3):
        data=self.db.view_proposals(self.user_id)
        new_data=[]
        for i in data :
            new_data.append(i[3:])
        num=len(new_data)
        if mode ==3:
            if new_data!=[]:
                self.main_window(new_data[index],mode=3,index=index,num=num)
            else:
                messagebox.showerror("Sorry","You haven't any Proposals")
        elif mode==6:
            return new_data

    def view_requests(self,index=0):
        data=self.db.view_requests(self.user_id)
        new_data=[]
        for i in data :
            new_data.append(i[3:])
        num=len(new_data)
        if new_data!=[]:
            self.main_window(new_data[index],mode=4,index=index,num=num)
        else:
            messagebox.showerror("Sorry","You haven't any Requests")

    def view_matches(self,index=0):
        data1=self.db.view_proposals(self.user_id)
        new_data1=[]
        for i in data1 :
            new_data1.append(i[3:])
        
        data2=self.db.view_requests(self.user_id)
        new_data2=[]
        for i in data2 :
            new_data2.append(i[3:])

        new_data=[]
        if new_data1!=[] and new_data2!=[]:
            for i in range (len(new_data1)):
                for j in range(len(new_data2)):
                    if new_data1[i][0]==new_data2[j][0]:
                        new_data.append(new_data1[i])

        num=len(new_data)
        if new_data!=[]:
            self.main_window(new_data[index],mode=5,index=index,num=num)
        else:
            messagebox.showerror("Sorry","You haven't any Matches")

    def change_password(self):
        self.clear()

        self.label0 = Label(self.root, text='Old Password :', fg='white', bg='#7D05FC')
        self.label0.configure(font=('Times', 10, 'italic'))
        self.label0.pack(pady=(5, 5))

        self.old_password = Entry(self.root)
        self.old_password.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.old_password.focus()
        self.old_password.bind("<Return>",lambda event :self.new_password.focus())

        self.label1 = Label(self.root, text='New Password :', fg='white', bg='#7D05FC')
        self.label1.configure(font=('Times', 10, 'italic'))
        self.label1.pack(pady=(5, 5))

        self.new_password = Entry(self.root)
        self.new_password.pack(pady=(0, 10), ipadx=30, ipady=5)
        self.new_password.bind("<Return>",lambda event :self.change_password_func())

        self.change_password_button = Button(self.root, text='Change Password', bg='white',command=lambda: self.change_password_func())
        self.change_password_button.pack(pady=(5, 10), ipadx=70, ipady=4)

    def change_password_func(self):
        old_password=self.old_password.get()
        new_password=self.new_password.get()
        if old_password == self.user_data[3] :
            response = self.db.change_password(self.user_id,new_password)

            if response == 1:
                messagebox.showinfo("Successful","Password Changed Successfull")
                self.clear()
                self.main_window(self.user_data)
            else:
                messagebox.showerror("Error","Some Error Occured!")
        else :
            messagebox.showerror("Error","Please Enter Valid older Password")
            self.change_password()

    def reg_submit(self):
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        filename=self.filename['text'].split("/")[-1]

        if filename!="":
            response = self.db.insert_user(name,email, password,filename)
        else :
            response = self.db.insert_user(name,email, password)

        if response == 1:
            messagebox.showinfo("Registration successful", 'You may Login now')
            if filename=="":
                pass
            else:
                shutil.copyfile(self.filename['text'],'C:\\Users\\admin\\PycharmProjects\\finder\\images\\'+ filename)
            self.load_gui()
        else:
            messagebox.showerror('Error', 'Database Error')

        # self.name.delete(0,END)
        # self.email.delete(0, END)
        # self.password.delete(0, END)


obj = Login()