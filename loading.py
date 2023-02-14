# from tkinter import *
# from time import sleep
# from tracemalloc import stop
# import jk
# class loadingsplash:
#     def play_animation(self):
#         for i in range(5):
#             for j in range(16):
#                 Label(self.root,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
#                 sleep(0.06)
#                 self.root.update_idletasks()
#                 Label(self.root,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
#                 stop()
#         else:
#             self.root.destroy()
#             exit(0)

#     def __init__(self):
#         self.root=Tk()
#         self.root.config(bg="black")
#         self.root.title("custom  Loader")
#         self.root.attributes("-fullscreen",True)
#         self.root.attributes('-transparentcolor','black')
#         self.root.state('zoomed')
#         Label(self.root,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
#         for i in range (16):
#             Label(self.root,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
#             self.root.update()
#             self.play_animation()
#         self.root.mainloop()


# if __name__=="__main__":
#     loadingsplash()   

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
from time import sleep
from tracemalloc import stop
class loadingsplash:
    def play_animation(self):
        for i in range(5):
            for j in range(16):
                Label(self.root,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
                sleep(0.06)
                self.root.update_idletasks()
                Label(self.root,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
                stop()
        else:
            self.root.destroy()
            exit(0)

    def __init__(self):
        self.root=Tk()
        self.root.config(bg="black")
        self.root.title("custom  Loader")
        self.root.attributes("-fullscreen",True)
        self.root.attributes('-transparentcolor','black')
        self.root.state('zoomed')
        Label(self.root,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
        for i in range (16):
            Label(self.root,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
            self.root.update()
            self.play_animation()
        self.root.mainloop()


if __name__=="__main__":
    loadingsplash() 
