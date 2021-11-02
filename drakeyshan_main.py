from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import os

#CLASS OF CART WINDOW
class Cart(Toplevel):
    def __init__(self, cart):
        self.cart_frame = cart
        Toplevel.__init__(self)
        #CART WINDOW-ATTRIBUTES
        cartwindow = self
        global current_user
    
        global arr_types
        global arr_qty
        global arr_price
        
        global milktea_total

        #CART WINDOW-PROPERTIES
        window_height = 490
        window_width = 730
        screen_width = cartwindow.winfo_screenwidth()
        screen_height = cartwindow.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        cartwindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        cartwindow.title("Cart Frame: "+current_user)
        canvas = Canvas(cartwindow,bg = "#ffffff",height = 490,width = 730,
            bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        item_label = Label(cartwindow, text=self.check_arr_types(),font="calibri 10",bg="white")
        item_label.place(x=255, y=130)

        quantity_label = Label(cartwindow, text=self.check_arr_qty(),font="calibri 10",bg="white")
        quantity_label.place(x=365, y=130)

        price_label = Label(cartwindow, text=self.check_arr_price(),font="calibri 10",bg="white")
        price_label.place(x=435, y=130)

        total_label = Label(cartwindow, text=str(milktea_total),font="calibri 10",bg="white")
        total_label.place(x=325, y=396)

        #CART WINDOW-BACKGROUND
        background_img = PhotoImage(file = f"backgroundcart.png")
        background = canvas.create_image(367.5, 242.5,image=background_img)

        #CART WINDOW-BUTTONS
        imgco = PhotoImage(file = f"imgcartcheckout.png") #NO FUNCTION YET -- WHEN CLICKED DIALOG BOX WITH PAYMENT INPUT
        checkoutbutton = Button(cartwindow,image = imgco,borderwidth = 0,highlightthickness = 0,
            command = cartwindow.check_out, relief = "flat")
        checkoutbutton.place(x = 369, y = 436,width = 124,height = 41)

        imgcartback = PhotoImage(file = f"imgcartback.png")     #NO FUNCTION YET -- BACK TO MAIN FRAME FOR SELECTION OF TYPE OF DRINK
        cartbackbutton = Button(cartwindow,image = imgcartback,borderwidth = 0,highlightthickness = 0,
            command = cartwindow.btn_clicked, relief = "flat")
        cartbackbutton.place(x = 235, y = 436,width = 124,height = 41)

        #CART WINDOW-LOOPINGS
        cartwindow.resizable(False, False)
        cartwindow.mainloop()

        #FUNCTIONS
    def btn_clicked(self):

        back_option = messagebox.askquestion("Changed your mind?", "If you go back to menu, your current orders will be deleted. Do you wish to proceed?")

        if back_option == "yes":
            global arr_types
            global arr_qty
            global arr_price
            global milktea_total

            arr_types = []
            arr_qty = []
            arr_price = []
            milktea_total = 0

            self.destroy()


    def check_arr_types(self):
        len_type = len(arr_types)
        str_type = ""
        for i in range(len_type):
            str_type = str_type + arr_types[i] +'\n'
        return str_type

    def check_arr_qty(self):
        len_qty = len(arr_qty)
        str_qty = "" 
        for i in range(len_qty):
            str_qty = str_qty + arr_qty[i] +'\n'
        return str_qty

    def check_arr_price(self):
        len_price = len(arr_price)
        str_price = ""
        for i in range(len_price):
            str_price = str_price + arr_price[i] + '\n'
        return str_price    

    def check_out(self):
        global milktea_total

        if milktea_total == 0:
            messagebox.showwarning("Notice","You don't have any orders.")
        else:    
            payment = askinteger("Enter Payment","The total of your order is "+str(milktea_total)+". How much will you pay?")
            change_coins = payment - milktea_total
            if payment < milktea_total:
                messagebox.showerror("Payment error", "You have entered an insufficient amount. Please try again.")
            else:    
                showinfo("Thank you, "+current_user,'You have paid {}'.format(payment)+" for your order. Your change is "+str(change_coins)+". Enjoy and have a nice day.")


#CLASSS OF SMOOTHIES WINDOW
class Smoothies(Toplevel):
    def __init__(self, smoothies):
        self.smoothies_frame = smoothies
        Toplevel.__init__(self)
        #SMOOTHIES WINDOW-ATTRIBUTES
        smoothieswindow = self
        global current_user

        #SMOOTHIES WINDOW-PROPERTIES
        window_height = 490
        window_width = 730
        screen_width = smoothieswindow.winfo_screenwidth()
        screen_height = smoothieswindow.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        smoothieswindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        smoothieswindow.title("Smoothies Frame: "+current_user)
        canvas = Canvas(smoothieswindow,bg = "#ffffff",height = 490,width = 730,
            bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        #SMOOTHIES WINDOW-BACKGROUND
        background_img = PhotoImage(file = f"backgroundc.png")
        background = canvas.create_image(367.5, 242.5,image=background_img)

        #SMOOTHIES WINDOW-BUTTONS
        imgorders = PhotoImage(file = f"img0mt.png")
        orderbuttons = Button(smoothieswindow, image = imgorders,borderwidth = 0,highlightthickness = 0,
            command = smoothieswindow.order,relief = "flat")
        orderbuttons.place(x = 378, y = 403,width = 123,height = 50)

        imgcback = PhotoImage(file = f"imgmtback.png")     #NO FUNCTION YET -- BACK TO MAIN FRAME FOR SELECTION OF TYPE OF DRINK
        cbackbutton = Button(smoothieswindow,image = imgcback,borderwidth = 0,highlightthickness = 0,
            command = smoothieswindow.btn_clicked, relief = "flat")
        cbackbutton.place(x = 229, y = 405,width = 124,height = 41)

        #SMOOTHIES WINDOW-SPINBOX
        self.chocomousse = Spinbox(smoothieswindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.chocomousse.place(x = 183, y = 320, width = 90)

        self.chocobanana = Spinbox(smoothieswindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.chocobanana.place(x = 325, y = 320, width = 90)

        self.choco = Spinbox(smoothieswindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.choco.place(x = 471, y = 320, width = 90)

        #SMOOTHIES WINDOW-LOOPINGS
        smoothieswindow.resizable(False, False)
        smoothieswindow.mainloop()

    #FUNCTIONS
    def btn_clicked(self):
        self.destroy()
        menu=MainMenu(self)

    def order(self):
        global milktea_total

        arr_chmousse = []
        arr_chbanana = []
        arr_choco = []

        global arr_types
        global arr_qty
        global arr_price

        qty_chmousse = int(self.chocomousse.get())
        qty_chbanana = int(self.chocobanana.get())
        qty_choco = int(self.choco.get())

        price_chmousse = 135
        price_chbanana = 140
        price_choco = 130

        total_chmousse = qty_chmousse * price_chmousse
        total_chbanana = qty_chbanana * price_chbanana
        total_choco = qty_choco * price_choco

        choco_total = total_chmousse + total_chbanana + total_choco

        if choco_total == 0:
            messagebox.showwarning("Notice","You don't have any orders.")
        else:
            choco_option = messagebox.askquestion("Confirmation","Are you sure with your order?")
            if choco_option == "yes":
                milktea_total+=choco_total
                #arrays for order
                if qty_chmousse !=0:
                    arr_chmousse=["Choco Mousse",qty_chmousse,total_chmousse]
                    arr_types.append(arr_chmousse[0])
                    arr_qty.append(str(arr_chmousse[1]))
                    arr_price.append(str(arr_chmousse[2]))

                if qty_chbanana !=0:
                    arr_chbanana=["Choco Banana",qty_chbanana,total_chbanana]
                    arr_types.append(arr_chbanana[0])
                    arr_qty.append(str(arr_chbanana[1]))
                    arr_price.append(str(arr_chbanana[2]))

                if qty_choco !=0:
                    arr_choco=["Chocolate",qty_choco,total_choco]
                    arr_types.append(arr_choco[0])
                    arr_qty.append(str(arr_choco[1]))
                    arr_price.append(str(arr_choco[2]))

                messagebox.showinfo("Notice", "Order/s added.")
                self.destroy()
                menu=MainMenu(self)     
                        

#CLASS OF FRUITTEA WINDOW
class FruitTea(Toplevel):
    def __init__(self, fruittea):
        self.fruittea_frame = fruittea
        Toplevel.__init__(self)
        #FRUITTEA WINDOW-ATTRIBUTES
        fruitteawindow = self
        global current_user

        #FRUITTEA WINDOW-PROPERTIES
        window_height = 490
        window_width = 730
        screen_width = fruitteawindow.winfo_screenwidth()
        screen_height = fruitteawindow.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        fruitteawindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        fruitteawindow.title("Fruit Tea Frame: "+current_user)
        fruitteawindow.configure(bg = "#ffffff")
        canvas = Canvas(fruitteawindow,bg = "#ffffff",height = 490,width = 730,
            bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        #FRUITTEA WINDOW-BACKGROUND
        background_img = PhotoImage(file = f"backgroundft.png")
        background = canvas.create_image(367.5, 242.5,image=background_img)

        #FRUITTEA WINDOW-BUTTONS
        imgorderft = PhotoImage(file = f"img0mt.png")
        orderbuttonft = Button(fruitteawindow, image = imgorderft,borderwidth = 0,highlightthickness = 0,
            command = fruitteawindow.order,relief = "flat")
        orderbuttonft.place(x = 378, y = 430,width = 123,height = 50)

        imgftback = PhotoImage(file = f"imgmtback.png")     #NO FUNCTION YET -- BACK TO MAIN FRAME FOR SELECTION OF TYPE OF DRINK
        ftbackbutton = Button(fruitteawindow,image = imgftback,borderwidth = 0,highlightthickness = 0,
            command = fruitteawindow.btn_clicked, relief = "flat")
        ftbackbutton.place(x = 229, y = 435,width = 124,height = 41)

        #FRUITTEA WINDOW-SPINBOX
        self.grape = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.grape.place(x = 183, y = 220, width = 90)

        self.lychee = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.lychee.place(x = 325, y = 235, width = 90)

        self.yogurt = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.yogurt.place(x = 471, y = 220, width = 90)

        self.mango = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.mango.place(x = 250, y = 405, width = 90)

        self.passionfruit = Spinbox(fruitteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.passionfruit.place(x = 405, y = 405, width = 90 )

        #FRUITTEA WINDOW-LOOPINGS
        fruitteawindow.resizable(False, False)
        fruitteawindow.mainloop()
    
    #FRUITTEA WINDOW-FUNCTIONS
    def btn_clicked(self):
        self.destroy()
        menu=MainMenu(self)

    def order(self):
        global milktea_total
        arr_grape = []
        arr_lychee = []
        arr_yogurt = []
        arr_mango = []
        arr_passion = []

        global arr_types
        global arr_qty
        global arr_price

        qty_grape = int(self.grape.get())
        qty_lychee = int(self.lychee.get())
        qty_yogurt = int(self.yogurt.get())
        qty_mango = int(self.mango.get())
        qty_passion = int(self.passionfruit.get())

        price_grape = 130
        price_lychee = 130
        price_yogurt = 150
        price_mango = 120
        price_passion = 130

        total_grape = qty_grape * price_grape
        total_lychee = qty_lychee * price_lychee
        total_yogurt = qty_yogurt * price_yogurt
        total_mango = qty_mango * price_mango
        total_passion = qty_passion * price_passion

        fruittea_total = total_grape + total_lychee + total_yogurt + total_mango + total_passion
        if fruittea_total == 0:
            messagebox.showwarning("Notice","You don't have any orders.")
        else:
            fruittea_option = messagebox.askquestion("Confirmation","Are you sure with your order?")
            if fruittea_option == "yes":
                milktea_total+=fruittea_total

                #arrays for order
                if qty_grape !=0:
                    arr_grape=["Grapes",qty_grape,total_grape]
                    arr_types.append(arr_grape[0])
                    arr_qty.append(str(arr_grape[1]))
                    arr_price.append(str(arr_grape[2]))

                if qty_lychee !=0:
                    arr_lychee=["Lychee",qty_lychee,total_lychee]
                    arr_types.append(arr_lychee[0])
                    arr_qty.append(str(arr_lychee[1]))
                    arr_price.append(str(arr_lychee[2]))  

                if qty_yogurt !=0:
                    arr_yogurt=["Yogurt",qty_yogurt,total_yogurt]
                    arr_types.append(arr_yogurt[0])
                    arr_qty.append(str(arr_yogurt[1]))
                    arr_price.append(str(arr_yogurt[2]))

                if qty_mango !=0:
                    arr_mango=["Mango",qty_mango,total_mango]
                    arr_types.append(arr_mango[0])
                    arr_qty.append(str(arr_mango[1]))
                    arr_price.append(str(arr_mango[2]))

                if qty_passion !=0:
                    arr_passion=["Passionfruit",qty_passion,price_passion]
                    arr_types.append(arr_passion[0])
                    arr_qty.append(str(arr_passion[1]))
                    arr_price.append(str(arr_passion[2]))

                messagebox.showinfo("Notice", "Order/s added.")
                self.destroy()
                menu=MainMenu(self)   

#CLASS OF MILKTEA WINDOW
class MilkTea(Toplevel):
    def __init__(self,milktea):
        self.milktea_frame = milktea
        Toplevel.__init__(self)
        #MILKTEA WINDOW-ATTRIBUTES
        milkteawindow = self
        global current_user
        
        #MILKTEA WINDOW-PROPERTIES
        window_height = 490
        window_width = 730
        screen_width = milkteawindow.winfo_screenwidth()
        screen_height = milkteawindow.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        milkteawindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        milkteawindow.title("Milktea Frame: "+current_user)
        milkteawindow.configure(bg = "#ffffff")
        canvas = Canvas(milkteawindow,bg = "#ffffff",height = 490,width = 730,
            bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        #MILKTEA WINDOW-BACKGROUND
        background_img = PhotoImage(file = f"backgroundmt.png")
        background = canvas.create_image(367.5, 242.5,image=background_img)

        #MILKTEA WINDOW-BUTTONS
        imgordermt = PhotoImage(file = f"img0mt.png")
        orderbuttonmt = Button(milkteawindow,image = imgordermt,borderwidth = 0,highlightthickness = 0,
            command = self.order,relief = "flat")
        orderbuttonmt.place(x = 371, y = 431,width = 123,height = 50)

        imgmtback = PhotoImage(file = f"imgmtback.png")     #NO FUNCTION YET -- BACK TO MAIN FRAME FOR SELECTION OF TYPE OF DRINK
        mtbackbutton = Button(milkteawindow,image = imgmtback,borderwidth = 0,highlightthickness = 0,
            command = milkteawindow.btn_clicked, relief = "flat")
        mtbackbutton.place(x = 222, y = 435,width = 124,height = 41)

        #MILKTEA WINDOW-SPINBOX
        self.coffee = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.coffee.place(x = 183, y = 220, width = 90)

        self.strawberry = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.strawberry.place(x = 325, y = 235, width = 90)

        self.thai = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.thai.place(x = 471, y = 220, width = 90)

        self.banana = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.banana.place(x = 175, y = 390, width = 90)

        self.matcha = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.matcha.place(x = 325, y = 390, width = 90 )

        self.pearl = Spinbox(milkteawindow, from_=0, to=10, bg="#F2C6C2",
        relief="flat",state="readonly")
        self.pearl.place(x = 465, y = 390, width = 90 )

        #MILKTEA WINDOW-LOOPINGS
        milkteawindow.resizable(False, False)
        milkteawindow.mainloop()

    #MILKTEA WINDOW-FUNCTIONS
    def btn_clicked(self):
        self.destroy()
        menu=MainMenu(self)  

    def order(self):

        global milktea_total

        global arr_types
        global arr_qty
        global arr_price

        qty_coffee = int(self.coffee.get())
        qty_strawberry = int(self.strawberry.get())
        qty_thai = int(self.thai.get())
        qty_banana = int(self.banana.get())
        qty_matcha = int(self.matcha.get())
        qty_pearl = int(self.pearl.get())

        price_coffee = 120
        price_strawberry = 140
        price_thai = 110
        price_banana = 120
        price_matcha = 150
        price_pearl = 100

        total_coffee = qty_coffee * price_coffee
        total_strawberry = qty_strawberry * price_strawberry
        total_thai = qty_thai * price_thai
        total_banana = qty_banana * price_banana
        total_matcha = qty_matcha * price_matcha
        total_pearl = qty_pearl * price_pearl

        meltea_total = total_coffee + total_strawberry + total_thai + total_banana + total_matcha + total_pearl

        if meltea_total==0:
            messagebox.showwarning("Notice","You don't have any orders.")
        else:
            milktea_option = messagebox.askquestion("Confirmation","Are you sure with your order?")
            if milktea_option == "yes":
                milktea_total += meltea_total 

                #arrays for order
                if qty_coffee !=0:
                    arr_coffee = ["Coffee",qty_coffee,total_coffee]
                    arr_types.append(arr_coffee[0])
                    arr_qty.append(str(arr_coffee[1]))
                    arr_price.append(str(arr_coffee[2]))

                if qty_strawberry !=0:
                    arr_strawberry = ["Strawberry",qty_strawberry,total_strawberry]
                    arr_types.append(arr_strawberry[0])
                    arr_qty.append(str(arr_strawberry[1]))
                    arr_price.append(str(arr_strawberry[2]))

                if qty_thai !=0:
                    arr_thai = ["Thai",qty_thai,total_thai]
                    arr_types.append(arr_thai[0])
                    arr_qty.append(str(arr_thai[1]))
                    arr_price.append(str(arr_thai[2]))

                if qty_banana !=0:
                    arr_banana = ["Banana",qty_banana,total_banana] 
                    arr_types.append(arr_banana[0])
                    arr_qty.append(str(arr_banana[1]))
                    arr_price.append(str(arr_banana[2]))

                if qty_matcha !=0:
                    arr_matcha = ["Matcha",qty_matcha,total_matcha]
                    arr_types.append(arr_matcha[0])
                    arr_qty.append(str(arr_matcha[1]))
                    arr_price.append(str(arr_matcha[2]))

                if qty_pearl !=0:
                    arr_pearl = ["Pearl",qty_pearl,total_pearl]
                    arr_types.append(arr_pearl[0])
                    arr_qty.append(str(arr_pearl[1]))
                    arr_price.append(str(arr_pearl[2]))

                messagebox.showinfo("Notice", "Order/s added.")
                self.destroy()
                menu=MainMenu(self)    

#CLASS OF MAIN MENU WINDOW
class MainMenu(Toplevel):
    def __init__(self, menu):
        self.menu_frame = menu
        Toplevel.__init__(self)
        #MAIN MENU WINDOW-ATTRIBUTES
        mainmenu = self

        #MAIN MENU WINDOW-PROPERTIES
        window_height = 490
        window_width = 730
        screen_width = mainmenu.winfo_screenwidth()
        screen_height = mainmenu.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        mainmenu.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        mainmenu.title("Drakeyshan Milktea Shop: "+current_user)
        mainmenu.configure(bg = "#ffffff")
        canvas = Canvas(mainmenu,bg = "#ffffff",height = 490,width = 730,
            bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        #MAIN MENU WINDOW-BACKGROUND
        background_img = PhotoImage(file = f"backgroundmm.png")
        background = canvas.create_image(371.0, 241.5,image=background_img)

        #MAIN MENU WINDOW-BUTTONS
        imgmt = PhotoImage(file = f"img0mm.png")
        mtbutton = Button(mainmenu, image = imgmt,borderwidth = 0,highlightthickness = 0,
            command = mainmenu.btn_milktea,relief = "flat")
        mtbutton.place(x = 300, y = 152,width = 130,height = 74)

        imft = PhotoImage(file = f"img1mm.png")
        ftbutton = Button(mainmenu, image = imft,borderwidth = 0,highlightthickness = 0,
            command = mainmenu.btn_fruittea,relief = "flat")
        ftbutton.place(x = 300, y = 235,width = 130,height = 74)

        imgc = PhotoImage(file = f"imgsmoothies.png")
        chocobutton = Button(mainmenu, image = imgc,borderwidth = 0,highlightthickness = 0,
            command = mainmenu.btn_smoothies,relief = "flat")
        chocobutton.place(x = 300, y = 318,width = 130,height = 74)

        imgcrt = PhotoImage(file = f"imgcart.png") 
        chocobutton = Button(mainmenu, image = imgcrt,borderwidth = 0,highlightthickness = 0,
            command = mainmenu.btn_cart,relief = "flat")
        chocobutton.place(x = 300, y = 405,width = 130,height = 74)

        #MAIN MENU WINDOW-LOOPINGS
        mainmenu.resizable(False, False)
        mainmenu.mainloop()

    #MAIN MENU WINDOW-FUNCTIONS

    def btn_clicked(self):
        print(current_user)

    def btn_milktea(self):
        self.withdraw()
        milktea = MilkTea(self)

    def btn_fruittea(self):
        self.withdraw() 
        fruittea = FruitTea(self)

    def btn_smoothies(self):
        self.withdraw()
        smoothies = Smoothies(self) 


    def btn_cart(self):
        cart = Cart(self)
        self.menu_frame.withdraw()

    def hide_window(self):
        self.menu_frame.withdraw()
    
#CLASS OF REGISTER WINDOW
class SignUpFrame(Toplevel):
    def __init__(self, signup):
        self.signup_frame = signup
        Toplevel.__init__(self)
        #REGISTER WINDOW-ATTRIBUTES
        global username
        global password
        username = StringVar()
        password = StringVar()    
        global signupwindow
        signupwindow = self
        
        #REGISTER WINDOW-PROPERTIES
        window_height = 490
        window_width = 730
        screen_width = signupwindow.winfo_screenwidth()
        screen_height = signupwindow.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        signupwindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        
        signupwindow.title("Signup Window")
        signupwindow.configure(bg = "#ffffff")
        canvas = Canvas(signupwindow,bg = "#ffffff",height = 490,width = 730,
            bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        #REGISTER WINDOW-BACKGROUND
        background_img = PhotoImage(file = f"backgroundsu.png")
        background = canvas.create_image(465.5, 237.5,image=background_img)

        #REGISTER WINDOW-TEXTBOX
        global email_entry_reg
        email_entry_reg = Entry(signupwindow,
            bd = 0,bg = "#ffffff",highlightthickness = 0,
            font="Helvetica", fg="#A66D6D")
        email_entry_reg.place(x = 90, y = 180, width = 215, height=20)

        global username_entry_reg
        username_entry_reg = Entry(signupwindow,
            bd = 0,bg = "#ffffff",highlightthickness = 0,
            font="Helvetica", fg="#A66D6D")
        username_entry_reg.place(x = 90, y = 250,width = 215,height = 20)

        global password_entry_reg
        password_entry_reg = Entry(signupwindow,
            bd = 0,bg = "#ffffff",highlightthickness = 0, show="*",
            fg="#A66D6D")
        password_entry_reg.place(x = 90, y = 330,width = 215,height = 20)

        #REGISTER WINDOW-BUTTONS
        imgcreate = PhotoImage(file = f"img0su.png")
        createbutton = Button(signupwindow, image = imgcreate,borderwidth = 0,highlightthickness = 0,
            command = self.register_user,relief = "flat")
        createbutton.place(x = 75, y = 379,width = 195,height = 74)

        imgexit = PhotoImage(file = f"img1su.png")
        exitbutton = Button(signupwindow, image = imgexit,borderwidth = 0,highlightthickness = 0,
            command = self.exit_reg,relief = "flat")
        exitbutton.place(x = 6, y = 3,width = 31,height = 40)

        #REGISTER WINDOW-LOOPINGS
        signupwindow.resizable(False, False)
        signupwindow.mainloop()

    #FUNCTIONS
    def btn_clicked():
        print("Button Clicked")

    def register_user(self):
        username_info = username_entry_reg.get()
        password_info = password_entry_reg.get()
        email_info = email_entry_reg.get()

        file=open(username_info,"w+")
        file.write(username_info+"\n")
        file.write(password_info)
        file.close()

        username_entry_reg.delete(0, END)
        password_entry_reg.delete(0, END)

        messagebox.showinfo(title="Registration Successful", message="Hello, "+username_info+". You are now registered.")
        self.destroy()
        self.signup_frame.show_window()

    def exit_reg(self):
        msgBox = messagebox.askquestion('Exit Registration', 'Are you sure you want to cancel your registration?', icon = 'error')
        if msgBox == 'yes':
            self.destroy()
            self.signup_frame.show_window()

    def hide_window(self):
        self.root.withdraw()

    def show_window(self):
        self.root.update()
        self.root.deiconify()          
        
#CLASS OF LOGIN WINDOW
class LoginFrame():  
    def __init__(self, parent):
        self.root = parent
        global current_user

        global arr_types
        arr_types = []

        global arr_qty
        arr_qty = []

        global arr_price
        arr_price = []

        global milktea_total
        milktea_total=0
        

        #LOGIN WINDOW-ATTRIBUTES
        global username_verify
        global password_verify
        username_verify = StringVar()
        password_verify = StringVar()

        #LOGIN WINDOW-PROPERTIES
        window_height = 490
        window_width = 730

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        self.root.title("Drakeyshan Milktea Shop Login")
        self.root.configure(bg = "#ffffff")
        canvas = Canvas(self.root,bg = "#ffffff",height = 490,width = 730,
            bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        #LOGIN WINDOW-BACKGROUND
        background_img = PhotoImage(file = f"backgroundlogin.png")
        background = canvas.create_image(297.0, 251.5,image=background_img)

        #LOGIN WINDOW-TEXTBOX
        global username_entry_login
        username_entry_login = Entry(
            bd = 0,bg = "#ffffff",highlightthickness = 0,
            font="Helvetica", fg="#A66D6D",textvariable=username_verify)
        username_entry_login.place(x = 470, y = 170,width = 215,height = 20)

        global password_entry_login
        password_entry_login = Entry(
            bd = 0,bg = "#ffffff",highlightthickness = 0, show="*",
            fg="#A66D6D",textvariable=password_verify)
        password_entry_login.place(x = 470, y = 245,width = 215,height = 20)

        #LOGIN WINDOW-BUTTONS
        imglogin = PhotoImage(file = f"img0login.png")
        loginbutton = Button(image = imglogin,borderwidth = 0,highlightthickness = 0,
            command = self.login_verify,relief = "flat")
        loginbutton.place(x = 501, y = 297,width = 100,height = 74)

        imgreg = PhotoImage(file = f"img1login.png")
        registerbutton = Button(image = imgreg,borderwidth = 0,highlightthickness = 0,
            command = self.register_window,relief = "flat")
        registerbutton.place(x = 486, y = 431,width = 132,height = 24)

        imgexit = PhotoImage(file = f"img2login.png")
        exitbutton = Button(image = imgexit,borderwidth = 0,highlightthickness = 0,
            command = self.exit_reg,relief = "flat")
        exitbutton.place(x = 683, y = 10,width = 31,height = 40)

        #LOGIN WINDOW-LOOPINGS
        self.root.resizable(False, False)
        self.root.mainloop()

    #FUNCTIONS
    def hide_window(self):
        self.root.withdraw()

    def show_window(self):
        self.root.update()
        self.root.deiconify()

    def exit_reg(self):
        msgBox = messagebox.askquestion('Exit Login', 'Are you sure you want to exit?', icon = 'error')
        if msgBox == 'yes':
            self.root.withdraw()       

    def btn_clicked(self):
        print("Button Clicked")

    def register_window(self):
        self.hide_window()
        signup = SignUpFrame(self)

    def login_verify(self):
        username_login = username_verify.get()
        password_login = password_verify.get()

        username_entry_login.delete(0, END)
        password_entry_login.delete(0, END)

        list_of_files = os.listdir()
        if username_login in list_of_files:
            file1 = open(username_login, "r")
            verify = file1.read().splitlines()
            if password_login in verify:
                messagebox.showinfo(title="Login Successful", message="Hello, "+username_login+". Logging in..")
                global current_user
                current_user = username_login
                self.hide_window()
                menu=MainMenu(self)
            else:
                messagebox.showwarning(title="Incorrect Password", message="Hello, "+username_login+". Is this you? Your password is not recognized.")
        else:
            messagebox.showerror(title="User Does Not Exist", message="There are no such user. Please register an account first.")

       
if __name__ == "__main__":
    root = Tk()
    app_instance = LoginFrame(root)
    root.mainloop()