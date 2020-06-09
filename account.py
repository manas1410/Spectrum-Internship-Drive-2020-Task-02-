from tkinter import *
import tkinter.font as font
import sqlite3
def main():
    new_account=Tk()
    new_account.geometry("420x460")
    new_account.title("New Account")
    new_account.iconbitmap("logo/spectrumlogo.ico")
    #all_Labels
    f=font.Font(family='Times New',size=20,weight='bold')
    create=Label(new_account,text="Create a new Account\n\n",fg='Blue',font=f)
    create.grid(row=0,column=0,columnspan=2)

    Label(new_account,text="*Please enter Your Details below").grid(row=0,column=0,columnspan=2)

    f1=font.Font(family='Times New',size=15,weight='bold')
    Label(new_account,text="             Full Name:",fg='red',font=f1).grid(row=1,column=0)
    full_name=Entry(new_account,width=35,borderwidth=2)
    full_name.grid(row=1,column=1,padx=0)

    

    Label(new_account,text="                 Branch:",fg='red',font=f1).grid(row=2,column=0)
    branch=Entry(new_account,width=35,borderwidth=2)
    branch.grid(row=2,column=1)

    Label(new_account,text="    Registration ID.:",fg='red',font=f1).grid(row=3,column=0)
    registration_id=Entry(new_account,width=35,borderwidth=2)
    registration_id.grid(row=3,column=1)

    Label(new_account,text="  Create Password:",fg='red',font=f1).grid(row=4,column=0)
    create_password=Entry(new_account,width=35,borderwidth=2)
    create_password.grid(row=4,column=1)

    Label(new_account,text="Confirm Password:",fg='red',font=f1).grid(row=5,column=0)
    confirm_password=Entry(new_account,width=35,borderwidth=2)
    confirm_password.grid(row=5,column=1)

    temp=Label(new_account,text=" ",pady=5)
    temp.grid(row=6,column=0,columnspan=2)
    def submit():
        name1=full_name.get()
        reg=registration_id.get()
        pas1=create_password.get()
        pas2=confirm_password.get()
        branch1=branch.get()
        l=[name1,pas1,pas2,reg,branch1]
        if(pas1!=pas2):
            temp['text']="Password does't match"
        elif(None in l or "" in l):
            temp['text']="Some fields are not enterted yet"
            
        else:
            cs=list(name1).count(" ")
            if(cs==0):
                s1=name1
            else:
                s=list(name1).index(" ")
                s1=str(name1)[:s:]
            s2=s1.lower()+reg[len(reg)-4:len(reg)]
            
            temp['text']="Your username is {} and password is {} \n Please press *Back* button to go back to login page".format(s2,pas1)
            
    def cancel():
        new_account.destroy()
        import welcome
        welcome.main()
    def back():
        name1=full_name.get()
        reg=registration_id.get()
        pas1=create_password.get()
        pas2=confirm_password.get()
        branch1=branch.get()
        cs=list(name1).count(" ")
        if(cs==0):
            s1=name1
        else:
            s=list(name1).index(" ")
            s1=str(name1)[:s:]
        s2=s1.lower()+reg[len(reg)-4:len(reg)]

            #database
        db=sqlite3.connect("user_pas.db")

            #cursor
        c=db.cursor()

            #insert into tabels
        c.execute("INSERT INTO user_pas VALUES(:username,:password)",
                      {
                          'username':s2,
                          'password':pas1
                          })

    
            #commit_changes
        db.commit()
            #close connection
        db.close()
        new_account.destroy()
        import welcome
        welcome.main()
        
    #allinputs
    global name1,name2,reg,pas1,pas2,branch1


    #buttons
    submit=Button(new_account,text="Submit",padx=100,pady=5,bg='red',font='Stylus',command=submit,borderwidth=3)
    submit.grid(row=7,column=0,columnspan=2)

    cancel=Button(new_account,text="Cancel",padx=50,pady=5,bg='blue',font='Stylus',command=cancel,borderwidth=3)
    cancel.grid(row=8,column=0,columnspan=2)

    back=Button(new_account,text="Back",padx=25,pady=5,bg='green',font='Stylus',command=back,borderwidth=3)
    back.grid(row=9,column=0,columnspan=2)
    new_account.mainloop()

if __name__=='__main__':
    main()
