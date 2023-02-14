


# from tkinter import *
# def aboutview():
#     ro=Tk()
#     ro.config(bg="#1F2732")
#     #ro.config(bg="black")
#     ro.title("About")    
#     ro.iconbitmap("notebook.ico")
#     ro.geometry("380x300+300+300")
#     background_image = PhotoImage(file='imgk.png')
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
# root.config(bg="white")
# # root.wm_attributes('-transparentcolor',root['bg'])
# def play_gif():
#     global img
#     img=Image.open("first.gif")
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
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


















import tkinter as ui
import time

window = ui.Tk()
window.wm_attributes('-transparentcolor',window['bg'])

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)


digital_clock_lbl = ui.Label(window, text="00:00:00", font="merlin 40 ", foreground="WHITE")
digital_clock_lbl.pack()

update_clock()

window.mainloop()
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
