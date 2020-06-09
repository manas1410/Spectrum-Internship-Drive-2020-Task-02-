
from tkinter import *
import tkinter.font as font
import sqlite3

def main():
    sub=Tk()
    sub.title("Choose any Subject")
    sub.geometry("420x550")
    sub.iconbitmap("logo/spectrumlogo.ico")

    db=sqlite3.connect("mark_list.db")
    #cursor
    c=db.cursor()

    #query the database
    c.execute("SELECT *,oid FROM mark_list")
    records=c.fetchall()
    l=len(c.fetchall())
    n3=records[l-1][1]
    r3=records[l-1][2]
    b3=records[l-1][3]

    #commit_changes
    db.commit()
    #close connection
    db.close()
    f_new=font.Font(family='Times New',size=20,weight='bold')
    f1=font.Font(family='Times New',size=15,weight='bold')
    f2=font.Font(family='Times New',size=10,weight='bold')
    
    """n5=Label(sub,text='                 ',fg='green',font=f1)
    r5=Label(sub,text='                  ',fg='green',font=f1)
    b5=Label(sub,text='                 ',fg='green',font=f1)"""
    
    wel=Label(sub,text="Welcome\nYou may enter your marks\n\n",fg='blue',font=f_new).grid(row=0,column=0,columnspan=3)

    full_name1=Label(sub,text="Name:{}\n Registration ID:{}\n Branch:{} ".format(n3,r3,b3),font=f1,fg='purple').grid(row=1,column=0,columnspan=3)
    """n5['text']=n3
    n5.grid(row=1,column=2)


    branch=Label(sub,text="            Branch: ",font=f1,fg='purple').grid(row=2,column=0,columnspan=2)
    b5['text']=b3
    b5.grid(row=2,column=2)

    reg_no=Label(sub,text="Registration ID: ",font=f1,fg='purple').grid(row=3,column=0,columnspan=2)
    r5['text']=r3
    r5.grid(row=3,column=2)"""

    Label(sub,text=" \n\n").grid(row=3)
    
    
    def mark(text):
        import input_marks
        input_marks.sub=text
        input_marks.main()
    Label(sub,text='Click on the Respective Button to enter mark\n',fg='red',font=f2).grid(row=4,column=0,columnspan=3)
    #buttons
    chemistry=Button(sub,text='Chemistry',padx=5,pady=5,borderwidth=5,font=f1,fg='red',bg='yellow',command=lambda :mark("CHEMISTRY"))
    chemistry.grid(row=5,column=0)

    math=Button(sub,text='Math',padx=20,pady=5,borderwidth=5,fg='red',font=f1,bg='yellow',command=lambda :mark("MATH"))
    math.grid(row=5,column=1)

    computer=Button(sub,text='Computer',padx=5,pady=5,borderwidth=5,font=f1,fg='red',bg='yellow',command=lambda :mark("COMPUTER"))
    computer.grid(row=5,column=2)

    Label(sub,text="\n\n\n").grid(row=6)

    def submit():
        
        sub.destroy()
        import last
        last.main()

    def cancel():
        db=sqlite3.connect("mark_list.db")
        #cursor
        c=db.cursor()

        #query the database
        c.execute("SELECT *,oid FROM mark_list")
        records=c.fetchall()
        l=len(c.fetchall())
        n6=records[l-1][1]
        c.execute("""UPDATE mark_list SET chemistry=? WHERE name=?""",(0,n6))
        c.execute("""UPDATE mark_list SET math=? WHERE name=?""",(0,n6))
        c.execute("""UPDATE mark_list SET computer=? WHERE name=?""",(0,n6))
        c.execute("""UPDATE  mark_list SET registration_no=? WHERE name=?""",(' ',n6))
        c.execute("""UPDATE  mark_list SET branch=? WHERE name=?""",(' ',n6))
        c.execute("""UPDATE mark_list SET name=? WHERE name=?""",(' ',n6))

        #commit_changes
        db.commit()
        #close connection
        db.close()

        sub.destroy()
        import input_details
        input_details.main()

    submit_m=Button(sub,text='Submit',padx=10,pady=1,borderwidth=5,bg='green',font=f1,command=submit)
    submit_m.grid(row=7,column=0,columnspan=3)

    cancel=Button(sub,text='Cancel',padx=3,pady=1,borderwidth=5,bg='red',font=f2,command=cancel)
    cancel.grid(row=8,column=0,columnspan=3)

    mainloop()
if __name__=='__main__':
    main()
