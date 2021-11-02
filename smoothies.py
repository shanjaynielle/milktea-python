from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#WINDOW PROPERTIES
smoothieswindow = Tk()
smoothieswindow.geometry("730x490")
smoothieswindow.title("Smoothies Frame")
smoothieswindow.configure(bg = "#ffffff")
canvas = Canvas(smoothieswindow,bg = "#ffffff",height = 490,width = 730,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundc.png")
background = canvas.create_image(367.5, 242.5,image=background_img)

#BUTTONS
imgorders = PhotoImage(file = f"img0c.png")
orderbuttons = Button(image = imgorders,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
orderbuttons.place(x = 303, y = 433,width = 123,height = 50)

#SPINBOX
grape = Spinbox(smoothieswindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
grape.place(x = 183, y = 320, width = 90)

lychee = Spinbox(smoothieswindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
lychee.place(x = 325, y = 320, width = 90)

yogurt = Spinbox(smoothieswindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
yogurt.place(x = 471, y = 320, width = 90)

#LOOP
smoothieswindow.resizable(False, False)
smoothieswindow.mainloop()
