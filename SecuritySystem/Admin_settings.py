import customtkinter
from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
import mysql.connector
from change_password import change_pass
import re
pattern_name = r'^[a-zA-Z]+$'
pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern_phone = r'^\d{4}-\d{7}$'
pattern_phone = r'^\d{4}-\d{7}$'
main_font = ('Century Gothic', 30)
font=('Century Gothic',20)
inner_font = ('Century Gothic', 12)
class AdminSettings:
# Constructor
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600+200+60")
        self.root.title("Admin Settings")
        self.root.resizable(0,0)
        root.wm_iconbitmap(r"face.ico")
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("green")
        self.root.configure(bg="gray10")
        self.switch_1 = customtkinter.StringVar()
        self.id_var=customtkinter.StringVar()
        # Background Image
        img1 = ImageTk.PhotoImage(Image.open(r"images\back.png"))
        self.l1 = customtkinter.CTkLabel(master=root, image=img1)
        self.l1.pack()
        # Main Frame
        self.frame = customtkinter.CTkFrame(master=self.l1, width=360, height=500,bg_color="black")
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # Labels
        self.edit_lbl = customtkinter.CTkLabel(self.frame, text="Edit Admin's Detail", font=font)
        self.edit_lbl.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        # Image
        img2 = ImageTk.PhotoImage(Image.open(r"images\edit.png").resize((100, 100)))
        self.l2 = customtkinter.CTkLabel(master=self.frame, image=img2, text="")
        self.l2.place(relx=0.5, y=117, anchor=tkinter.CENTER)
        # Edit Frame
        self.edit_frame = customtkinter.CTkFrame(self.frame, height=290, width=290, fg_color="transparent", border_width=1, border_color="grey")
        self.edit_frame.place(x=40, rely=0.4)
        # Switch
        self.switch = customtkinter.CTkSwitch(self.edit_frame, font=inner_font, text="Switch App Mode", command=self.change_color,
                                              variable=self.switch_1, onvalue="on", offvalue="off")
        self.switch.place(x=10, rely=0.88)
        # Separator
        self.l3 = customtkinter.CTkLabel(self.frame, height=0, text="________________________________________", text_color="darkblue")
        self.l3.place(relx=0.18, y=168)
        # Entry Labels
        self.id_lbl = customtkinter.CTkLabel(self.edit_frame, text="Admin id :", font=inner_font, fg_color="transparent")
        self.id_lbl.place(x=60, y=20)
        self.id = customtkinter.CTkEntry(self.edit_frame, width=70, font=inner_font, placeholder_text="Enter your id",textvariable=self.id_var,state="readonly")
        self.id.place(x=150, y=20)
        self.f_name_lbl = customtkinter.CTkLabel(self.edit_frame, font=inner_font, text="Enter new First Name :")
        self.f_name_lbl.place(x=10, y=60)
        self.f_name = customtkinter.CTkEntry(self.edit_frame, width=130, font=inner_font, placeholder_text="Enter new First Name")
        self.f_name.place(x=150, y=60)
        self.l_name_lbl = customtkinter.CTkLabel(self.edit_frame, font=inner_font, text="Enter new Last Name :")
        self.l_name_lbl.place(x=10, y=100)
        self.l_name = customtkinter.CTkEntry(self.edit_frame, width=130, font=inner_font, placeholder_text="Enter new Last Name")
        self.l_name.place(x=150, y=100)
        self.email_lbl = customtkinter.CTkLabel(self.edit_frame, font=inner_font, text="Enter new Email :")
        self.email_lbl.place(x=10, y=140)
        self.email = customtkinter.CTkEntry(self.edit_frame, width=130, font=inner_font, placeholder_text="Enter new Email")
        self.email.place(x=150, y=140)
        self.contact_lbl = customtkinter.CTkLabel(self.edit_frame, font=inner_font, text="Enter new Contact :")
        self.contact_lbl.place(x=10, y=180)
        self.contact = customtkinter.CTkEntry(self.edit_frame, width=130, font=inner_font, placeholder_text="Enter new Contact")
        self.contact.place(x=150, y=180)
        # Buttons
        self.edit_save_btn = customtkinter.CTkButton(self.edit_frame, width=130, text="Edit and Save", font=(('Century Gothic', 12)), cursor="hand2",command=self.update_details)
        self.edit_save_btn.place(x=10, y=220)
        self.clear_btn = customtkinter.CTkButton(self.edit_frame, width=130, text="Clear", font=(('Century Gothic', 12)), cursor="hand2",command=self.reset)
        self.clear_btn.place(x=150, y=220)
        self.button1=customtkinter.CTkButton(master=self.edit_frame,width=100,hover_color='gray', text="Change password?",font=('Century Gothic',12),fg_color="transparent",cursor="hand2",text_color="#0000FF",command=self.open_change_pass)
        self.button1.place(x=155,y=254)
        self.load_data()
# To reset the fields    
    def reset(self):
        self.id.focus(),
        self.f_name.focus(),
        self.l_name.focus(),
        self.email.focus(),
        self.contact.focus(),
        self.f_name.delete(0,"end"),
        self.l_name.delete( 0, "end"),
        self.email.delete( 0, "end"),
        self.contact.delete( 0, "end"),
        self.edit_frame.focus()
# To change the password
    def open_change_pass(self):
        win1 =Toplevel()
        app=change_pass(win1)    
# To change the apperance mode    
    def change_color(self):
        val = self.switch_1.get()
        if val == "on":
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("system")
# To load the data into text fields    
    def load_data(self):  
        try:
            conn =  mysql.connector.connect(host="localhost",username="root",password="@fyp2020",database="design")
            cursor = conn.cursor()
            cursor.execute("SELECT Id, First_Name, Last_Name, Email, Contact FROM admin")
            data = cursor.fetchone()
            self.id_var.set(data[0])
            self.f_name.delete(0, 'end')  
            self.f_name.insert(0, data[1])
            self.l_name.delete(0, 'end')  
            self.l_name.insert(0, data[2])
            self.email.delete(0, 'end')   
            self.email.insert(0, data[3])
            self.contact.delete(0, 'end') 
            self.contact.insert(0, data[4])
        # Set focus on one of the entry fields to make them editable
            self.f_name.focus()
        except Exception as e:
             messagebox.showerror("Error",f"Due to{str(e)} data could not be fetched.",parent=self.root) 
#  To Update details                        
    def update_details(self):
        data = (self.f_name.get(), self.l_name.get(), self.email.get(), self.contact.get())
        if "" in data:  # Checking if any of the fields are empty
            messagebox.showerror("Error", "Please fill all fields to edit.",parent=self.root)
        elif not re.match(pattern_name,self.f_name.get()):
            messagebox.showwarning("Invalid Name","Please Enter valid first name",parent=self.root)    
        elif not re.match(pattern_name,self.l_name.get()):
            messagebox.showwarning("Invalid Name","Please Enter valid last name",parent=self.root)  
        elif not re.match(pattern_email,self.email.get()):
            messagebox.showerror("Error","PLease Enter Valid Email. Your Email should follow the Format  xxx@xxx.com",parent=self.root)       
        elif not re.match(pattern_phone,self.contact.get()):
            messagebox.showwarning("Invalid Name","Employee's Contact should be in Correct Format (XXXX-XXXXXXX) .",parent=self.root) 
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
                cursor = conn.cursor()
                # Assuming your table name is 'admin' and 'Id' is the primary key
                cursor.execute("UPDATE admin SET First_Name = %s, Last_Name = %s, Email = %s, Contact = %s WHERE Id = %s", data + (self.id_var.get(),))
                conn.commit()
                messagebox.showinfo("Edited", "Details updated successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)}, details cannot be edited.", parent=self.root)
if __name__ == "__main__":
    root = customtkinter.CTk()
    admin_setting = AdminSettings(root)
    root.mainloop()


