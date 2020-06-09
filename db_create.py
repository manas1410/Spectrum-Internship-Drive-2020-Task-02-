from tkinter import*
import sqlite3

mark_list=Tk()
mark_list.geometry("300x200")
mark_list.title("Mark List")
db=sqlite3.connect("mark_list.db")
#cursor
c=db.cursor()
#insert into tabels
c.execute("""CREATE TABLE mark_list(
user_name text,
name text,
registration_no text,
branch text,
chemistry integer,
math integer,
computer integer,
cgpa integer,
grade text)""")


    
#commit_changes
db.commit()
#close connection
db.close()

mark_list.mainloop()
