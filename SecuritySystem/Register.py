# importing neccessary modules
import customtkinter
from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from Forget_password import forget_password
import mysql.connector
import re
from main import Main
main_font = ('Century Gothic', 30)
font=('Century Gothic',20)
inner_font = ('Century Gothic', 12)
#defining patterns for input field constraints
pattern_name = r'^[a-zA-Z]+$'
pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern_phone = r'^\d{4}-\d{7}$'
pattern_password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[\w@$!%*?&]{8,}$'
#object for this winow
def main():
    root=customtkinter.CTk()
    app=register(root)
    root.mainloop()
class register():
# Constructor
    def __init__(self,root):
        self.switch_1 = customtkinter.StringVar()
        self.root =root
        self.root.geometry("1000x600+200+60")
        self.root.title("Registeration Form")
        self.root.resizable(0,0)
        root.wm_iconbitmap(r"face.ico")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        #Creating widgets
        self.img=ImageTk.PhotoImage(Image.open(r"images\back.png"))
        self.l1=customtkinter.CTkLabel(master=self.root,image=self.img)
        self.l1.pack()
        self.mainframe = customtkinter.CTkFrame(self.l1,width=400,height=550,bg_color="black")
        self.mainframe.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        self.frame = customtkinter.CTkFrame(self.mainframe,width=400,height=550)
        self.frame.pack()
        self.switch = customtkinter.CTkSwitch(self.frame,font=inner_font,text="Switch App Mode",command=self.change_color,variable=self.switch_1,onvalue="on",offvalue="off")
        self.switch.place(x=20,rely=0.9)
        self.l2=customtkinter.CTkLabel(master=self.frame, text="Create a new Account",font=font)
        self.l2.place(x=80, y=30)
        self.img1=ImageTk.PhotoImage(Image.open(r"images\add-user.png").resize((100,100)))
        self.l2=customtkinter.CTkLabel(master=self.frame,image=self.img1,text="")
        self.l2.place(relx=0.5,y=117,anchor=tkinter.CENTER)
        self.l3 = customtkinter.CTkLabel(self.frame,height=0,text="________________________________________",text_color="darkblue")
        self.l3.place(relx=0.2,y=168)
        self.entry_frame=customtkinter.CTkFrame(self.frame,border_width=1,width=320,height=280,fg_color="transparent",corner_radius=40,border_color="gray")
        self.entry_frame.place(relx=0.1,y=200)
        self.l2=customtkinter.CTkLabel(master=self.entry_frame,height=20, text="Enter Your Details Below",font=font)
        self.l2.place(relx=0.5,rely=0.05,anchor=tkinter.CENTER)
        self.f_name=customtkinter.CTkEntry(self.entry_frame,font=inner_font,placeholder_text="First Name")
        self.f_name.place(relx=0.05,y=40)
        self.l_name=customtkinter.CTkEntry(self.entry_frame,font=inner_font,placeholder_text="Last Name")
        self.l_name.place(relx=0.5,y=40)
        self.contact=customtkinter.CTkEntry(self.entry_frame,font=inner_font,placeholder_text="Contact")
        self.contact.place(relx=0.05,y=80)
        self.email=customtkinter.CTkEntry(self.entry_frame,font=inner_font,placeholder_text="Email")
        self.email.place(relx=0.5,y=80)
        self.ques=customtkinter.CTkComboBox(self.entry_frame,font=inner_font,values=["Security Question","Friend's Name","Pet's Name","Favourite Hobby","Date of Birth"])
        self.ques.place(relx=0.05,y=120)
        self.ans=customtkinter.CTkEntry(self.entry_frame,font=inner_font,placeholder_text="Security Answer")
        self.ans.place(relx=0.5,y=120)
        self.password=customtkinter.CTkEntry(self.entry_frame,font=inner_font,placeholder_text="Password",show="*")
        self.password.place(relx=0.05,y=160)
        self.confirm_password=customtkinter.CTkEntry(self.entry_frame,font=inner_font,placeholder_text="Confirm Password",show="*")
        self.confirm_password.place(relx=0.5,y=160)
        self.submit = customtkinter.CTkButton(self.entry_frame,text_color="black",cursor="hand2",width=200,text="Submit",font=inner_font,command=self.reg_admin)
        self.submit.place(x=60,y=200)
        self.labl = customtkinter.CTkLabel(self.entry_frame,font=inner_font,text="Already a member?")
        self.labl.place(x=80,y=230)
        self.button4=customtkinter.CTkButton(self.entry_frame,text="Login",command=self.login,hover_color="gray",width=14,fg_color="transparent",text_color="blue",cursor="hand2")
        self.button4.place(x=198,y=230)     
# Back to login screen from the register screen
    def login(self):
        self.root.withdraw()
        newwin = Toplevel(self.root)
        app = login(newwin)         
# Changing the appearance mode
    def change_color(self):
        val = self.switch_1.get()
        if val == "on":
            customtkinter.set_appearance_mode("system")
            customtkinter.set_default_color_theme("green")
        else:
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("green")     
 #registration of an admin
    def reg_admin(self):
        if self.f_name.get() =="" or self.l_name.get()=="" or self.contact.get()=="" or self.email.get()=="" or self.ques.get()=="" or self.ans.get()=="" or self.password.get()=="" or self. confirm_password.get()=="":
            messagebox.showerror("Error" ,"All Fields are required !", parent=self.root)
            return False
        elif  not re.match(pattern_name, self.f_name.get()) :
            messagebox.showerror("Error","PLease Enter Valid First_name.",parent=self.root)
            return False
        elif not re.match(pattern_name,self.l_name.get()):
            messagebox.showerror("Error","PLease Enter Valid Last_name.")
            return False
        elif not re.match(pattern_phone,self.contact.get()):
            messagebox.showerror("Error", "Contact should be in Correct Format (XXXX-XXXXXXX) .",parent=self.root)
            return False
        elif  not re.match(pattern_email, self.email.get()) :
            messagebox.showerror("Error","PLease Enter Valid Email. Your Email should follow the Format  xxx@xxx.com",parent=self.root)
            return False
        elif self.ques.get()=="Security Question":
            messagebox.showerror("Error","Please Select the Security Question",parent=self.root) 
            return False
        elif not re.match(pattern_password,self.password.get()):
            messagebox.showerror("Error","PLease choose a strong password 'Your password should contain At least one uppercase letter ,At least one lowercase letter,  At least one digit, At least one special character among @$!%*?& and minimum length of 8 characters'.",parent=self.root)
            return False
        elif self.password.get()!=self.confirm_password.get():
            messagebox.showwarning('Password Mismatch', 'The password does not match.\n Please try again.',parent=self.root)
            return False
        else :
            try:
                conn =  mysql.connector.connect(host="localhost",username="root",password="@fyp2020",database="design")
                cursor=conn.cursor()
                cursor.execute("Select * from admin")
                admin_data =cursor.fetchall()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}")
            if admin_data ==[]:
                try:
                    messagebox.showinfo("Remember","Remeber Your Choosen Security Question and Answer, incase you want to reset the password !",parent=self.root)
                    data = (self.f_name.get(),self.l_name.get(),self.contact.get(),self.email.get(),self.ques.get(),self.ans.get(),self.password.get(),)
                    conn =  mysql.connector.connect(host="localhost",username="root",password="@fyp2020",database="design")   
                    cursor=conn.cursor()
         
                    cursor.execute("INSERT INTO admin(First_name,Last_name,Contact,Email,Security_Ques,Security_Ans,Password) VALUES (%s,%s,%s,%s,%s,%s,%s)",data) 
                    conn.commit() 
                    self.reset()
                    response=messagebox.askyesno("DataSaved","Registration Successfull! Do You Want to login?",parent=self.root)
                    if response >0:
                        self.login()
                except Exception as e:
                    messagebox.showerror("Error", f"Due to {str(e)} regitraion cannot be done!",parent=self.root)  
            else:
                 messagebox.showwarning("Limit Exceeded","There could only be one admin. ThankYou!",parent=self.root)                
# Setting the input fields to null or empty                   
    def reset(self):
        self.f_name.focus(),
        self.l_name.focus(),
        self.contact.focus(),
        self.email.focus(),
        self.ques.focus(),
        self.ans.focus(),
        self.password.focus(),
        self.confirm_password.focus(),
        self.f_name.delete(0,"end"),
        self.l_name.delete(0,"end"),
        self.contact.delete(0,"end"),
        self.email.delete(0,"end"),
        self.ques.set("Security Question"),
        self.ans.delete(0,"end"),
        self.password.delete(0,"end"),
        self.confirm_password.delete(0,"end"),
        self.mainframe.focus()
 ##class login               
class login():
    #Constructor
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
        self.frame=customtkinter.CTkFrame(master=self.l1, width=320, height=360,bg_color="black")
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
     
# Change appearance mode
    def change_color(self):
        val = self.switch_1.get()
        if val == "on":
            customtkinter.set_appearance_mode("dark") 
            customtkinter.set_default_color_theme("green")  
        else:
            customtkinter.set_appearance_mode("system") 
            customtkinter.set_default_color_theme("green") 
        
# Login to main screen      
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
        
# Opening forget_password screen from the login screen
    def open_forget_screen(self):
        newwin = Toplevel(self.root)
        app = forget_password(newwin)
        newwin.focus_set()
# Opening forget_password screen from the login screen
    def open_main_screen(self):
        self.root.withdraw()
        newwin = Toplevel(self.root)
        app = Main(newwin)
        newwin.focus_set()
        
# Opening register_screen from the login screen
    def open_register_screen(self):
        self.root.withdraw()
        newwin = Toplevel(self.root)
        app = register(newwin) 
        newwin.focus_set()         
if __name__=="__main__":
    main()