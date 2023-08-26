from tkinter import*
from tkinter import messagebox
a=Tk()
a.title("login page")
a.geometry("200x200")

l1=Label(a,text="Login",fon=("Arial Bold",10))
l1.grid(column=2,row=0,pady=10)

l1=Label(a,text="User Name:")
l1.grid(column=1,row=1,pady=4)
t1=Entry(a,width=20)
t1.grid(column=2,row=1)

l2=Label(a,text="Password:")
l2.grid(column=1,row=2)
t2=Entry(a,width=20,show="*")
t2.grid(column=2,row=2)

def link():
    messagebox.showinfo("login","Login Successful")

btn=Button(a,text="login",command=link)
btn.grid(column=2,row=5,pady=10)

a.mainloop()
