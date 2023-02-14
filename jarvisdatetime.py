
# from tkinter import *
# def aboutview():
#     ro=Tk()
#     ro.config(bg="#1F2732")
#     #ro.config(bg="black")
#     ro.title("About")    
#     ro.iconbitmap("notebook.ico")
#     ro.geometry("380x300+300+300")
#     background_image = PhotoImage(file='2723.png')
#     Label(ro,image=background_image,fg="#FFBD09",bg="#1F2732",bd=0).pack(anchor=NW)
#     # ro.attributes("-fullscreen",True)
#     # ro.attributes('-transparentcolor','black')
#     # ro.state('zoomed')
#     # # Label(ro,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").pack()
#     Label(ro,text="About me :-",font="Bahnschrift 19",bg="#1F2732",fg="#FFBD09").pack(anchor=NW)   
#     Label(ro,
#     text=
#     """my self bhuvnesh verma .
#     The application is created with the help
#     of python and tkinter 
#     hopefully you like it  .""",font="calibri 15",bg="#1F2732",fg="white").pack(anchor=NW)
#     close=Button(ro, text='  close  ', command=quit,bg='#10121f',font=("calibri", 13),bd=0,fg='white',highlightthickness=0,pady=3)
#     close.pack()
#     def changex(event):
#         close['bg']='red'
#     def returnx(event):
#         close['bg']='#10121f'
#     close.bind('<Enter>',changex)
#     close.bind('<Leave>',returnx)
#     ro.mainloop()
# aboutview()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from tkinter import*
# from PIL import Image,ImageTk,ImageSequence
# import time
# root=Tk()
# root.geometry("600x400")
# #root.config(bg="white")
# root.wm_attributes('-transparentcolor',root['bg'])
# def play_gif():
#     global img
#     img=Image.open("sunset.gif")
#     lbl=Label(root)
#     lbl.place(x=0,y=0)
#     for img in ImageSequence.Iterator(img):
#         img=img.resize((300,300))
#         img=ImageTk.PhotoImage(img)
#         lbl.config(image=img,borderwidth=0)
#         root.update()
#         time.sleep(0.01)
#     root.after(0,play_gif)
# def exit():
#     root.destroy()
# Button(root,text="play",command=play_gif).place(x=500,y=300)
# Button(root,text="exit",command=exit).place(x=450,y=300)
# root.mainloop()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import tkinter as ui
# import time

# window = ui.Tk()
# window.wm_attributes('-transparentcolor',window['bg'])

# def update_clock():
#     hours = time.strftime("%I")
#     minutes = time.strftime("%M")
#     seconds = time.strftime("%S")
#     am_or_pm = time.strftime("%p")
#     time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
#     digital_clock_lbl.config(text=time_text)
#     digital_clock_lbl.after(1000, update_clock)


# digital_clock_lbl = ui.Label(window, text="00:00:00", font="Helvetica 40 ")
# digital_clock_lbl.pack()

# update_clock()

# window.mainloop()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
# import tkinter as ui

# import time
# import math

# window = ui.Tk()
# window.geometry("400x400")


# def update_clock():
#     hours = int(time.strftime("%I"))
#     minutes = int(time.strftime("%M"))
#     seconds = int(time.strftime("%S"))

#     # updating seconds hand
#     seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
#     seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
#     canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

#     # updating minutes hand
#     minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
#     minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
#     canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

#     # updating hours hand
#     hours_x = hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
#     hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
#     canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

#     window.after(1000, update_clock)


# canvas = ui.Canvas(window, width=400, height=400, bg="black")
# canvas.pack(expand=True, fill='both')

# # create background
# bg = ui.PhotoImage(file='dial_400.png')
# canvas.create_image(200, 200, image=bg)


# # create clock hands
# # seconds hand
# center_x = 200
# center_y = 200

# seconds_hand_len = 95
# minutes_hand_len = 80
# hours_hand_len = 60

# seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')
# # minutes hand
# minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='white')
# # hours hand
# hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='white')

# update_clock()

# window.mainloop()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# import tkinter as tk

# # Top level window
# frame = tk.Tk()
# frame.title("TextBox Input")
# frame.geometry('400x200')
# # Function for getting Input
# # from textbox and printing it
# # at label widget

# def printInput():
# 	inp = inputtxt.get(1.0, "end-1c")
# 	print(inp)
# # 	lbl.config(text = "Provided Input: "+inp)

# # TextBox Creation
# inputtxt = tk.Text(frame,
# 				height = 2,
# 				width = 10)

# inputtxt.grid(row=1,column=1,sticky=tk.NW)

# # Button Creation
# printButton = tk.Button(frame,text = "Print", command = printInput)
# printButton.grid(row=1,column=2,sticky=tk.NE)

# # Label Creation
# lbl = tk.Label(frame, text = "")
# lbl.grid(row=2,column=1,sticky=tk.NW)
# frame.mainloop()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from tkinter import *
# from tkinter import messagebox
# import datetime

# def save ():
#     strDate = datetime.datetime.now().strftime("%d:%B:%y")
#     strTime = datetime.datetime.now().strftime("%H:%M:%S")
#     topic=savename.get()
#     f=open(f"{topic}.txt",'w')
#     f.write(f" Note of the  Date:- {strDate} \n while time was {strTime}")
#     f.close()
#     messagebox.showinfo("Message","your file as saved") 
#     r.destroy()
# r=Tk()
# r.geometry("200x70+300+300")
# Label(r, text="Save with the name .....").grid(sticky=W, pady=4, padx=5)
# savename=StringVar()
# Entry(r,textvariable=savename).grid(row=1, column=0, columnspan=2, rowspan=4,padx=5,ipady=3, sticky=E+W+S+N)
# Button(r, text="Save",command=save).grid(row=1, column=3)
# r.mainloop()
# import datetime
# from tkinter import *
# from tkinter import messagebox
# def save():
#     r=Tk()
#     r.geometry("210x70+300+300")
#     Label(r, text="Save with the name .....").grid(sticky=W, pady=4, padx=5)
#     savename=StringVar()
#     Entry(r,textvariable=savename).grid(row=1, column=0, columnspan=2, rowspan=4,padx=5,ipady=3, sticky=E+W+S+N)
    
#     def saveas ():
#         strDate = datetime.datetime.now().strftime("%d:%B:%y")
#         strTime = datetime.datetime.now().strftime("%H:%M:%S")
#         topic=savename.get() 
#         foo=open(f"{topic}.txt","w")
#         foo.write(f" Note of the  Date:- {strDate} \n while time was {strTime}")
#         foo.write("\n")
#         foo.write("okhtfguyhytgujrt")
#         foo.close()
#         messagebox.showinfo("Message","your file as saved") 
#         r.destroy()
#     Button(r, text="Save",command=saveas).grid(row=1, column=3)
#     r.mainloop()
# save()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from tkinter import *
# from tkinter import font
# root=Tk()
# fonts=font.families()
# for i in fonts:
#     print(i)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[importing module's]

# from tkinter import *
# from time import sleep   
# from tracemalloc import stop
# from cgitb import text
# from tkinter import messagebox
# import datetime

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[loading frame ]

# def nike():

#     ro=Tk()
#     ro.config(bg="black")
#     ro.title("Loading")
#     ro.attributes("-fullscreen",True)
#     ro.attributes('-transparentcolor','black')
#     ro.state('zoomed')
#     Label(ro,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
#     for i in range (16):
#         Label(ro,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
#         ro.update()
#         for i in range(3):
#             for j in range(16):
#                 Label(ro,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
#                 sleep(0.06)
#                 ro.update_idletasks()
#                 Label(ro,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
#                 stop()
#         else:
#             ro.destroy()
#             ok()
#             exit(0)
#     ro.mainloop()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[frame structure]

# def ok():

#     root = Tk()
#     root.geometry("350x300+300+300")
#     root.title("Notes")
#     root.iconbitmap("notebook.ico")

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[save function]

#     def save():
#         r=Tk()
#         r.geometry("210x70+300+300")
#         r.iconbitmap("notebook.ico")
#         r.title("Save")
#         Label(r, text="Save with the name .....",bg="#1F2732",fg="#FFBD09").grid(sticky=W, pady=4, padx=5)
#         r.config(bg="#1F2732")
#         def printIn():
#             j = jk.get(1.0, "end-1c") 
#             strDate = datetime.datetime.now().strftime("%d:%B:%y")
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             inp = area.get(1.0, "end-1c")
#             foo=open(f"{j}.txt","w")
#             foo.write(f" Note of the  Date:- {strDate} \n while time was {strTime}")
#             foo.write("\n")
#             foo.write(inp)
#             foo.close()
#             messagebox.showinfo("Message","your file as saved") 
#             r.destroy()
#             print(j)
#         jk = Text(r,height=1,width=5,relief=RIDGE,bd=0)
#         jk.grid(row=1, column=0,padx=5,ipady=3, sticky=E+W+S+N)
#         hi=Button(r, text="Save",command=printIn,bg="#1F2732",fg="#FFBD09",borderwidth=2)
#         hi.grid(row=1, column=3)
#         def changex(event):
#             hi['bg']='#3e4042'
#         def returnx(event):
#             hi['bg']="#1F2732"
#         hi.bind('<Enter>',changex)
#         hi.bind('<Leave>',returnx)
#         r.mainloop() 

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[viewing function]

#     def printInput():
#         inp = area.get(1.0, "end-1c")
#         print(inp)
#         rt=Tk()
#         rt.title("View")
#         rt.iconbitmap("notebook.ico")
#         rt.config(bg="#1F2732")
#         rt.geometry("350x300+300+300")
#         Label(rt,text="The text you have wrote",bg="#1F2732",fg="#FFBD09", pady=15).grid(sticky=NW)
#         Label(rt,text=inp,bg="#1F2732",fg="white").grid(sticky=E+W+S+N)
#         rt.mainloop()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[joing row and column]

#     root.config(bg="#1F2732")
#     root.columnconfigure(1, weight=1)
#     root.columnconfigure(3, pad=7)
#     root.rowconfigure(3, weight=1)
#     root.rowconfigure(5, pad=7)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[labeling the text]

#     lbl = Label(root,text="Don't forget to save before closing",bg="#1F2732",fg="#FFBD09")
#     lbl.grid(sticky=W, pady=4, padx=5)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[entery taking]

#     area = Text(root,bg='#3e4042',fg="white",relief=RIDGE,bd=0)
#     area.grid(row=1, column=0, columnspan=2, rowspan=4,padx=5, sticky=E+W+S+N)
#     inp = area.get(1.0, "end-1c") 

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[view button]

#     abtn = Button(root,text="view",command=printInput,bg="#1F2732",fg="#FFBD09",borderwidth=0)
#     abtn.grid(row=1, column=3,ipadx=2)
#     def changex(event):
#         abtn['bg']='#3e4042'
#     def returnx(event):
#         abtn['bg']="#1F2732"
#     abtn.bind('<Enter>',changex)
#     abtn.bind('<Leave>',returnx)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[colse button]

#     close=Button(root, text='  close  ', command=quit,bg="#1F2732",fg="#FFBD09",bd=0,highlightthickness=0,borderwidth=0)
#     close.grid(row=2, column=3, pady=4)
#     def changex(event):
#         close['bg']='red'
#     def returnx(event):
#         close['bg']="#1F2732"
#     close.bind('<Enter>',changex)
#     close.bind('<Leave>',returnx)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[about button]

#     hbtn = Button(root,text="about",bg="#1F2732",fg="#FFBD09",borderwidth=0,command=aboutview)
#     hbtn.grid(row=5, column=0, padx=5,sticky=W)
#     def changex(event):
#         hbtn['bg']='#3e4042'
#     def returnx(event):
#         hbtn['bg']="#1F2732"
#     hbtn.bind('<Enter>',changex)
#     hbtn.bind('<Leave>',returnx)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[save button]

#     obtn = Button(root, text="Save",command=save,bg="#1F2732",fg="#FFBD09",borderwidth=0)
#     obtn.grid(row=5, column=3)
#     def changex(event):
#         obtn['bg']='#3e4042'
#     def returnx(event):
#         obtn['bg']="#1F2732"
#     obtn.bind('<Enter>',changex)
#     obtn.bind('<Leave>',returnx)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[frame close]

#     root.mainloop()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[about creator]
# def aboutview():
#     aro=Tk()
#     aro.config(bg="#1F2732")
#     #ro.config(bg="black")
#     aro.title("About")    
#     aro.iconbitmap("notebook.ico")
#     aro.geometry("350x300+300+300")
#     Label(aro,text="About me :-",font="Bahnschrift 19",bg="#1F2732",fg="#FFBD09").pack(anchor=NW)   
#     Label(aro,
#     text=
#     """my self bhuvnesh verma .
#     The application is created with the
#       help of python and tkinter 
#         hopefully you like it  .""",font="calibri 15",bg="#1F2732",fg="white").pack(anchor=NW)
#     closei=Button(aro, text='  close  ', command=aro.destroy,bg='#10121f',font=("calibri", 13),bd=0,fg='white',highlightthickness=0,pady=3)
#     closei.pack(padx=50,pady=50)
#     def changex(event):
#         closei['bg']='red'
#     def returnx(event):
#         closei['bg']='#10121f'
#     closei.bind('<Enter>',changex)
#     closei.bind('<Leave>',returnx)
#     aro.mainloop()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Runing the application]
# if __name__=="__main__":
#     nike()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[The End.]
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# from tkinter import *
# from time import sleep   
# from tracemalloc import stop
# from cgitb import text
# from tkinter import messagebox
# import datetime

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[loading frame ]
# a="#1F2732"
# b="#FFBD09"
# c='#3e4042'
# def nike():

#     ro=Tk()
#     ro.config(bg="black")
#     ro.title("Loading")
#     # ro.attributes("-fullscreen",True)
#     # ro.attributes('-transparentcolor','black')
#     ro.config(bg=c)
#     # ro.state('zoomed')
#     # Label(ro,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
#     ro.geometry("350x300+300+300")
#     # for i in range (7):
#     #     Label(ro,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
#     #     ro.update()
#     #     for i in range(3):
#     #         for j in range(7):
#     #             Label(ro,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
#     #             sleep(0.06)
#     #             ro.update_idletasks()
#     #             Label(ro,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
#     #             stop()
#     #     else:
#     #         ro.destroy()
#     #         # ok()
#     #         exit()
#     ro.mainloop()
# nike()


































# >>>>>>>>>>>>>>>>>>>>>>>>:-
# import pygame
# from tkinter import *
# from tkinter.filedialog import askdirectory
# import os

# music_player = Tk()
# music_player.title("My Music Player")
# music_player.geometry("450x350")
# directory = askdirectory()
# os.chdir(directory)
# song_list = os.listdir()

# play_list = Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=SINGLE)
# for item in song_list:
#     pos = 0
#     play_list.insert(pos, item)
#     pos += 1
# pygame.init()
# pygame.mixer.init()

# def play():
#     pygame.mixer.music.load(play_list.get(ACTIVE))
#     var.set(play_list.get(ACTIVE))
#     pygame.mixer.music.play()
# def stop():
#     pygame.mixer.music.stop()
# def pause():
#     pygame.mixer.music.pause()
# def unpause():
#     pygame.mixer.music.unpause()
# Button1 = Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play)
# Button2 = Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop)
# Button3 = Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause)
# Button4 = Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause)

# var = StringVar() 
# song_title = Label(music_player, font="Helvetica 12 bold", textvariable=var)

# song_title.pack()
# Button1.pack()
# Button2.pack()
# Button3.pack()
# Button4.pack()
# play_list.pack(fill="both", expand="yes")
# music_player.mainloop()

















# import os
# from tkinter.filedialog import askdirectory
# directory = askdirectory()
# os.chdir(directory)
# song_list = os.listdir()
# for item in song_list:
#     print(str(item))
   


########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################



from tkinter import *
from ctypes import windll
tk_title = "Jarvis" # Put here your window title
root=Tk() # root (your app doesn't go in root, it goes in window)
root.title(tk_title) 
root.overrideredirect(True) # turns off title bar, geometry
root.geometry('400x600+75+75') # set new geometry the + 75 + 75 is where it starts on the screen
# root.iconbitmap("implant.ico") # to show your own icon 
root.minimized = False # only to know if root is minimized
root.maximized = False # only to know if root is maximized
LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
DGRAY = '#25292e' # window background color               (Hex color)
RGRAY = '#10121f' # title bar color                       (Hex color)
root.config(bg="#25292e")
title_bar = Frame(root, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)
def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
                               # even when using root.overrideredirect(True)

    # Some WindowsOS styles, required for task bar integration
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)  
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())
def minimize_me():
    root.attributes("-alpha",0) # so you can't see the window when is minimized
    root.minimized = True 
def deminimize(event):
    root.focus() 
    root.attributes("-alpha",1) # so you can see the window when is not minimized
    if root.minimized == True:
        root.minimized = False                              
def maximize_me():

    if root.maximized == False: # if the window was not maximized
        root.normal_size = root.geometry()
        expand_button.config(text=" 🗗 ")
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.maximized = not root.maximized 
        # now it's maximized       
    else: # if the window was maximized
        expand_button.config(text=" 🗖 ")
        root.geometry(root.normal_size)
        root.maximized = not root.maximized
        # now it is not maximized
# put a close button on the title bar
close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
title_bar_title = Label(title_bar, text=tk_title, bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)
# a frame for the main area of the window, this is where the actual app will go
window = Frame(root, bg=DGRAY,highlightthickness=0)
# pack the widgets
title_bar.pack(fill=X)
close_button.pack(side=RIGHT,ipadx=7,ipady=1)
expand_button.pack(side=RIGHT,ipadx=7,ipady=1)
minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
title_bar_title.pack(side=LEFT, padx=10)
window.pack(expand=1, fill=BOTH) # replace this with your main Canvas/Frame/etc.
#xwin=None
#ywin=None
# bind title bar motion to the move window function
def changex_on_hovering(event):
    global close_button
    close_button['bg']='red'
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=RGRAY
def change_size_on_hovering(event):
    global expand_button
    expand_button['bg']=LGRAY
def return_size_on_hovering(event):
    global expand_button
    expand_button['bg']=RGRAY
def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=LGRAY
def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=RGRAY
def get_pos(event): # this is executed when the title bar is clicked to move the window
    if root.maximized == False:  
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root
        ywin = ywin - starty
        xwin = xwin - startx
        def move_window(event): # runs when window is dragged
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')
        def release_window(event): # runs when window is released
            root.config(cursor="arrow")           
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        expand_button.config(text=" 🗖 ")
        root.maximized = not root.maximized
title_bar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
title_bar_title.bind('<Button-1>', get_pos) # so you can drag the window from the title 
# button effects in the title bar when hovering over buttons
close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)
expand_button.bind('<Enter>', change_size_on_hovering)
expand_button.bind('<Leave>', return_size_on_hovering)
minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)
# resize the window width =======================================================================
resizex_widget = Frame(window,bg=DGRAY,cursor='sb_h_double_arrow')
resizex_widget.pack(side=RIGHT,ipadx=2,fill=Y)
def resizex(event):
    xwin = root.winfo_x()
    difference = (event.x_root - xwin) - root.winfo_width()
    if root.winfo_width() > 150 : # 150 is the minimum width for the window
        try:
            root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
        except:
            pass
    else:
        if difference > 0: # so the window can't be too small (150x150)
            try:
                root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
            except:
                pass
    resizex_widget.config(bg=DGRAY)
resizex_widget.bind("<B1-Motion>",resizex)
# resize the window height =======================================================================
resizey_widget = Frame(window,bg=DGRAY,cursor='sb_v_double_arrow')
resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)
def resizey(event):
    ywin = root.winfo_y()
    difference = (event.y_root - ywin) - root.winfo_height()
    if root.winfo_height() > 150: # 150 is the minimum height for the window
        try:
            root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
        except:
            pass
    else:
        if difference > 0: # so the window can't be too small (150x150)
            try:
                root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
            except:
                pass
    resizex_widget.config(bg=DGRAY)
resizey_widget.bind("<B1-Motion>",resizey)
# some settings
root.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
root.after(10, lambda: set_appwindow(root)) # to see the icon on the task bar

#YOUR CODE GOES HERE==================================================================================
#Label(window,text="Hello :D",bg=DGRAY,fg="#fff").pack(expand=1) # example 



import time
def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes 
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)

digital_clock_lbl =Label(window, text="00:00",fg="white",bg=DGRAY, font="comics 20 ")
digital_clock_lbl.pack(padx=5,pady=5,side=LEFT,anchor=N)
update_clock()
close=Button(window, text='  close  ', command=quit,bg=RGRAY,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
close.pack(side=BOTTOM,anchor=W)
def changex(event):
    global close
    close['bg']='red'
def returnx(event):
    global close
    close['bg']=RGRAY
close.bind('<Enter>',changex)
close.bind('<Leave>',returnx)

# ===================================================================================================
root.mainloop()


