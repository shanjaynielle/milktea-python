from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#WINDOW PROPERTIES
loginwindow = Tk()
loginwindow.geometry("730x490")
loginwindow.title("Login Window")
loginwindow.configure(bg = "#ffffff")
canvas = Canvas(loginwindow,bg = "#ffffff",height = 490,width = 730,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundlogin.png")
background = canvas.create_image(297.0, 251.5,image=background_img)

#TEXTBOX
username = Entry(
    bd = 0,bg = "#ffffff",highlightthickness = 0,
    font="Helvetica", fg="#A66D6D")
username.place(x = 470, y = 170,width = 215,height = 20)

password = Entry(
    bd = 0,bg = "#ffffff",highlightthickness = 0, show="*",
    fg="#A66D6D")
password.place(x = 470, y = 245,width = 215,height = 20)

#BUTTONS
imglogin = PhotoImage(file = f"img0login.png")
loginbutton = Button(image = imglogin,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
loginbutton.place(x = 501, y = 297,width = 100,height = 74)

imgreg = PhotoImage(file = f"img1login.png")
registerbutton = Button(image = imgreg,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
registerbutton.place(x = 486, y = 431,width = 132,height = 24)

imgexit = PhotoImage(file = f"img2login.png")
exitbutton = Button(image = imgexit,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
exitbutton.place(x = 683, y = 10,width = 31,height = 40)

loginwindow.resizable(False, False)
loginwindow.mainloop()
