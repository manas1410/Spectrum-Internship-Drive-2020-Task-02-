from tkinter import*
import sqlite3

user_pas=Tk()
user_pas.geometry("300x200")
user_pas.title("User_pas")
db=sqlite3.connect("user_pas.db")
#cursor
c=db.cursor()
#insert into tabels
c.execute("""CREATE TABLE user_pas(
username text,
password text
)""")


    
#commit_changes
db.commit()
#close connection
db.close()

user_pas.mainloop()
