#importing neccessary modules
import customtkinter
from tkinter import *
from tkcalendar import *
from tkinter import ttk, messagebox,Tk
import tkinter as tk
import mysql.connector
import re
import cv2
import tkinter
from PIL import Image,ImageTk
#defining patterns for input field constraints
pattern = r'^[a-zA-Z]+$'
pattern_date=r'^\d{2}/\d{2}/\d{4}$'
pattern_phone = r'^\d{4}-\d{7}$'
pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
main_font = ('Century Gothic', 30)
font=('Century Gothic',20)
inner_font = ('Century Gothic', 12)
#class employee
class Employee():
# Constructor
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x650+180+40")
        self.root.title("Employee Details")
        self.root.resizable(0,0)
        root.wm_iconbitmap(r"face.ico")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root.configure(bg="gray10")
        self.id = customtkinter.StringVar()
        self.facial_data = customtkinter.StringVar()
        self.switch_1 = customtkinter.StringVar()
        #calling the function to load the widgets
        self.create_widgets()
# Widgets
    def create_widgets(self):
        style=ttk.Style()
        style.configure('Treeview',
        background="silver",
        foreground="black"
        )
        style.theme_use('default')
        style.map('Treeview',
        background=[('selected','green')])
        self.main_frame=customtkinter.CTkFrame(self.root,width=1100,height=650)
        self.main_frame.pack()
        self.top_frame=customtkinter.CTkFrame(self.main_frame,width=1060,height=500,border_width=2,fg_color="transparent")
        self.top_frame.place(relx=0.5,rely=0.6,anchor= tkinter.CENTER)
        self.main_frame.configure(bg_color="transparent")
        self.main_label = customtkinter.CTkLabel(self.main_frame,text="Welcome to Smart Security System",font=font)
        self.main_label.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
        self.left_frame =customtkinter.CTkFrame(self.top_frame,border_width=2,height=500,width=480,fg_color="transparent")
        self.left_frame.place(x= 240,rely=0.5,anchor=tkinter.CENTER)
        self.label_employee = customtkinter.CTkLabel(self.left_frame,text="Add New Employee",font=font)
        self.label_employee.place(relx=0.5,rely=0.05,anchor= tkinter.CENTER)
        self.employee_entries = customtkinter.CTkFrame(self.left_frame,height=430,width=400,fg_color="transparent",border_width=2)
        self.employee_entries.place(x=30,y=50)
        self.emp_id_lbl = customtkinter.CTkLabel(self.employee_entries,text="Employee Id :",font=('Century Gothic',12,"bold"))
        self.emp_id_lbl.place(x = 92 ,y = 15)
        self.emp_id= customtkinter.CTkEntry(self.employee_entries,state="readonly",font=inner_font,textvariable=self.id)
        self.emp_id.place(x=190,y=15)
        self.emp_first = customtkinter.CTkEntry(self.employee_entries,placeholder_text="First Name",height=30,width=170,font=inner_font)
        self.emp_first.place(x=22,y=60)
        self.emp_last = customtkinter.CTkEntry(self.employee_entries,placeholder_text="Last Name",height=30,width=170,font=inner_font)
        self.emp_last.place(x=210,y=60)
        self.emp_contact=customtkinter.CTkEntry(self.employee_entries,placeholder_text="Contact No",height=30,width=170,font=inner_font)
        self.emp_contact.place(x=22,y=105)
        self.emp_email = customtkinter.CTkEntry(self.employee_entries,placeholder_text="Email Address",height=30,width=170,font=inner_font)
        self.emp_email.place(x=210,y=105)
        self.emp_gender=customtkinter.CTkComboBox(self.employee_entries,values=["Male","Female"],height=30,width=170,font=inner_font)
        self.emp_gender.place(x=22,y=150)
        self.emp_dob = customtkinter.CTkEntry(self.employee_entries,placeholder_text="Date of Birth",height=30,width=170,font=inner_font)
        self.emp_dob.place(x=210,y=150)
        self.emp_dob.bind("<ButtonRelease-1>",self.pick_date)
        self.emp_dep=customtkinter.CTkComboBox(self.employee_entries,values=["Select Department","Computer Science","Artificial Intelligence","English","Management","Psychology","Bio Sciences","Mathematics"],height=30,width=170,font=inner_font)
        self.emp_dep.place(x=22,y=195)
        self.emp_designation = customtkinter.CTkEntry(self.employee_entries,placeholder_text="Designation",height=30,width=170,font=inner_font)
        self.emp_designation.place(x=210,y=195)
        self.emp_facialdata =customtkinter.CTkFrame(self.employee_entries,width=360,height=60,fg_color="transparent",border_width=2)
        self.emp_facialdata.place(x=20,rely=0.58)
        self.facial_lbl =customtkinter.CTkLabel(self.emp_facialdata,text="Facial data",fg_color="transparent", font=inner_font,height=0)
        self.facial_lbl.place(x=0,y=0)
        self.radio_yes = customtkinter.CTkRadioButton(self.emp_facialdata,text="Yes",value="Yes",font=inner_font,variable=self.facial_data,state=DISABLED)
        self.radio_yes.place(x=10,y=33)
        self.radio_yes.bind("<ButtonRelease>",self.show_msg)
        self.radio_no = customtkinter.CTkRadioButton(self.emp_facialdata,text="No",value="No",font=inner_font,variable=self.facial_data)
        self.radio_no.place(x=80,y=33)
        self.button_frame=customtkinter.CTkFrame(self.employee_entries,fg_color="transparent",width=360,height=100,border_width=2)
        self.button_frame.place(x=20,rely=0.73)
        self.save = customtkinter.CTkButton(self.button_frame,text="Save",font=inner_font,width=100,cursor="hand2",command=self.savedata)
        self.save.place(x=10,y=10)
        self.update_btn = customtkinter.CTkButton(self.button_frame,text="Update",font=inner_font,width=100,cursor="hand2",command=self.update)
        self.update_btn.place(x=130,y=10)
        self.delete = customtkinter.CTkButton(self.button_frame,text="Delete",font=inner_font,width=100,cursor="hand2",command=self.del_data)
        self.delete.place(x=250,y=10)
        self.reset_btn = customtkinter.CTkButton(self.button_frame,text="Clear",font=inner_font,width=165,cursor="hand2",command=self.reset)
        self.reset_btn.place(x=185,y=50)
        self.photo_sample = customtkinter.CTkButton(self.button_frame,cursor="hand2",text="Take Photo Sample",fg_color="green",font=inner_font,width=170,command=self.dataset)
        self.photo_sample.place(x=10,y=50)
        self.right_frame =customtkinter.CTkFrame(self.top_frame,border_width=2,height=500,width=578,fg_color="transparent")
        self.right_frame.place(x= 770,rely=0.5,anchor=tkinter.CENTER)
        self.search_employee = customtkinter.CTkLabel(self.right_frame,text="Search Employee",font=font)
        self.search_employee.place(relx=0.5,rely=0.05,anchor= tkinter.CENTER)
        self.search_system=customtkinter.CTkFrame(self.right_frame,width=544,height=430,border_width=2,fg_color="transparent")
        self.search_system.place(x=15,y=50)
        self.search_frame=customtkinter.CTkFrame(self.search_system,width=530,height=60,border_width=2)
        self.search_frame.place(x=5,y=8)
        self.lbl_search=  customtkinter.CTkLabel(self.search_frame,text="Search By",font=('Century Gothic',14,"bold"))
        self.lbl_search.place(x=10,y=10)
        self.search_cmb=customtkinter.CTkComboBox(self.search_frame,font=inner_font,values=["Employee_Id", "First_Name","last_Name","Email","Gender","DOB","Dep","Des"])
        self.search_cmb.place(y=10,x=80)
        self.search_entry = customtkinter.CTkEntry(self.search_frame,font=inner_font,placeholder_text="Enter Value to Search")
        self.search_entry.place(y=10,x=230)
        self.search_btn=customtkinter.CTkButton(self.search_frame,text="Search",font=inner_font,width=60,cursor="hand2",command=self.search_by)
        self.search_btn.place(y=10,x=380)
        self.View_btn=customtkinter.CTkButton(self.search_frame,text="View All",font=inner_font,width=60,cursor="hand2",command=self.view_data)
        self.View_btn.place(y=10,x=450)
        self.tble = ttk.Treeview(self.search_system)
        self.tble.configure(yscrollcommand=self.tble.yview,xscrollcommand=self.tble.xview)
        self.tble["columns"]=("Id", "First Name","Last Name","Contact Number","Email","Gender","DOB","Dep","Designation","Facial Data")
        self.tble.column("#0",width=0,stretch=tk.NO)
        self.tble.column("Id",width=18,anchor=tk.CENTER)
        self.tble.column("First Name",width=50,anchor=tk.CENTER)
        self.tble.column("Last Name",width=50,anchor=tk.CENTER)
        self.tble.column("Contact Number",width=50,anchor=tk.CENTER)
        self.tble.column("Email",width=60,anchor=tk.CENTER)
        self.tble.column("Gender",width=40,anchor=tk.CENTER)
        self.tble.column("DOB",width=45,anchor=tk.CENTER)
        self.tble.column("Dep",width=40,anchor=tk.CENTER)
        self.tble.column("Designation",width=50,anchor=tk.CENTER)
        self.tble.column("Facial Data",width=50,anchor=tk.CENTER)
        self.tble.heading("Id",text="Id")
        self.tble.heading("First Name",text="f_Name")
        self.tble.heading("Last Name",text="l_Name")
        self.tble.heading("Contact Number",text="Contact")
        self.tble.heading("Email",text="Email")
        self.tble.heading("Gender",text="Gender")
        self.tble.heading("DOB",text="DOB")
        self.tble.heading("Dep",text="Dep")
        self.tble.heading("Designation",text="Des")
        self.tble.heading("Facial Data",text="Facial_Data")
        self.tble.place(x=5,y=70,width=530,height=355)
        self.scrollbar = customtkinter.CTkScrollbar(self.search_system, command=self.tble.yview,height=370)
        self.scrollbar.place(relx=0.97,rely=0.1)
        self.tble.bind("<ButtonRelease>",self.get_treeview_data)
        self.switch = customtkinter.CTkSwitch(self.main_frame,font=inner_font,text="Switch App Mode",command=self.change_color,variable=self.switch_1,onvalue="on",offvalue="off")
        self.switch.place(x=20,y=20)
        self.tble.configure(yscrollcommand=self.scrollbar.set)
        self.view_data()
# To display information to take the photo sample after selecting yes
    def show_msg(self,event):
        if self.radio_yes._state==NORMAL:
            messagebox.showinfo("Note","Please click the button 'PhotoSample' to take the photosample of this employee",parent=self.root)     
# To search the employee through its attributes
    def search_by(self):
        try:
            self.tble.delete(*self.tble.get_children())
            conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employee WHERE " + self.search_cmb.get() + " = %s", (self.search_entry.get(),))
            rows = cursor.fetchall()
            for i in rows:
                self.tble.insert('', 'end', values=i)
            conn.commit()
            conn.close() 
        except Exception as e:
            # Show a messagebox with the error message
            messagebox.showerror("Error", f"Due to {str(e)}, data could not be displayed",parent=self.root)    
# To chnage the appearance mode
    def change_color(self):
        val = self.switch_1.get()
        if val == "on" or val == "":
            customtkinter.set_appearance_mode("light")
            customtkinter.set_default_color_theme("dark-blue")
        else:
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("dark-blue")   
#displays  data in tree view
    def view_data(self):
        try:
            self.tble.delete(*self.tble.get_children())
            conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employee")
            rows = cursor.fetchall()
            for i in rows:
                self.tble.insert('', 'end', values=i)
            conn.commit()
            conn.close() 
        except Exception as e:
            messagebox.showerror("Error",f"Due to {str(e)} data could be displayed",parent=self.root)     
# saving data to database
    def savedata(self):
        if self.emp_first.get() == "" or self.emp_last.get() == "" or self.emp_contact.get() == "" or self.emp_email.get() == "" or self.emp_gender.get() == "" or self.emp_dob.get() == "" or self.emp_dep.get() == "" or self.emp_designation.get() == "" :
            messagebox.showerror("Missing Field", "Please Enter All The Required Fields!",parent=self.root)
            return False 
        elif  not re.match(pattern, self.emp_first.get()) :
            messagebox.showerror("Error","PLease Enter Valid First_name",parent=self.root)
            return False 
        elif not re.match(pattern,self.emp_last.get()):
            messagebox.showerror("Error","PLease Enter Valid Last_name",parent=self.root)
            return False 
        elif not re.match(pattern_phone,self.emp_contact.get()):
            messagebox.showerror("Error", "Employee's Contact should be in Correct Format (XXXX-XXXXXXX) .",parent=self.root)       
            return False 
        elif not re.match(pattern_email,self.emp_email.get()):
            messagebox.showerror("Error","PLease Enter Valid Email. Your Email should follow the Format  xxx@xxx.com",parent=self.root)
            return False 
        elif not re.match(pattern_date,self.emp_dob.get()):
            messagebox.showerror("Error","PLease Enter Valid Date of Birth",parent=self.root)
            return False 
        elif self.emp_dep.get()=="Select Department":
            messagebox.showerror("Error","Please Select the department",parent=self.root)          
            return False 
        elif not re.match(pattern,self.emp_designation.get()):
            messagebox.showerror("Error","PLease Enter Valid Designation",parent=self.root)
            return False
        elif self.facial_data.get() == "" or len(self.facial_data.get())>3:
            messagebox.showerror("Error", "Please select the facial data", parent=self.root)
            return False
        else: 
            conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employee where Employee_id=%s", (self.id.get(),))  # Changed id.get() to self.id.get()
            row = cursor.fetchone()
            if row:
                messagebox.showerror("Error", "Data Already exist", parent=self.root)
                return False 
            else:
                try:  
                    global cal, win 
                    cast = str(cal.get_date())
                    data = (self.emp_first.get(), self.emp_last.get(), self.emp_contact.get(), self.emp_email.get(), self.emp_gender.get(),
                            cast, self.emp_dep.get(), self.emp_designation.get(), self.facial_data.get(),)            
                    cursor.execute("INSERT INTO employee (First_Name, Last_Name, Contact, Email, Gender, DOB, Dep, Des, Facialdata) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
                    conn.commit()
                    messagebox.showinfo("Success", "Data has been saved Successfully. Please select the data from the list to Take Photosample", parent=self.root)
                    self.view_data()
                    self.reset()
                except Exception as e:
                    messagebox.showerror("Error", f"Due to {e} the data could not be inserted.", parent=self.root)
                    return False
                finally:
                    conn.close()
# To create a date picker
    def pick_date(self, event=None):
        global cal, win
        win = Toplevel()
        win.geometry("280x250+450+400")
        cal = Calendar(win, selectmode="day", date_pattern="dd/mm/yyyy")
        cal.pack()
        btn = customtkinter.CTkButton(win, text="Submit", command=self.getdate)
        btn.pack(pady=10)
        win.mainloop()
# To get the date from the datepicker
    def getdate(self):
        self.emp_dob.delete(0, END)
        cast = str(cal.get_date())
        self.emp_dob.insert(0, cast) 
        win.destroy()    
# To get the data from the treevirw    
    def get_treeview_data(self, event):
        focus = self.tble.focus()
        data_content = self.tble.item(focus)
        data_store = data_content["values"]
        self.id.set(data_store[0])
        if not self.id.get()=="":
            self.radio_yes.configure(state=NORMAL)
            self.emp_first.delete(0, 'end')
            self.emp_first.insert(0, data_store[1])
            self.emp_last.delete(0, 'end')
            self.emp_last.insert(0, data_store[2])
            self.emp_contact.delete(0, 'end')
            self.emp_contact.insert(0, data_store[3])
            self.emp_email.delete(0, 'end')
            self.emp_email.insert(0, data_store[4])
            self.emp_gender.set(data_store[5])
            self.emp_dob.delete(0, 'end')
            self.emp_dob.insert(0, data_store[6])
            self.emp_dep.set(data_store[7])
            self.emp_designation.delete(0, 'end')
            self.emp_designation.insert(0, data_store[8])
            self.facial_data.set(data_store[9])
# Reset fields to null
    def reset(self):
        self.emp_first.focus(),
        self.emp_last.focus(),
        self.emp_contact.focus(),
        self.emp_email.focus(),
        self.emp_gender.focus(),
        self.emp_dep.focus(),
        self.emp_designation.focus(),
        self.emp_dob.focus(),
        self.id.set(""),
        self.emp_first.delete(0,"end"),
        self.emp_last.delete(0,"end"),
        self.emp_contact.delete(0,"end"),
        self.emp_email.delete(0,"end"),
        self.emp_gender.set("Male"),
        self.emp_dep.set("Select Department"),
        self.emp_designation.delete(0,"end"),
        self.emp_dob.delete(0,"end"),
        self.facial_data.set(None),
        self.radio_yes.configure(state=DISABLED),
        self.employee_entries.focus()
# To update the employee
    def update(self):
        data = (self.emp_first.get(), self.emp_last.get(), self.emp_contact.get(), self.emp_email.get(), self.emp_gender.get(),
                self.emp_dob.get(), self.emp_dep.get(), self.emp_designation.get(), self.facial_data.get(),)
        if self.id.get() == "" or self.facial_data.get()==None :
            messagebox.showerror("Missing Field", "No Data Found! Select the Employee to be updated.",parent=self.root)
            return False
        elif  any(value == "" for value in data):
            messagebox.showerror("Missing Field", "Please Enter All The Required Fields!",parent=self.root)
            return False 
        elif  not re.match(pattern, self.emp_first.get()) :
            messagebox.showerror("Error","PLease Enter Valid First_name",parent=self.root)
            return False 
        elif not re.match(pattern,self.emp_last.get()):
            messagebox.showerror("Error","PLease Enter Valid Last_name",parent=self.root)
            return False 
        elif not re.match(pattern_phone,self.emp_contact.get()):
            messagebox.showerror("Error", "Employee's Contact should be in Correct Format (XXXX-XXXXXXX) .",parent=self.root)       
            return False 
        elif not re.match(pattern_email,self.emp_email.get()):
            messagebox.showerror("Error","PLease Enter Valid Email. Your Email should follow the Format  xxx@xxx.com",parent=self.root)
            return False 
        elif not re.match(pattern_date,self.emp_dob.get()):
            messagebox.showerror("Error","PLease Enter Valid Date of Birth",parent=self.root)
            return False 
        elif self.emp_dep.get()=="Select Department":
            messagebox.showerror("Error","Please Select the department",parent=self.root)          
            return False 
        elif not re.match(pattern,self.emp_designation.get()):
            messagebox.showerror("Error","PLease Enter Valid Designation",parent=self.root)
            return False
        elif self.facial_data.get() == "" or len(self.facial_data.get())>3:
            messagebox.showerror("Error", "Please select the facial data", parent=self.root)
            return False
        else:    
            try:
                upd = messagebox.askyesno("Update", "Do you want to update this data ? ",parent=self.root)
                if upd:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
                    cursor = conn.cursor()
                    cursor.execute("UPDATE employee SET First_Name=%s, Last_Name=%s, Contact=%s, Email=%s, Gender=%s, DOB=%s, Dep=%s, Des=%s, Facialdata=%s WHERE Employee_Id = %s", data + (self.id.get(),))
                    conn.commit()
                    cursor.close()  # Close cursor after use
                    conn.close()    # Close connection after use
                    self.view_data()
                    self.reset()
                    messagebox.showinfo("Success", "Details Updated Successfully",parent=self.root)
                else:
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)} data cannot be updated",parent=self.root)
                return False 
# To delete the employee
    def del_data(self):
        if self.id.get() == "" :
            messagebox.showerror("Missing Field", "No Employee Found! Select the Employee to be deleted.",parent=self.root)
            return False 
        else:
            try:
                delete_confirmation = messagebox.askyesno("Delete", "Do you want to delete this data?",parent=self.root)
                if delete_confirmation:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM employee WHERE Employee_Id = %s", (self.id.get(),))
                    conn.commit()
                    self.view_data()
                    self.reset()
                    conn.close()
                    messagebox.showinfo("Success", "Data Deleted Successfully",parent=self.root)
                if not delete_confirmation:
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)}, data cannot be deleted",parent=self.root)
                return False 
# To generate the dataset
    def dataset(self):
        data = (self.emp_first.get(), self.emp_last.get(), self.emp_contact.get(), self.emp_email.get(), self.emp_gender.get(),
        self.emp_dob.get(), self.emp_dep.get(), self.emp_designation.get(), self.facial_data.get(),)
        if any(value == "" for value in data):
            messagebox.showerror("Missing Field", "Please Enter All The Required Fields!", parent=self.root)
        elif self.facial_data.get()=="No":
            messagebox.showerror("Error","Please Select Yes to continue",parent=self.root)    
        else:
            try:
                # Establish database connection
                conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
                cursor = conn.cursor()
                # Insert employee details
                cursor.execute("SELECT Employee_Id FROM employee WHERE Employee_Id = %s", (self.id.get(),))
                id_data = cursor.fetchone()
                id_data=id_data[0]
                if id_data:
                    # If the employee ID exists, proceed with updating the record
                    cursor.execute("UPDATE employee SET First_Name=%s, Last_Name=%s, Contact=%s, Email=%s, Gender=%s, DOB=%s, Dep=%s, Des=%s, Facialdata=%s WHERE Employee_Id = %s",
                                (data + (id_data,)))  # Extract the ID from the tuple
                    conn.commit()
                    conn.close()
                else:
                    messagebox.showerror('Error',"Employee ID not found in the database.",parent=self.root)
                    return False 
                # Load frontal face cascade classifier
                face_classifier = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
                # Function to crop face from image
                def face_crop(img):
                    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped, (x, y, w, h)
                # Open webcam
                cap = cv2.VideoCapture(0)
                # Initialize image ID
                img_id = 0
                # Loop to capture images
                while True:
                    ret, frame = cap.read()
                    if face_crop(frame) is not None:
                        img_id += 1
                        face, (x, y, w, h) = face_crop(frame)
                        face = cv2.resize(face, (450, 450))
                        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = f"Dataset/employee.{id_data}.{img_id}.jpg"
                        cv2.imwrite(file_path, face_gray)
                        cv2.putText(frame, str(img_id), (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        if img_id>0 and img_id<=50:
                            cv2.putText(frame, '''Please look straight to the camera''', (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (69, 66, 245), 2)
                        elif img_id>50 and img_id<=100:
                            cv2.putText(frame, '''Please move your face ''', (150, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (69, 66, 245), 2)
                            cv2.putText(frame, '''towards left side slowly''', (150, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (69, 69, 245), 2)
                        elif img_id>100 and img_id<=150:
                            cv2.putText(frame, '''Please move your face ''', (100, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (69, 66, 245), 2)
                            cv2.putText(frame, '''towards right side slowly''', (150, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (69, 66, 245), 2)  
                        else:
                             cv2.putText(frame, '''Please move your face''', (150, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (69, 66, 245), 2)
                             cv2.putText(frame, '''upwards downwards slowly''', (150, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (69, 66, 245), 2)
                        cv2.imshow("Cropped face", frame)
                        if cv2.waitKey(1) == 13 or img_id == 200:
                            break
                # Release webcam and close windows
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed", parent=self.root)
                self.update()
                self.reset()
            except mysql.connector.Error as err:
                messagebox.showerror("MySQL Error", f"MySQL Error: {err}", parent=self.root)
                return False 
            except cv2.error as err:
                messagebox.showerror("OpenCV Error", f"OpenCV Error: {err}", parent=self.root)
                return False 
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)} dataset could not be generated", parent=self.root)
                return False         
if __name__ == "__main__":
    root = customtkinter.CTk()  # Create root window
    obj = Employee(root)  # Initialize your application
    root.mainloop()