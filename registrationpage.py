from tkinter import*
a=Tk()
a.title("Registration page")
a.geometry("400x500")
lb1=Label(a,text="REGISTRATION",font=("Arial Bold",10))
lb1.grid(column=2,row=0,pady=10)
l1=Label(a,text="Name:")
l1.grid(column=1,row=1)
t1=Entry(a,width=20)
t1.grid(column=2,row=1,pady=4)

l2=Label(a,text="Roll Number:")
l2.grid(column=1,row=2)
t2=Entry(a,width=20)
t2.grid(column=2,row=2,pady=4)

l3=Label(a,text="Mobile Number:")
l3.grid(column=1,row=3)
t3=Entry(a,width=20)
t3.grid(column=2,row=3,pady=4)

l4=Label(a,text="Mobile Number:")
l4.grid(column=1,row=3)
t4=Entry(a,width=20)
t4.grid(column=2,row=3,pady=4)

l5=Label(a,text="Email:")
l5.grid(column=1,row=4)
t5=Entry(a,width=20)
t5.grid(column=2,row=4,pady=4)

def gender():
    r=str(radio.get())
    #l.configure(text=r)
    
l5=Label(a,text="Gender:")
l5.grid(column=1,row=5)
radio=IntVar()
r1=Radiobutton(a,text="Female",variable=radio,value=1,command=gender)
r1.grid(column=2,row=5)
r2=Radiobutton(a,text="Male",variable=radio,value=2,command=gender)
r2.grid(column=2,row=6,pady=4)


def age(val):
    l=Label(a,text=val)
    l.grid(column=1,row=8)
l6=Label(a,text="Select Age:")
l6.grid(column=1,row=7)
t6=Scale(a,from_=0 ,to=100,orient=HORIZONTAL,command=age)
t6.grid(column=2,row=7,pady=5)
t6.set(0)

l7=Label(a,text="Interested language:")
l7.grid(column=1,row=10,pady=4)

l8=Checkbutton(a,text="C")
l9=Checkbutton(a,text="C++")
l10=Checkbutton(a,text="python")
l11=Checkbutton(a,text="java")
l12=Checkbutton(a,text="HTML")
l13=Checkbutton(a,text="CSS")
l14=Checkbutton(a,text="javascript")
l15=Checkbutton(a,text="PHP")


l8.grid(column=2,row=9,pady=4)
l9.grid(column=2,row=10)
l10.grid(column=2,row=11)
l11.grid(column=2,row=12)
l12.grid(column=2,row=13)
l13.grid(column=2,row=14)
l14.grid(column=2,row=15)
l15.grid(column=2,row=16)

def submit():
    import loginpage

btn=Button(a,text="Submit",command=submit)
btn.grid(column=1,row=17,pady=20)

a.mainloop()


