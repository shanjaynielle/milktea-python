from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#FRAME PROPERTIES
signupwindow = Tk()
signupwindow.geometry("730x490")
signupwindow.title("Signup Window")
signupwindow.configure(bg = "#ffffff")
canvas = Canvas(signupwindow,bg = "#ffffff",height = 490,width = 730,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundsu.png")
background = canvas.create_image(465.5, 237.5,image=background_img)

#TEXTBOX
email = Entry(
    bd = 0,bg = "#ffffff",highlightthickness = 0,
    font="Helvetica", fg="#A66D6D")
email.place(x = 90, y = 180, width = 215, height=20)

username = Entry(
    bd = 0,bg = "#ffffff",highlightthickness = 0,
    font="Helvetica", fg="#A66D6D")
username.place(x = 90, y = 250,width = 215,height = 20)

password = Entry(
    bd = 0,bg = "#ffffff",highlightthickness = 0, show="*",
    fg="#A66D6D")
password.place(x = 90, y = 330,width = 215,height = 20)

#BUTTONS
imgcreate = PhotoImage(file = f"img0su.png")
createbutton = Button(image = imgcreate,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
createbutton.place(x = 75, y = 379,width = 195,height = 74)

imgexit = PhotoImage(file = f"img1su.png")
exitbutton = Button(image = imgexit,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
exitbutton.place(x = 6, y = 3,width = 31,height = 40)

signupwindow.resizable(False, False)
signupwindow.mainloop()
