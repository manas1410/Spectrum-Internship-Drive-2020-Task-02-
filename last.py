from tkinter import*
import website
import tkinter.font as font
from PIL import ImageTk,Image
import os
import sqlite3
import webbrowser

def main():
    cgnc=Tk()
    cgnc.title('Show')
    cgnc.iconbitmap("logo/spectrumlogo.ico")
    f=font.Font(family='Bookman Old Style',size=10,weight='bold')
    f1=font.Font(family='Bookman Old Style',size=10)

    db=sqlite3.connect("mark_list.db")
    #cursor
    c=db.cursor()

    #query the database
    c.execute("SELECT *,oid FROM mark_list")
    records=c.fetchall()
    l=len(c.fetchall())
    ch=records[l-1][4]
    ma=records[l-1][5]
    co=records[l-1][6]
    us=records[l-1][0]

    #commit_changes
    db.commit()
    #close connection
    db.close()

    def cgpa():
        cg1=((ch+ma+co)/3)/9.5
        cg="{:.2f}".format(cg1)
        db=sqlite3.connect("mark_list.db")
        c=db.cursor()

        #query the database
        c.execute("SELECT *,oid FROM mark_list")
        records=c.fetchall()
        l=len(c.fetchall())
        n6=records[l-1][1]
        c.execute("""UPDATE mark_list SET cgpa=? WHERE name=?""",(cg,n6))

        #commit_changes
        db.commit()
        #close connection
        db.close()
        entry.delete(0,END)
        entry.insert(0,cg)

    def grad():
        av=((ch+ma+co)/3)
        if av<=100 and av>=90:
            gr='O'
        elif av<90 and av>=80:
            gr='E'
        elif av<80 and av>=70:
            gr='A'
        elif av<70 and av>=60:
            gr='B'
        elif av<60 and av>=50:
            gr='C'
        elif av<50 and av>=40:
            gr='D'
        elif av<40:
            gr='F'
        db=sqlite3.connect("mark_list.db")
        c=db.cursor()

        #query the database
        c.execute("SELECT *,oid FROM mark_list")
        records=c.fetchall()
        l=len(c.fetchall())
        n6=records[l-1][1]
        c.execute("""UPDATE mark_list SET grade=? WHERE name=?""",(gr,n6))

        #commit_changes
        db.commit()
        #close connection
        db.close()    
        entry.delete(0,END)
        entry.insert(0,gr)
        
    #buttons
    cgpa=Button(cgnc,text='CGPA',bg='yellow',fg='black',borderwidth=3,padx=25,pady=20,command=cgpa,font=f)
    cgpa.grid(row=0,column=0)

    grade=Button(cgnc,text='GRADE',bg='yellow',fg='black',borderwidth=3,padx=20,pady=20,command=grad,font=f)
    grade.grid(row=0,column=1)

    Label(cgnc,text="\n").grid(row=1)

    def new():
        db=sqlite3.connect("mark_list.db")
        #cursor
        c=db.cursor()
        #insert into tabels
        c.execute("INSERT INTO mark_list VALUES(:user_name,:name,:registration_no,:branch,:chemistry,:math,:computer,:cgpa,:grade)",
                  {
                      'user_name':us,
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
        cgnc.destroy()
        import input_details
        input_details.main()
        
        
    def close():
        os._exit(1)

    new_input=Button(cgnc,text='New Input',bg='yellow',fg='black',borderwidth=3,padx=10,pady=20,command=new,font=f)
    new_input.grid(row=2,column=0)

    close=Button(cgnc,text='Close',bg='yellow',fg='black',borderwidth=3,command=close,padx=20,pady=20,font=f)
    close.grid(row=2,column=1)

    Label(cgnc,text="\n").grid(row=3)

    entry=Entry(cgnc,borderwidth=3,width=44)
    entry.grid(row=4,column=0,columnspan=2,padx=20)

    def show_en():
        show_ent=Toplevel()
        show_ent.geometry("600x450")
        db=sqlite3.connect("mark_list.db")
    #cursor
        c=db.cursor()
        
    #query the database
        c.execute("SELECT *,oid FROM mark_list")
        records=c.fetchall()
        f=font.Font(family='Bookman Old Style',size=10,weight='bold')
        l=len(c.fetchall())
        Label(show_ent,text="Username",font=f,fg='red').grid(row=0,column=0)
        Label(show_ent,text="Name",font=f,fg='red').grid(row=0,column=1)
        Label(show_ent,text="Registration ID",font=f,fg='red').grid(row=0,column=2)
        Label(show_ent,text="Branch",font=f,fg='red').grid(row=0,column=3)
        Label(show_ent,text="Chemistry",font=f,fg='red').grid(row=0,column=4)
        Label(show_ent,text="Math",font=f,fg='red').grid(row=0,column=5)
        Label(show_ent,text="Computer",font=f,fg='red').grid(row=0,column=6)
        Label(show_ent,text="Cgpa",font=f,fg='red').grid(row=0,column=7)
        Label(show_ent,text="Grade",font=f,fg='red').grid(row=0,column=8)
        
        r=1
        r1=0
        for record in records:
            
            if(records[l-1][0]==record[0]):
                l1=list(record)
                for c in range(0,9):
                    Label(show_ent,text=l1[c],fg='blue',font=f1).grid(row=r1+1,column=c)
                r+=1
            r=r+1
            r1=r1+1
              


    #commit_changes
        db.commit()
    #close connection
        db.close()
        

    show=Button(cgnc,text='Show Entries',bg='yellow',fg='black',borderwidth=3,command=show_en,padx=84,pady=5,font=f)
    show.grid(row=5,column=0,columnspan=2,padx=40)
    fo=font.Font(family='36 DAYS',size=10)

    def call(url):
        webbrowser.open_new(url)
    Label(cgnc,text="\nVisit our club website:",fg='blue',font=fo).grid(row=6,column=0,columnspan=2)
    l=Label(cgnc,text="https://spectrumcet.com/",fg='blue',font=fo)
    l.bind("<Button-1>",lambda x:call('https://spectrumcet.com/'))
    l.grid(row=7,column=0,columnspan=2)
    mainloop()
if __name__=='__main__':
    main()
