from tkinter import *
import tkinter.font as font
import sqlite3
sub=' '
ch=0
ma=0
co=0
def main():
    mark=Tk()
    mark.title("Mark")
    mark.iconbitmap("logo/spectrumlogo.ico")
    mark.geometry("150x100")
    marks=Entry(mark,width=20)
    f=font.Font(family='Panthon Rust',size=10,weight='bold')
    f1=font.Font(family='Singel',size=16,weight='bold')
    Label(mark,text="Enter your mark",font=f).pack()
    Label(mark,text=sub,fg='red',font=f1).pack()
    marks.pack()
    def submit():
        ch,ma,co=0,0,0
        if sub=='CHEMISTRY':
            ch=int(marks.get())
            db=sqlite3.connect("mark_list.db")
        #cursor
            c=db.cursor()
        #insert into tabels
            c.execute("""UPDATE  mark_list SET chemistry=? WHERE chemistry=?""",(ch,0))
        #commit_changes
            db.commit()
        #close connection
            db.close()
        elif sub=='MATH':
            ma=int((marks.get()))
            db=sqlite3.connect("mark_list.db")
        #cursor
            c=db.cursor()
        #insert into tabels
            c.execute("""UPDATE  mark_list SET math=? WHERE math=?""",(ma,0))
        #commit_changes
            db.commit()
        #close connection
            db.close()
            
        elif sub=='COMPUTER':
            co=int(marks.get())
            db=sqlite3.connect("mark_list.db")
        #cursor
            c=db.cursor()
        #insert into tabels
            c.execute("""UPDATE  mark_list SET computer=? WHERE computer=?""",(co,0))
        #commit_changes
            db.commit()
        #close connection
            db.close()

            
        mark.destroy()
            
    Button(mark,text='Submit',command=submit,bg='green',padx=15).pack()

    mark.mainloop()
if __name__=='__main__':
    main()
