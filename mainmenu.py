from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#FUNCTIONS
mainmenu = Tk()
mainmenu.geometry("730x490")
mainmenu.title("Main Menu Window")
mainmenu.configure(bg = "#ffffff")
canvas = Canvas(mainmenu,bg = "#ffffff",height = 490,width = 730,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundmm.png")
background = canvas.create_image(371.0, 241.5,image=background_img)

#BUTTONS
imgmt = PhotoImage(file = f"img0mm.png")
mtbutton = Button(image = imgmt,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
mtbutton.place(x = 300, y = 152,width = 130,height = 74)

imft = PhotoImage(file = f"img1mm.png")
ftbutton = Button(image = imft,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
ftbutton.place(x = 300, y = 235,width = 130,height = 74)

imgc = PhotoImage(file = f"img2mm.png")
chocobutton = Button(image = imgc,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
chocobutton.place(x = 300, y = 318,width = 130,height = 74)

mainmenu.resizable(False, False)
mainmenu.mainloop()
