from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#WINDOW PROPERTIES
milkteawindow = Tk()
milkteawindow.geometry("730x490")
milkteawindow.title("Milktea Frame")
milkteawindow.configure(bg = "#ffffff")
canvas = Canvas(milkteawindow,bg = "#ffffff",height = 490,width = 730,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundmt.png")
background = canvas.create_image(367.5, 242.5,image=background_img)

#BUTTONS
imgordermt = PhotoImage(file = f"img0mt.png")
orderbuttonmt = Button(image = imgordermt,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
orderbuttonmt.place(x = 303, y = 433,width = 123,height = 50)

#SPINBOX
coffee = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
coffee.place(x = 183, y = 220, width = 90)

strawberry = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
strawberry.place(x = 325, y = 235, width = 90)

thai = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
thai.place(x = 471, y = 220, width = 90)

banana = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
banana.place(x = 175, y = 390, width = 90)

matcha = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
matcha.place(x = 325, y = 390, width = 90 )

pearl = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
pearl.place(x = 465, y = 390, width = 90 )

#LOOP
milkteawindow.resizable(False, False)
milkteawindow.mainloop()
