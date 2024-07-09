import customtkinter
from tkinter import *
from tkinter import ttk, messagebox,Tk
import tkinter as tk
import mysql.connector
import tkinter
from PIL import Image,ImageTk
import re
import os
import csv
from tkinter import filedialog
from datetime import datetime
main_font = ('Century Gothic', 30)
font=('Century Gothic',20)
inner_font = ('Century Gothic', 12)
pattern_name = r'^[a-zA-Z]+$'
pattern_date=r'^\d{4}-\d{2}-\d{2}$'
pattern_time = r'^\d{2}:\d{2}:\d{2}$'
alldata=[]
filter_data=[]
class Logs():
# Constructor
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x650+180+40")
        self.root.title("Access Logs")
        root.wm_iconbitmap(r"face.ico")
        self.root.resizable(0,0)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root.configure(bg="gray10")
        self.id = customtkinter.StringVar()
        self.log_id = customtkinter.StringVar()
        self.facial_data = customtkinter.StringVar()
        self.switch_1 = customtkinter.StringVar()
        a = self.switch_1.get()
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
        self.label_employee = customtkinter.CTkLabel(self.left_frame,text="Edit Access Logs",font=font)
        self.label_employee.place(relx=0.5,rely=0.05,anchor= tkinter.CENTER)
        self.employee_entries = customtkinter.CTkFrame(self.left_frame,height=430,width=400,fg_color="transparent",border_width=2)
        self.employee_entries.place(x=30,y=50)
        self.logs_id_lbl = customtkinter.CTkLabel(self.employee_entries,text="Log Id :",font=('Century Gothic',12,"bold"))
        self.logs_id_lbl.place(x = 22 ,y = 25)
        self.logs_id= customtkinter.CTkEntry(self.employee_entries,state="readonly",font=inner_font,textvariable=self.log_id,width=50)
        self.logs_id.place(x=70,y=25)
        self.emp_id_lbl = customtkinter.CTkLabel(self.employee_entries,text="Employee Id :",font=('Century Gothic',12,"bold"))
        self.emp_id_lbl.place(x = 150 ,y = 25)
        self.emp_id= customtkinter.CTkEntry(self.employee_entries,state="readonly",font=inner_font,textvariable=self.id)
        self.emp_id.place(x=240,y=25)
        self.Name = customtkinter.CTkEntry(self.employee_entries,placeholder_text="Name",height=30,width=170,font=inner_font)
        self.Name.place(x=22,y=90)
        self.dep = customtkinter.CTkEntry(self.employee_entries,placeholder_text="Department",height=30,width=170,font=inner_font)
        self.dep.place(x=210,y=90)
        self.date=customtkinter.CTkEntry(self.employee_entries,placeholder_text="Date",height=30,width=170,font=inner_font)
        self.date.place(x=22,y=140)
        self.Time = customtkinter.CTkEntry(self.employee_entries,placeholder_text="Time",height=30,width=170,font=inner_font)
        self.Time.place(x=210,y=140)
        self.button_frame=customtkinter.CTkFrame(self.employee_entries,fg_color="transparent",width=360,height=100,border_width=2)
        self.button_frame.place(x=20,rely=0.5)
        self.update_btn = customtkinter.CTkButton(self.button_frame,text="Update",font=inner_font,width=160,cursor="hand2",command=self.update)
        self.update_btn.place(x=10,y=10)
        self.delete = customtkinter.CTkButton(self.button_frame,text="Delete",font=inner_font,width=160,cursor="hand2",command=self.del_data)
        self.delete.place(x=190,y=10)
        self.export_btn = customtkinter.CTkButton(self.button_frame,text="Export csv",font=inner_font,width=160,cursor="hand2",command=self.export_Csv,fg_color="green")
        self.export_btn.place(x=10,y=50)
        self.reset_btn = customtkinter.CTkButton(self.button_frame,text="Clear",font=inner_font,width=160,cursor="hand2",command=self.reset)
        self.reset_btn.place(x=190,y=50)
        self.right_frame =customtkinter.CTkFrame(self.top_frame,border_width=2,height=500,width=578,fg_color="transparent")
        self.right_frame.place(x= 770,rely=0.5,anchor=tkinter.CENTER)
        self.search_employee = customtkinter.CTkLabel(self.right_frame,text="Search Logs",font=font)
        self.search_employee.place(relx=0.5,rely=0.05,anchor= tkinter.CENTER)
        self.search_system=customtkinter.CTkFrame(self.right_frame,width=544,height=430,border_width=2,fg_color="transparent")
        self.search_system.place(x=15,y=50)
        self.search_frame=customtkinter.CTkFrame(self.search_system,width=530,height=60,border_width=2)
        self.search_frame.place(x=5,y=8)
        self.lbl_search=  customtkinter.CTkLabel(self.search_frame,text="Search By",font=('Century Gothic',14,"bold"))
        self.lbl_search.place(x=10,y=10)
        self.search_cmb=customtkinter.CTkComboBox(self.search_frame,font=inner_font,values=[" Log_id","Emp_id", "Name","Date","Time"])
        self.search_cmb.place(y=10,x=80)
        self.search_entry = customtkinter.CTkEntry(self.search_frame,font=inner_font,placeholder_text="Enter Value to Search")
        self.search_entry.place(y=10,x=230)
        self.search_btn=customtkinter.CTkButton(self.search_frame,text="Search",font=inner_font,width=60,cursor="hand2",command=self.search_by)
        self.search_btn.place(y=10,x=380)
        self.View_btn=customtkinter.CTkButton(self.search_frame,text="View All",font=inner_font,width=60,cursor="hand2",command=self.view_data)
        self.View_btn.place(y=10,x=450)
        self.tble = ttk.Treeview(self.search_system)
        self.tble.configure(yscrollcommand=self.tble.yview, xscrollcommand=self.tble.xview)
        self.tble["columns"] = ("Log_Id","Emp_Id", "Name", "Department", "Date", "Time") 
        self.tble.column("#0", width=0, stretch=tk.NO)  
        self.tble.column("Log_Id", width=0,anchor=tk.CENTER)  
        self.tble.column("Emp_Id", width=0,anchor=tk.CENTER)  
        self.tble.column("Name", width=20,anchor=tk.CENTER)  
        self.tble.column("Department", width=10,anchor=tk.CENTER)  
        self.tble.column("Date", width=30,anchor=tk.CENTER)  
        self.tble.column("Time", width=-5,anchor=tk.CENTER)      
        self.tble.heading("Log_Id", text="Log_Id")
        self.tble.heading("Emp_Id", text="Emp_Id")
        self.tble.heading("Name", text="Name")
        self.tble.heading("Department", text="Dep")
        self.tble.heading("Date", text="Date")
        self.tble.heading("Time", text="Time")
        self.tble.place(x=5, y=70, width=520, height=355)   
        self.scrollbar = customtkinter.CTkScrollbar(self.search_system, command=self.tble.yview,height=370)
        self.scrollbar.place(relx=0.97,rely=0.1)
        self.tble.bind("<ButtonRelease>",self.get_treeview_data)
        self.switch = customtkinter.CTkSwitch(self.main_frame,font=inner_font,text="Switch App Mode",command=self.change_color,variable=self.switch_1,onvalue="on",offvalue="off")
        self.switch.place(x=20,y=20)
        self.tble.configure(yscrollcommand=self.scrollbar.set)
        self.view_data()
# To search the accesslogs 
    def search_by(self):
        global alldata,filter_data
        try:
            self.tble.delete(*self.tble.get_children())
            conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM access_log WHERE " + self.search_cmb.get() + " = %s", (self.search_entry.get(),))
            rows = cursor.fetchall()
            alldata=rows
            filter_data=rows
            for i in rows:
                self.tble.insert('', 'end', values=i)
            conn.commit()
            conn.close() 
        except Exception as e:
            # Show a messagebox with the error message
            messagebox.showerror("Error", f"Due to {str(e)}, data could not be displayed",parent=self.root)
#   To change the appearance mode
    def change_color(self):
        val = self.switch_1.get()
        if val == "on" or val == "":
            customtkinter.set_appearance_mode("light")
            customtkinter.set_default_color_theme("dark-blue")
        else:
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("dark-blue")
# To view the data on front end
    def view_data(self):
        try:
            global alldata, filter_data
            self.tble.delete(*self.tble.get_children())
            conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM access_log")
            rows = cursor.fetchall()
            alldata = rows
            filter_data = rows 
            for i in rows:
                self.tble.insert('', 'end', values=i)
            conn.commit()
            conn.close() 
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {str(e)}",parent=self.root)                 
# To get the data present in tree view
    def get_treeview_data(self, event):
        focus = self.tble.focus()
        data_content = self.tble.item(focus)
        data_store = data_content["values"]
        self.log_id.set(data_store[0])
        self.id.set(data_store[1])
        self.Name.delete(0, 'end')
        self.Name.insert(0, data_store[2])
        self.dep.delete(0, 'end')
        self.dep.insert(0, data_store[3])
        self.date.delete(0, 'end')
        self.date.insert(0, data_store[4])
        self.Time.delete(0, 'end')
        self.Time.insert(0, data_store[5])
#reset fields to null
    def reset(self):
        self.Name.focus(),
        self.dep.focus(),
        self.date.focus(),
        self.Time.focus(),
        self.log_id.set(""),
        self.id.set(""),
        self.dep.delete(0,"end"),
        self.Name.delete(0,"end"),
        self.date.delete(0,"end"),
        self.Time.delete(0,"end"),
        self.top_frame.focus()
# To update the data
    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(Date) from access_log")
        date_check = cursor.fetchone()[0]
        conn.commit()
        cursor.close()  # Close cursor after use
        conn.close()
        
        if not re.match(pattern_date, self.date.get()):
            messagebox.showerror("Error", "Please Enter a valid date format", parent=self.root)
            return False
        
        try:
            date_check = datetime.strptime(date_check, "%Y-%m-%d")
            current = datetime.strptime(self.date.get(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date format is incorrect", parent=self.root)
            return False

        val_date = self.date.get()
        val_time = self.Time.get()

        data = (self.id.get(), self.Name.get(), self.dep.get(), self.date.get(), self.Time.get())
        deps = ["Computer Science", "Artificial Intelligence", "English", "Management", "Psychology", "Bio Sciences", "Mathematics"]

        # Validation checks
        if self.log_id.get() == "":
            messagebox.showerror("Missing Field", "No Employee Found! Select the Employee to be updated.", parent=self.root)
            return False
        elif any(value == "" for value in data):
            messagebox.showerror("Missing Field", "Please Enter All The Required Fields!", parent=self.root)
            return False
        elif not re.match(pattern_name, self.Name.get()):
            messagebox.showerror("Error", "Please Enter a valid name", parent=self.root)
            return False
        elif self.dep.get() not in deps:
            messagebox.showerror("Error", "Please Enter a valid Department", parent=self.root)
            return False
        elif not re.match(pattern_time, self.Time.get()):
            messagebox.showerror("Error", "Please Enter a valid time format", parent=self.root)
            return False

        try:
            correct_month = int(val_date[5:7])
            correct_day = int(val_date[8:])
            correct_hour = int(val_time[0:2])
            correct_min = int(val_time[3:5])
            correct_sec = int(val_time[6:])
        except ValueError:
            messagebox.showerror("Error", "Date or time contains invalid characters", parent=self.root)
            return False

        if correct_month < 1 or correct_month > 12:
            messagebox.showerror("Error", "Please Enter a valid month", parent=self.root)
            return False
        elif correct_day < 1 or correct_day > 31:
            messagebox.showerror("Error", "Please Enter a valid day", parent=self.root)
            return False
        elif correct_hour < 0 or correct_hour > 23:
            messagebox.showerror("Error", "Please Enter valid Hours", parent=self.root)
            return False
        elif correct_min < 0 or correct_min > 59:
            messagebox.showerror("Error", "Please Enter valid Minutes", parent=self.root)
            return False
        elif correct_sec < 0 or correct_sec > 59:
            messagebox.showerror("Error", "Please Enter valid Seconds", parent=self.root)
            return False
        elif current > date_check:
            messagebox.showerror("Error", "Date Cannot be exceeded from the Max Date", parent=self.root)
            return False

        # If all validations pass, proceed with the update
        try:
            upd = messagebox.askyesno("Update", "Do you want to update this data?", parent=self.root)
            if upd:
                conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
                cursor = conn.cursor()
                cursor.execute("UPDATE access_log SET Emp_id=%s, Name=%s, Dep=%s, Date=%s, Time=%s WHERE Log_id = %s", data + (self.log_id.get(),))
                conn.commit()
                cursor.close()  # Close cursor after use
                conn.close()    # Close connection after use
                self.view_data()
                self.reset()
                messagebox.showinfo("Success", "Details Updated Successfully", parent=self.root)
            else:
                return
        except Exception as e:
            messagebox.showerror("Error", f"Due to {str(e)} data cannot be updated", parent=self.root)
 # def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(Date) from access_log")
        date_check=cursor.fetchone()[0]
        conn.commit()
        cursor.close()  #Close cursor after use
        conn.close() 
        date_check =datetime.strptime(date_check, "%Y-%m-%d")
        current=datetime.strptime(self.date.get(), "%Y-%m-%d")       
        val_date=self.date.get()
        val_time=self.Time.get()
        correct_month = val_date[5:7]
        mon = val_date[5:7]
        mon =str(mon)
        correct_day =val_date[8:]
        correct_hour=val_time[0:2]
        correct_min=val_time[3:5]
        correct_sec=val_time[6:]
        correct_day=int(correct_day)
        correct_month=int(correct_month)
        correct_hour=int(correct_hour)
        correct_min=int(correct_min)
        correct_sec=int(correct_sec)
        data = (self.id.get(),self.Name.get(), self.dep.get(), self.date.get(), self.Time.get(),)
        deps=["Computer Science","Artificial Intelligence","English","Management","Psychology","Bio Sciences","Mathematics"]
        if self.log_id.get() == "" :
            messagebox.showerror("Missing Field", "No Employee Found! Select the Employee to be updatted.",parent=self.root)
            return False 
        elif any(value == "" for value in data):
            messagebox.showerror("Missing Field", "Please Enter All The Required Fields!",parent=self.root)
        elif not re.match(pattern_name,self.Name.get()):
            messagebox.showerror("Error","Please Enter a valid name",parent=self.root)     
        elif self.dep.get() not in deps:
            messagebox.showerror("Error","Please Enter a valid Department",parent=self.root)    
        
        elif not re.match(pattern_date,self.date.get()):
                messagebox.showerror("Error","Please Enter a valid date format",parent=self.root) 
        elif correct_month >=13 or type(correct_month):
            messagebox.showerror("Error","Please Enter a valid month",parent=self.root)   
        elif correct_day >=32:
            messagebox.showerror("Error","Please Enter a valid day",parent=self.root)
        elif correct_hour >=25:
            messagebox.showerror("Error","Please Enter valid Hours",parent=self.root)
        elif correct_min >=60:
            messagebox.showerror("Error","Please Enter valid Minutes",parent=self.root)
        elif correct_sec >=60:
            messagebox.showerror("Error","Please Enter valid Seconds",parent=self.root)
                
        elif not re.match(pattern_time,self.Time.get()):
            messagebox.showerror("Error","Please Enter a valid time format",parent=self.root) 
        elif current>date_check:
            messagebox.showerror("Error","Date Cannot be exceeded from the Max Date",parent=self.root)       
        else:    

            try:
                upd = messagebox.askyesno("Update", "Do you want to update this data ? ",parent=self.root)
                if upd:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
                    cursor = conn.cursor()
                    cursor.execute("UPDATE access_log SET Emp_id=%s,Name=%s, Dep=%s,Date=%s,Time=%s WHERE Log_id = %s", data + (self.log_id.get(),))
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
# Export csv
    def export_Csv(self):
        if len(alldata) < 1 and len(filter_data) < 1:
            messagebox.showerror("Error", "No data to export",parent=self.root)
            return False
        else:
            data_to_export = filter_data if len(filter_data) > 0 else alldata
            try:
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(('Csv file', '*.csv'), ('All Files', '*.*')))
                if fln:  # Check if the user selected a file
                    if not fln.endswith('.csv'):
                        fln += '.csv'
                    headings = ["Log_ID", 'Emp_ID', 'Name', 'Department', 'Date', 'Timestamp']    
                    try:
                        with open(fln, "w", newline='') as file:
                            exp_writer = csv.writer(file, delimiter=",")
                            exp_writer.writerow(headings)
                            for row in data_to_export:
                                exp_writer.writerow(row)
                            messagebox.showinfo("Success", "Your data has been exported to " + os.path.basename(fln) + " successfully.")
                    except PermissionError:
                        messagebox.showerror("Error", "The file is currently open and cannot be overwritten. Please close the file and try again.")
            except Exception as e:
                messagebox.showerror("Error", "An error occurred while exporting data: " + str(e))
# To delete data            
    def del_data(self):
        if self.log_id.get() == "" :
            messagebox.showerror("Missing Field", "No Employee Found! Select the Employee to be deleted.",parent=self.root)
            return False 
        elif self.logs_id.get()=="" or self.id.get()=="" or self.Name.get() == "" or self.dep.get() == "" or self.date.get() == "" or self.date.get() == "" or self.Time.get() == "":
            messagebox.showerror("Missing Field", "Please Enter All The Required Fields!",parent=self.root)
            
        else:
            
            try:
                delete_confirmation = messagebox.askyesno("Delete", "Do you want to delete this data?",parent=self.root)
                if delete_confirmation:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM access_log WHERE Log_id = %s", (self.log_id.get(),))
                    conn.commit()
                    
                    self.view_data()
                    self.reset()
                    conn.close()
                    messagebox.showinfo("Success", "Data Deleted Successfully",parent=self.root)
                if not delete_confirmation:
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)}, data cannot be deleted",parent=self.root)
if __name__ == "__main__":
    root = customtkinter.CTk()  # Create root window
    obj = Logs(root)  # Initialize your application
    root.mainloop()