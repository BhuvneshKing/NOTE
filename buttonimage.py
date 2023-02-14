from tkinter import*
root=Tk()
root.title("button")
root.geometry("800x800")
def hi():
    my_label.config(text="you clicked the button")

# photo=PhotoImage(file="AC.png")# put image in place of X
# img_label=Label(image=photo)
#img_label.pack(pady=20)
# poke=Button(root,image=photo,command=hi,borderwidth=0)
poke=Button(root,text="select",command=hi,borderwidth=0)
poke.pack(pady=20)
my_label=Label(root,text='')
my_label.pack(pady=20)
root.mainloop()