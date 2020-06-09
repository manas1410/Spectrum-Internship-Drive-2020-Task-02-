from tkinter import *
import tkinter.font as font
import sqlite3
from PIL import ImageTk,Image
import webbrowser

def main():
    mark=Tk()
    mark.geometry("650x600")
    mark.title("Welcome")
    mark.iconbitmap("logo/spectrumlogo.ico")
    
        #font
    f=font.Font(family='Bookman Old Style',size=15,weight='bold')
    f_head=font.Font(family='Panthon Rust',size=16,weight='bold')

        #headline
    headline=Label(mark,text="Welcome To Student Mark Insertion and CGPA calculation ",fg='blue',font=f_head)
    headline.pack()

        #space
    space=Label(mark,text="\n\n\n\n\n\n\n\n\n")

    #Username
    name=Label(mark,text="User Name:",fg='red',font=f)
    enterusername=Entry(mark,width=30,borderwidth=5)
    space.pack()
    name.pack()
    enterusername.pack()

        #password
    password=Label(mark,text="Password:",fg='red',font=f)
    enterpassword=Entry(mark,width=30,borderwidth=5)
    password.pack()
    enterpassword.pack()
   
    us=enterusername.get()

    def submit():
        
        db=sqlite3.connect("user_pas.db")

            #cursor
        c=db.cursor()
        c.execute("SELECT *,oid FROM user_pas")
        records=c.fetchall()
        v=0
        for i in records:
            if(i[0]==enterusername.get() and i[1]==enterpassword.get()):
                v=1
        #commit_changes
        db.commit()
            #close connection
        db.close()
        
        
        if(v==1):
            db=sqlite3.connect("mark_list.db")
        #cursor
            

            #cursor
            c=db.cursor()
            c.execute("""DELETE from mark_list where name=' '""")
        #commit_changes
            db.commit()
            #close connection
            db.close()

            db=sqlite3.connect("mark_list.db")
            c=db.cursor()
        #insert into tabels
            c.execute("INSERT INTO mark_list VALUES(:user_name,:name,:registration_no,:branch,:chemistry,:math,:computer,:cgpa,:grade)",
                  {
                      'user_name':enterusername.get(),
                      'name':' ',
                      'registration_no':' ',
                      'branch':' ',
                      'chemistry':0,
                      'math':0,
                      'computer':0,
                      'cgpa':0,
                      'grade':' '
                      })


    
        #commit_changes
            db.commit()
        #close connection
            db.close()
            mark.destroy()
            import input_details
            input_details.main()
    
            
            
        else:
            import invalid
            invalid.main()
                
            

    def create():
        mark.destroy()
        import account
        account.main()
            


    #button
    f1=font.Font(family='Bookman Old Style',size=10,weight='bold')
    f2=font.Font(family='Bookman Old Style',size=5)
    submit=Button(mark,text="Submit",bg='green',font=f1,command=submit)
    create=Button(mark,text="Create an Account",bg='red',font=f1,command=create)
    o=Label(mark,text="or",font=f1)
    submit.pack()
    o.pack()
    create.pack()
    c1=Label(mark,text="*Create an Account if you don't have*")
    c1.pack()

    def call(url):
        webbrowser.open_new(url)
    photo=PhotoImage(file=r"logo/spectrumlogo.png")
    phtotoimage=photo.subsample(3,3)
    spectrum_bt=Button(mark,image=phtotoimage,command=lambda :call('https://spectrumcet.com/'))
    spectrum_bt.pack()   

    Label(mark,text="\n\n\n\nVisit our club website:",fg='blue',font=f1).pack()
    l=Label(mark,text="https://spectrumcet.com/",fg='blue',font=f1)
    l.bind("<Button-1>",lambda x:call('https://spectrumcet.com/'))
    l.pack()

    mainloop()
if __name__=='__main__':
    main()
