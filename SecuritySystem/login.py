#importing necessary modules
import customtkinter
from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from Forget_password import forget_password
from main import Main
from Register import register
import mysql.connector
import re
main_font = ('Century Gothic', 30)
font=('Century Gothic',20)
inner_font = ('Century Gothic', 12)
#Creating a class for login screen
class login():
# Constructor
    def __init__(self,root):
        self.switch_1 = customtkinter.StringVar()
        self.root = root
        self.root.geometry("1000x600+200+60") #defining window's size
        self.root.title("Login") #window's title
        root.wm_iconbitmap(r"face.ico")
        self.root.resizable(0,0) ##window cannot be resized
        customtkinter.set_appearance_mode("system") # appearnace mode
        customtkinter.set_default_color_theme("green")
        # Creation of all of the widgets
        self.img1=ImageTk.PhotoImage(Image.open(r"images\back.png"))
        self.l1=customtkinter.CTkLabel(master=root,image=self.img1)
        self.l1.pack()
        self.frame=customtkinter.CTkFrame(master=self.l1, width=320, height=360)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.l2=customtkinter.CTkLabel(master=self.frame, text="Log into your Account",font=('Century Gothic',20))
        self.l2.place(x=50, y=45)
        self.switch = customtkinter.CTkSwitch(self.frame, font=inner_font, text="Switch App Mode", command=self.change_color,
                                              variable=self.switch_1, onvalue="on", offvalue="off")
        self.switch.place(x=20, rely=0.88)
        self.img2 = ImageTk.PhotoImage(Image.open(r"images\icons8-user-32.png").resize((25,25)))
        self.l3=customtkinter.CTkLabel(self.frame,image=self.img2,text="")
        self.l3.place(x=27,y=108)
        self.entry1=customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Username')
        self.entry1.place(x=50, y=110)
        self.img2 = ImageTk.PhotoImage(Image.open(r"images\icons8-key-48.png").resize((20,20)))
        self.l3=customtkinter.CTkLabel(self.frame,image=self.img2,text="")
        self.l3.place(x=27,y=166)
        self.entry2=customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Password', show="*")
        self.entry2.place(x=50, y=165)
        self.button1=customtkinter.CTkButton(master=self.frame,hover_color='gray', text="Forget password?",font=('Century Gothic',12),fg_color="transparent",cursor="hand2",text_color="black",command=self.open_forget_screen)
        self.button1.place(x=155,y=195)
        self.button2 = customtkinter.CTkButton(master=self.frame, width=220, text="Login", command=self.login, corner_radius=6)
        self.button2.place(x=50, y=240)
        self.lbl = customtkinter.CTkLabel(self.frame,text="Don't have an account?")
        self.lbl.place(x=50,y=270)
        self.button3=customtkinter.CTkButton(self.frame,text="Register Here",hover_color="gray",width=20,fg_color="transparent",text_color="blue",cursor="hand2",command=self.open_register_screen)
        self.button3.place(x=180,y=270)
# To change the appearance mode
    def change_color(self):
        val = self.switch_1.get()
        if val == "on":
            customtkinter.set_appearance_mode("dark") 
            customtkinter.set_default_color_theme("green")  
        else:
            customtkinter.set_appearance_mode("system") 
            customtkinter.set_default_color_theme("green")       
# To login to the system
    def login(self):
        if self.entry1.get()=="" or self.entry2.get()=="":
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
        else : 
            try:
                conn =mysql.connector.connect(host="localhost",username="root",password="@fyp2020",database="design")   
                cursor=conn.cursor() 
                cursor.execute("SELECT Email,Password from admin where Email = %s",(self.entry1.get(),))
                data=cursor.fetchone()
                conn.commit()
                if data is not None:
                    if data[0]==self.entry1.get() and data[1]==self.entry2.get():
                        messagebox.showinfo("Success","Login Successful",parent=self.root)
                        self.open_main_screen()
                    else:
                        messagebox.showinfo("Login Error","Invalid Credentials",parent=self.root)
                else:
                        messagebox.showinfo("Login Error","Invalid Credentials",parent=self.root)             
                
            except Exception as e:
                messagebox.showerror("Error",f"Due to  {str(e)} the request cannot be proceeded.", parent=self.root)        
# To switch to the forget screen
    def open_forget_screen(self):
        newwin = Toplevel(self.root)
        app = forget_password(newwin)
        newwin.focus_set()
# To open main screen
    def open_main_screen(self):
        self.root.withdraw()
        newwin = Toplevel(self.root)
        app = Main(newwin)
        newwin.focus_set()
#opening register_screen from the login screen
    def open_register_screen(self):
        self.root.withdraw()
        newwin = Toplevel(self.root)
        app = register(newwin) 
        newwin.focus_set() 
# Creating window object      
if __name__=="__main__":
    root=customtkinter.CTk()
    win1=login(root)
    root.mainloop()
      