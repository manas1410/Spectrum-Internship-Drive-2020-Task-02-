from tkinter import*
import tkinter.font as font
import sqlite3

name2=''
regis2=''
branch2=''
def main():
    inp=Tk()
    inp.geometry("430x300")
    inp.title("Enter The Details")
    inp.iconbitmap("logo/spectrumlogo.ico")
    
    f=font.Font(family='Bookman Old Style',size=15,weight='bold')
    f1=font.Font(family='Bookman Old Style',size=20,weight='bold')
    global n2
    global reg2
    global b2

    det=Label(inp,text="    Enter The Details\n",font=f1,fg='magenta')
    det.grid(row=0,column=0,columnspan=2)

    n1=Label(inp,text="               Name:",font=f)
    n1.grid(row=1,column=0)

    n2=Entry(inp,width=40)
    n2.grid(row=1,column=1)

    reg1=Label(inp,text="Registration ID:",font=f)
    reg1.grid(row=2,column=0)

    reg2=Entry(inp,width=40)
    reg2.grid(row=2,column=1)

    b1=Label(inp,text="            Branch:",font=f)
    b1.grid(row=3,column=0)

    b2=Entry(inp,width=40)
    b2.grid(row=3,column=1)


    invalid=Label(inp,text=' ',fg='red')
    invalid.grid(row=4,columnspan=2)

    
    
    def submit():
        name2=n2.get()
        regis2=reg2.get()
        branch2=b2.get()
        
        l=[name2,regis2,branch2]
        if (None in l or "" in l):
            invalid['text']="Please fill all the fields"
            
            
        else:
            db=sqlite3.connect("mark_list.db")
        #cursor
            c=db.cursor()
        #insert into tabels
            c.execute("""UPDATE mark_list SET name=? WHERE name=?""",(name2,' '))
            c.execute("""UPDATE  mark_list SET registration_no=? WHERE registration_no=?""",(regis2,' '))
            c.execute("""UPDATE  mark_list SET branch=? WHERE branch=?""",(branch2,' '))
            


    
        #commit_changes
            db.commit()
        #close connection
            db.close()
       
            inp.destroy()
            import subject
            subject.main()

    def back():
        db=sqlite3.connect("mark_list.db")

            #cursor
        c=db.cursor()
        c.execute("""DELETE from mark_list where name=' '""")
        #commit_changes
        db.commit()
            #close connection
        db.close()
        
        inp.destroy()
        import welcome
        welcome.main()
    
    #buttons
    sub1=Button(inp,text="Submit",borderwidth=3,padx=40,font=f,bg='green',command=submit)
    sub1.grid(row=5,column=0,columnspan=2)

    back1=Button(inp,text="Back",borderwidth=3,padx=20,font=f,bg='red',command=back)
    back1.grid(row=6,column=0,columnspan=2)
    inp.mainloop()

         
    
if __name__=='__main__':
    main()


