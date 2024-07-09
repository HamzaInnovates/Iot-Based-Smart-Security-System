import customtkinter
from tkinter import *
from tkinter import messagebox
import tkinter
import mysql.connector
import re
pattern_password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[\w@$!%*?&]{8,}$'
main_font = ('Century Gothic', 30)
font=('Century Gothic',20)
inner_font = ('Century Gothic', 12)
class change_pass():
# Constructor
    def __init__(self,root):
        self.root=root
        self.root.geometry("380x300+500+220")
        self.root.title("Reset Password")
        self.root.resizable(0,0)
        root.wm_iconbitmap(r"face.ico")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        switch_1 = customtkinter.StringVar()
        self.ids = customtkinter.StringVar()
        self.main_frame=customtkinter.CTkFrame(self.root,width=1100,height=650)
        self.main_frame.pack()
        self.change_lbl = customtkinter.CTkLabel(self.main_frame,text="Change Password",font=font)
        self.change_lbl.place(relx=0.3,rely=0.1)
        self.change_frame = customtkinter.CTkFrame(self.main_frame,border_width=1,border_color="grey",width=334,height=200,fg_color="transparent")
        self.change_frame.place(relx=0.06,rely=0.3)
        self.switch = customtkinter.CTkSwitch(self.change_frame,font=inner_font,text="Switch App Mode",command=self.change_color,variable=switch_1,onvalue="on",offvalue="off")
        self.switch.place(x=10,rely=0.85)
        self.id_lbl=customtkinter.CTkLabel(self.change_frame,width=100,font=inner_font,text="ID :")
        self.id_lbl.place(x=60,y=10)
        self.id=customtkinter.CTkEntry(self.change_frame,width=100,font=inner_font,state="readonly",textvariable=self.ids)
        self.id.place(x=125,y=10)
        self.current_pass=customtkinter.CTkEntry(self.change_frame,width=145,font=inner_font,placeholder_text="Enter Current Password")
        self.current_pass.place(x=95,y=50)
        self.password_new = customtkinter.CTkEntry(self.change_frame,placeholder_text="Enter New Password",font=inner_font,show="*")
        self.password_new.place(x=10,y=90)
        self.confirm_password = customtkinter.CTkEntry(self.change_frame,placeholder_text="Confirm Password",font=inner_font,show="*")
        self.confirm_password.place(x=180,y=90)
        self.reset_btn = customtkinter.CTkButton(self.change_frame,text="Reset",font=inner_font,fg_color="green",command=self.change_pswd)
        self.reset_btn.place(x=10,y=134)
        self.reset_btn = customtkinter.CTkButton(self.change_frame,text="Clear",font=inner_font,fg_color="Red",command=self.reset)
        self.reset_btn.place(x=180,y=134)
        self.load_id()
# To change the appearance mode    
    def change_color(self):
        val = self.switch.get()
        if val == "off":
            customtkinter.set_appearance_mode("system")
        else:
            customtkinter.set_appearance_mode("dark")   
# To reset the fields
    def reset(self): 
        self.current_pass.focus(),
        self.password_new.focus(),
        self.confirm_password.focus(),
        self.current_pass.delete(0,"end"),
        self.password_new.delete(0,"end"),
        self.confirm_password.delete(0,"end"),
        self.main_frame.focus()
# To load the id on runtime
    def load_id(self):
        try:
            conn =  mysql.connector.connect(host="localhost",username="root",password="@fyp2020",database="design")
            cursor=conn.cursor()
            cursor.execute("Select Id from admin")
            data =cursor.fetchone()
            self.ids.set(data[0])
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
# To change the password
    def change_pswd(self):
        current_pass_value = self.current_pass.get()
        if current_pass_value == "":
            messagebox.showerror("Error", "Please enter your current password first to change the password.")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
            cursor = conn.cursor()
            cursor.execute("SELECT Password FROM admin WHERE Id=%s", (self.ids.get(),))
            data_2 = cursor.fetchone()[0]
            if data_2 is not None and current_pass_value.strip()==data_2.strip():
                if self.confirm_password.get() == "" or self.password_new.get() == "":
                    messagebox.showerror("'Error","Please fill all fields. ",parent=self.root)
                elif not re.match(pattern_password, self.password_new.get()):
                    messagebox.showerror("Error", "Please choose a strong password. Your password should contain at least one uppercase letter, at least one lowercase letter, at least one digit, at least one special character among @$!%*?& and minimum length of 8 characters.", parent=self.root)
                elif self.confirm_password.get() != self.password_new.get():
                    messagebox.showwarning("Warning", "New passwords do not match .",parent=self.root)
                else:
                    cursor.execute("UPDATE admin SET Password=%s WHERE Id=%s", (self.password_new.get(), self.ids.get(),))
                    conn.commit()
                    messagebox.showinfo("Success", "Password changed successfully.",parent=self.root)
                    self.reset()     
            else:
                messagebox.showerror("Error", "Invalid Current Password.",parent=self.root)                     
if __name__=="__main__":
    root=customtkinter.CTk()
    win=change_pass(root)
    root.mainloop()        
    