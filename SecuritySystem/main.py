import customtkinter
import mysql.connector
import pyfirmata2
# from voice_gen import voice
from tkinter import *
# from controller import automate
from servo_control import control_servo
from Access_log import Logs
from Developers import deops
import time
import pyttsx3
import tkinter
import threading
import numpy as np
import cv2
from tkinter import ttk, messagebox, Tk
import os
from PIL import Image, ImageTk
from time import strftime,sleep
from datetime import datetime,timedelta
from employee import Employee
from Admin_settings import AdminSettings
from Forget_password import forget_password
import re
main_font = ('Century Gothic', 30)
font=('Century Gothic',20)
inner_font = ('Century Gothic', 12)
pattern_name = r'^[a-zA-Z]+$'
pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern_phone = r'^\d{4}-\d{7}$'
pattern_password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[\w@$!%*?&]{8,}$'
time=""
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)
def main():
    win =customtkinter.CTk()
    app=Main(win)
    win.mainloop()
class Main():
#   Constructor
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600+200+60")
        self.root.title("Main Screen")
        self.root.resizable(0,0)
        root.wm_iconbitmap(r"face.ico")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        self.switch_1 = customtkinter.StringVar()
        self.header_frame=customtkinter.CTkFrame(self.root,width=1000,height=600)
        self.header_frame.pack()
        self.switch = customtkinter.CTkSwitch(self.header_frame, font=inner_font, text="Switch App Mode", command=self.change_color,
                                              variable=self.switch_1, onvalue="on", offvalue="off")
        self.switch.place(x=20, y=20)
        self.head_label = customtkinter.CTkLabel(self.header_frame, text="Welcome To Smart Security System", font=main_font)
        self.head_label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
        self.main_frame = customtkinter.CTkFrame(self.header_frame, height=400, width=900, border_width=1, border_color="gray", fg_color="transparent")
        self.main_frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        self.emp_img = ImageTk.PhotoImage(Image.open(r"images\employee.png").resize((120, 100)))
        self.emp_button = customtkinter.CTkButton(self.main_frame, cursor="hand2", fg_color="transparent", image=self.emp_img, width=10, text="",command=self.Employees)
        self.emp_button.place(x=60, y=20)
        self.empbtn = customtkinter.CTkButton(self.main_frame, text="Employee Details", width=137, font=('Century Gothic', 12, "bold"), cursor="hand2", bg_color="transparent",command=self.Employees)
        self.empbtn.place(x=60, y=118)
        self.emp_img = ImageTk.PhotoImage(Image.open(r"images\access-control.png").resize((120, 100)))
        self.emp_button = customtkinter.CTkButton(self.main_frame, cursor="hand2", fg_color="transparent", image=self.emp_img, width=10, text="",command=self.Access_manager_thread)
        self.emp_button.place(x=280, y=20)
        self.empbtn = customtkinter.CTkButton(self.main_frame, text="Access Manager", width=137,command=self.Access_manager_thread, font=('Century Gothic', 12, "bold"), cursor="hand2", bg_color="transparent")
        self.empbtn.place(x=280, y=118)
        self.emp_img = ImageTk.PhotoImage(Image.open(r"images\file.png").resize((120, 100)))
        self.emp_button = customtkinter.CTkButton(self.main_frame, cursor="hand2", fg_color="transparent", image=self.emp_img, width=10, text="",command=self.access_logs)
        self.emp_button.place(x=500, y=20)
        self.empbtn = customtkinter.CTkButton(self.main_frame, width=137, text="Access Logs", font=('Century Gothic', 12, "bold"), cursor="hand2", bg_color="transparent",command=self.access_logs)
        self.empbtn.place(x=500, y=118)
        self.emp_img = ImageTk.PhotoImage(Image.open(r"images\server-control.png").resize((120, 100)))
        self.emp_button = customtkinter.CTkButton(self.main_frame, cursor="hand2", fg_color="transparent", image=self.emp_img, width=10, text="", command=self.load_dataset)
        self.emp_button.place(x=720, y=20)
        self.empbtn = customtkinter.CTkButton(self.main_frame, text="Data Set", width=137, font=('Century Gothic', 12, "bold"), cursor="hand2", bg_color="transparent", command=self.load_dataset)
        self.empbtn.place(x=720, y=118)
        self.emp_img = ImageTk.PhotoImage(Image.open(r"images\training.png").resize((120, 100)))
        self.emp_button = customtkinter.CTkButton(self.main_frame, cursor="hand2", fg_color="transparent", image=self.emp_img, width=10, text="", command=self.train_dataset)
        self.emp_button.place(x=60, y=230)
        self.empbtn = customtkinter.CTkButton(self.main_frame, text="Train Dataset", width=137, font=('Century Gothic', 12, "bold"), cursor="hand2", bg_color="transparent", command=self.train_dataset)
        self.empbtn.place(x=60, y=328)
        self.emp_img = ImageTk.PhotoImage(Image.open(r"images\settings.png").resize((120, 100)))
        self.emp_button = customtkinter.CTkButton(self.main_frame, cursor="hand2", fg_color="transparent", image=self.emp_img, width=10, text="", command=self.admin_settings)
        self.emp_button.place(x=280, y=230)
        self.empbtn = customtkinter.CTkButton(self.main_frame, text="Settings", width=137, font=('Century Gothic', 12, "bold"), cursor="hand2", bg_color="transparent", command=self.admin_settings)
        self.empbtn.place(x=280, y=328)
        self.emp_img = ImageTk.PhotoImage(Image.open(r"images\programmer.png").resize((120, 100)))
        self.emp_button = customtkinter.CTkButton(self.main_frame, cursor="hand2", fg_color="transparent", image=self.emp_img, width=10, text="",command=self.devops)
        self.emp_button.place(x=500, y=230)
        self.empbtn = customtkinter.CTkButton(self.main_frame, text="Developers", width=137, font=('Century Gothic', 12, "bold"), cursor="hand2", bg_color="transparent",command=self.devops)
        self.empbtn.place(x=500, y=328)
        self.emp_img = ImageTk.PhotoImage(Image.open(r"images\logout.png").resize((120, 100)))
        self.emp_button = customtkinter.CTkButton(self.main_frame, cursor="hand2", fg_color="transparent", image=self.emp_img, width=10, text="",command=self.logout)
        self.emp_button.place(x=720, y=230)
        self.empbtn = customtkinter.CTkButton(self.main_frame, text="Logout", width=137, font=('Century Gothic', 12, "bold"), cursor="hand2", bg_color="transparent",command=self.logout)
        self.empbtn.place(x=720, y=328)
# Thread to rotate the servo
    def rotate(self):
        rotate_thread = threading.Thread(target=self.rotate_servo)
        rotate_thread.start() 
# Thread to generate voice
    def voice_gen(self):
        voices = threading.Thread(target=self.voice)  
        voices.start()
        sleep(2)
# To generate the voice
    def voice():   
        engine.say("Door is being unlocked for 10 seconds")
        engine.runAndWait()
# To rotate the servo 
    def rotate_servo(self):
        control_servo(40)
        control_servo(0)
# To open admin settings           
    def admin_settings(self):
        newwin = Toplevel(self.root)
        app = AdminSettings(newwin)
        newwin.focus_set()  # Set focus to the new window
# To open developers page
    def devops(self):
        newwin = Toplevel(self.root)
        app = deops(newwin)
        newwin.focus_set()  # Set focus to the new window
# To open access log page
    def access_logs(self):
        newwin = Toplevel(self.root)
        app = Logs(newwin)
        newwin.focus_set()  # Set focus to the new window
# To open Employee page
    def Employees(self):
        newwin = Toplevel(self.root)
        app = Employee(newwin)
        newwin.focus_set()  # Set focus to the new window
# To return to login page
    def logout(self):
        self.root.withdraw()
        newwin = Toplevel(self.root)
        app = login(newwin)
        newwin.focus_set()  # Set focus to the new window
# To change the appearance mode
    def change_color(self):
        val = self.switch_1.get()
        if val == "on" or val == "":
            customtkinter.set_appearance_mode("system")
            customtkinter.set_default_color_theme("green")
        else:
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("green")
# To load the dataset
    def load_dataset(self):
        folder_path = r"Dataset"
        os.startfile(folder_path)
# To train the dataset
    def train_dataset(self):
        data_dir = r"Dataset"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for img_path in path:
            image = Image.open(img_path).convert("L")
            image_np = np.array(image, 'uint8')
            id = int(os.path.split(img_path)[-1].split(".")[1]) 
            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training data", image_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids) 
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed",parent=self.root)
# Thread for access manager    
    def Access_manager_thread(self):
        # Start a new thread for the Access_manager function
        access_thread = threading.Thread(target=self.Access_manager)
        access_thread.start()    
# Log access to csv
    def attendance(self, emp_id, f_name, Dep):
        with open(r"Attendance.csv", "r+", newline="\n") as f:
            my_data = f.readlines()
            name_list = []
            for line in my_data:
                entry = line.split(",")
                name_list.append(entry[0])
            now = datetime.now()
            date = now.strftime("%Y/%m/%d")
            current_time = now.strftime("%H:%M:%S")
            if str(emp_id) not in name_list:
                f.writelines(f"\n{emp_id},{f_name},{Dep},{date},{current_time}")
                self.voice_gen()
                self.rotate()
            elif str(emp_id) in name_list:
                last_log_date = None
                last_log_time = None
                for line in my_data:
                    entry = line.split(",")
                    if entry[0] == str(emp_id):
                        last_log_date = entry[-2].strip()  # Extract the last log date for this employee
                        last_log_time = entry[-1].strip()  # Extract the last log time for this employee
                if last_log_date == date:
                    last_log_datetime = datetime.strptime(last_log_date + " " + last_log_time, "%Y/%m/%d %H:%M:%S")
                    time_difference = now - last_log_datetime
                    # Convert time difference to minutes
                    minutes_difference = time_difference.total_seconds() / 60
                    if minutes_difference >= 1:
                        self.voice_gen()
                        self.rotate()  
                        # Checking if more than 1 minute has passed since the last entry on the same date
                        f.writelines(f"\n{emp_id},{f_name},{Dep},{date},{current_time}")
                    else:
                        pass
                else:
                    f.writelines(f"\n{emp_id},{f_name},{Dep},{date},{current_time}")
                    self.voice_gen()
                    self.rotate()
# Thread to generate voice
    def voice(self):
        voice_thread=threading.Thread(target=self.run_voice)
        voice_thread.start()
# To run the voice                    
    def run_voice(self):  
        engine = pyttsx3.init()
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        text ="Door is being unlocked for ten seconds."
        engine.say(text)
        engine.runAndWait()
# To store Access
    def store_Access(self, emp_id, f_name, Dep):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(Date), MAX(Time) FROM access_log WHERE Emp_id = %s", (emp_id,))
        last_entry = cursor.fetchone()
        last_date = last_entry[0]
        last_time = last_entry[1]
        if last_date is not None and last_time is not None:
            last_date = datetime.strptime(last_date, "%Y-%m-%d").date()
            if str(last_date) == date:
                last_log_datetime = datetime.combine(last_date, datetime.strptime(last_time, "%H:%M:%S").time())
                time_difference = now - last_log_datetime
                # Convert time difference to minutes
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference >= 1.0:
                    cursor.execute("INSERT INTO access_log (Emp_id, Name, Dep, Date, Time) VALUES (%s, %s, %s, %s, %s)",
                                (emp_id, f_name, Dep, date, time))
                    conn.commit()
                    self.rotate()
                else:
                    pass
            else:
                cursor.execute("INSERT INTO access_log (Emp_id, Name, Dep, Date, Time) VALUES (%s, %s, %s, %s, %s)",
                            (emp_id, f_name, Dep, date, time))
                conn.commit()
                self.rotate()
        else:
            cursor.execute("INSERT INTO access_log (Emp_id, Name, Dep, Date, Time) VALUES (%s, %s, %s, %s, %s)",
                        (emp_id, f_name, Dep, date, time))
            conn.commit()
            self.rotate()               
# To manage the access  
    def Access_manager(self):
        def draw(img, face_classifier, scale_factor, min_neighbour, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = face_classifier.detectMultiScale(gray_img, scale_factor, min_neighbour)
            coord = []
            for x, y, h, w in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="@fyp2020", database="design")
                cursor = conn.cursor()
                cursor.execute("SELECT First_Name FROM employee WHERE Employee_id = %s", (id,))
                f_name = cursor.fetchone()
                if f_name is not None:
                    
                    f_name = f_name[0]
                    cursor.execute("SELECT Employee_id FROM employee WHERE Employee_id = %s", (id,))
                    emp_id = cursor.fetchone()
                    emp_id = emp_id[0]
                    cursor.execute("SELECT Dep FROM employee WHERE Employee_id = %s", (id,))
                    Dep = cursor.fetchone()
                    Dep = Dep[0]
                if f_name and emp_id and Dep:
                    if confidence > 80:
                        cv2.putText(img, f"Name: {f_name}", (x, y-75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Employee id: {emp_id}", (x, y-45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {Dep}", (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                        self.attendance(emp_id,f_name,Dep)
                        self.store_Access(emp_id,f_name,Dep)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, f"Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord
        def recognize(img, clf, face_cascade):
            coord = draw(img, face_cascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        # clf = cv2.face.LBPHFaceRecognizer()
        clf.read("Classifier.xml")
        # vid ="http://192.168.18.6:8080/video"
        video_cap = cv2.VideoCapture(0)
        # video_cap.open(vid)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, face_cascade)
            cv2.imshow("Welcome to Access Manager", img)
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
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
class register():
    #costructor
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
        newwin = Toplevel()
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
 # Registration of an admin
    def reg_admin(self):
        if self.f_name.get() =="" or self.l_name.get()=="" or self.contact.get()=="" or self.email.get()=="" or self.ques.get()=="" or self.ans.get()=="" or self.password.get()=="" or self. confirm_password.get()=="":
            messagebox.showerror("Error" ,"All Fields are required !", parent=self.root)
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
if __name__ == "__main__":
    main()   
