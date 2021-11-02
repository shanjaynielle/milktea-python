from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#WINDOW PROPERTIES
fruitteawindow = Tk()
fruitteawindow.geometry("730x490")
fruitteawindow.title("Fruit Tea Frame")
fruitteawindow.configure(bg = "#ffffff")
canvas = Canvas(fruitteawindow,bg = "#ffffff",height = 490,width = 730,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundft.png")
background = canvas.create_image(367.5, 242.5,image=background_img)

#BUTTONS
imgorderft = PhotoImage(file = f"img0ft.png")
orderbuttonft = Button(image = imgorderft,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
orderbuttonft.place(x = 303, y = 433,width = 123,height = 50)

#SPINBOX
grape = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
grape.place(x = 183, y = 220, width = 90)

lychee = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
lychee.place(x = 325, y = 235, width = 90)

yogurt = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
yogurt.place(x = 471, y = 220, width = 90)

mango = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
mango.place(x = 250, y = 405, width = 90)

passionfruit = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
relief="flat",state="readonly")
passionfruit.place(x = 405, y = 405, width = 90 )

#LOOP
fruitteawindow.resizable(False, False)
fruitteawindow.mainloop()
