from tkinter import*
root=Tk()
root.geometry("300x300")
import datetime
x = datetime.datetime.now() 
a=x.strftime("%x %A")
b=x.strftime("%I:%M %p")
c=x.strftime("%A")
d=x.strftime("%H:%M")
e=x.strftime("%C")
f=(e,"century")
def getvals():
    print(f"The value of username is {uservalue.get()}")
    x=uservalue.get()
    y=x.capitalize()
    if y=="Date":
            me=Tk()
            me.geometry("360x50")
            me.minsize(360,50)
            me.maxsize(360,50)
            me.title("Date")
            melabel = Label(me,text=a,bg='White',font=("Times",30,'bold'))
            melabel.pack(side=TOP)
            me.mainloop()
    elif y=="Time":
        me=Tk()
        me.geometry("170x50")
        me.minsize(170,50)
        me.maxsize(170,50)
        me.title("Time")
        melabel = Label(me,text=b,bg='White',font=("Times",30,'bold'))
        melabel.pack(side=TOP)
        me.mainloop()
    elif y=="Day":
        me=Tk()
        me.geometry("200x50")
        me.minsize(200,50)
        me.maxsize(200,50)
        me.title("Day")
        melabel = Label(me,text=c,bg='White',font=("Times",30,'bold'))
        melabel.pack(side=TOP)
        me.mainloop()
    elif y=="Century":
        me=Tk()
        me.geometry("200x50")
        me.minsize(200,50)
        me.maxsize(200,50)
        me.title("Century")
        melabel = Label(me,text=f,bg='White',font=("Times",30,'bold'))
        melabel.pack(side=TOP)
        me.mainloop()
    else:
        me=Tk()
        me.geometry("50x80")
        me.title("sorry")
        melabel=Label(me,text="sorry",font=("Times",30,'bold'))
        melabel.pack()
   
# time
user=Label(root,text="Entry what you want")
user.grid()
uservalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
userentry.grid(row=0,column=1)
Button(text="Submit", command=getvals).grid()

root.mainloop()