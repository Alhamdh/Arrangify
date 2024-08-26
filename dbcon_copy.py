from tkinter import *
from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Treeview
import pandas as pd
import psycopg2
# from psycopg2.extensions import register_adapter, AsIs


root = Tk()
root.geometry("1280x720")
root.title("Arrangify")

con = psycopg2.connect(
     database="arrangify",
     user="postgres",
     password="password",
     host="localhost",
     port='5432'
)

# function to change properties of button on hover
def changeOnHover(button, imgOnHover, imgOnLeave):
 
    # adjusting background of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        image=imgOnHover,
        width = 240,
        height = 270
    ))
 
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        image=imgOnLeave,
        width = 220,
        height = 250
    ))

def EntryHover(entry):
    entry.bind("<Button-1>",func=lambda e: entry.config(
        background = "#214810"
    ))
    # entry.bind("<Leave>", func = lambda e: entry.config(
    #     background = "#ffffff"
    # ))

class loginScreen(Frame):

    def __init__(self):
        super().__init__()
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alham\Downloads\navi\navi\assets\login")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def toggle_password_visibility():
            # self.show_password
            if self.show_password:
                self.entry_1.config(show='')
                self.show_password = False
                show_hide_button.config(image=pw_button_img2)
            else:
                self.entry_1.config(show='*')
                self.show_password = True
                show_hide_button.config(image=pw_button_img1)
        
        def home_page():
            pw = self.entry_1.get()
            if pw == "nnn":
                home()
                loginScreen.destroy(self)
            else:
                self.pw_lbl.place(x=663,y=321)
        
        self.canvas = Canvas(
            # self,
            bg="#2148C0",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.pw_lbl = Label(
            text="Wrong Passwword",
            fg = "#ff758c",
            bg="#2148C0",
            font=("Lato Regular", 15 * -1)
        )

        # Load and display the image
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(500.0, 542.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            619.0,
            333.0,
            image=self.image_image_2
        )

        # Create text labels
        self.canvas.create_text(490.0, 320.0, anchor="nw", text="PASSWORD", fill="#FFFFFF", font=("Montserrat Light", 14))
        self.canvas.create_text(485.0, 211.0, anchor="nw", text="WELCOME TO", fill="#FFFFFF", font=("Inter", 20))
        self.canvas.create_text(490.0, 246.0, anchor="nw", text="ARRANGIFY", fill="#FFFFFF", font=("Inter", 48))

        # Create entry widget for password
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(640.0, 367.5, image=self.entry_image_1)
        self.entry_1 = Entry(
            # self,
            # image = entry_bg_1,
            show='*',
            bd=0,
            bg="#2148C0",
            fg="#ffffff",
            insertbackground='#ffffff',  # cursor color
            highlightthickness=0
        )
        self.entry_1.place(x=494.0, y=348.0, width=292.0, height=42.0)

        # Create button to show/hide password
        # pw_button_img1 = PhotoImage(file="hide_pw.png")
        self.show_password = True # Flag to track password visibility
        pw_button_img1 = PhotoImage(file=relative_to_assets("show_pw.png"))
        pw_button_img1 = pw_button_img1.subsample(15)
        pw_button_img2 = PhotoImage(file=relative_to_assets("hide_pw.png"))
        pw_button_img2 = pw_button_img2.subsample(15)
        # pw_button_img1.subsample(10)
        show_hide_button = Button(
            # text="Show Password",
            image=pw_button_img1,
            font=("Montserrat regular", 12),
            command=toggle_password_visibility,
            bg="#2148C0",
            fg="#ffffff",
            relief="flat"
        )
        show_hide_button.place(x=743, y=353, width=40, height=30)

        # Create other buttons
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            # self,
            image=self.button_image_1,
            # text="Login",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: home_page(),
            relief="flat",
            # bg="#ffffff"
        )
        # button_1.configure(image = button_image_1)
        self.button_1.place(x=490.0, y=423.0, width=300.0, height=45.0)

        button_2 = Button(
            text="FORGOT PASSWORD?",
            font=("Montserrat regular", 14),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            bg="#2148C0",
            fg="#ffffff",
            relief="flat"
        )
        button_2.place(x=590.0, y=479.0, width=220.0, height=20.0)


class home(Frame):
    
    def __init__(self):
        super().__init__()
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alham\Downloads\navi\navi\assets\home")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def goto_page(frame):
            frame()
            home.destroy(self)

        self.canvas = Canvas(
            bg = "#2148C0",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_image_1_hover = PhotoImage(
            file=relative_to_assets("button_1_hover.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goto_page(manage_room),
            relief="flat"
        )
        self.button_1.place(
            x=260.0,
            y=234.0,
            width=220.0,
            height=250.0
        )
        changeOnHover(self.button_1,self.button_image_1_hover,self.button_image_1)
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_image_2_hover = PhotoImage(
            file=relative_to_assets("button_2_hover.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goto_page(arrange),
            relief="flat"
        )
        changeOnHover(self.button_2,self.button_image_2_hover,self.button_image_2)
        self.button_2.place(
            x=530.0,
            y=234.0,
            width=220.0,
            height=250.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_image_3_hover = PhotoImage(
            file=relative_to_assets("button_3_hover.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goto_page(view_seats),
            relief="flat"
        )
        changeOnHover(self.button_3,self.button_image_3_hover,self.button_image_3)
        self.button_3.place(
            x=800.0,
            y=234.0,
            width=220.0,
            height=250.0
        )
        # Load and display the image
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(500.0, 542.0, image=self.image_image_1)

        # self.image_image_2 = PhotoImage(
        #     file=relative_to_assets("image_2.png"))
        # self.image_2 = self.canvas.create_image(
        #     619.0,
        #     333.0,
        #     image=self.image_image_2
        # )
        # self.button_3.bind("<Enter>", func = lambda e: self.button_3.place(
        #     x=800.0,
        #     y=234.0,
        #     width=240.0,
        #     height=260.0
        # ))
        # login.destroy(self)


class manage_room(Frame):
    def __init__(self):
        super().__init__()
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alham\Downloads\navi\navi\assets\room")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            bg = "#2148C0",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        cursor_obj2 = con.cursor()

        self.rc_lbl = Label(text="Room Code",font=("Lato Regular", 18 * -1),width=10,height=1,bg = "#E4FCFF",fg="#58585A",justify=LEFT)
        self.cap_lbl = Label(text="Capacity",font=("Lato Regular", 18 * -1),width=10,height=1,bg = "#E4FCFF",fg="#58585A",justify=LEFT,anchor = 'w')
        self.pri_lbl = Label(text="Priority",font=("Lato Regular", 18 * -1),width=10,height=1,bg = "#E4FCFF",fg="#58585A",justify=LEFT,anchor=W)
        self.empty_lbl = Label(text="EMPTY FIELDS!",font=("Lato Regular", 10 * -1),width=20,height=1,bg = "#E4FCFF",fg="red",anchor=W)

        def goto_page(frame):
            frame()
            manage_room.destroy(self)
                

        def add_room():
            refresh()
            self.entry_1.config(state="normal")
            self.entry_2.delete(0,'end')
            self.entry_1.delete(0,'end')
            self.entry_3.delete(0,'end')
            self.rc_lbl.place(x=153,y=325)
            self.entry_1.place(x=153,y=355,width=315,height=36)
            self.cap_lbl.place(x=153,y=418)
            self.entry_2.place(x=153,y=448,width=315,height=36)
            self.pri_lbl.place(x=153,y=511)
            self.entry_3.place(x=153,y=541,width=315,height=36)
            self.button_3.place(
                x=346.0,
                y=239.0,
                # width=150.0,
                # height=42.0
            )

        #function for refresh
        def refresh():
            for lbl in self.data_lbl:
                lbl.grid_forget()
            for btn in self.del_btn:
                btn.grid_forget()
            for btn in self.edit_btn:
                btn.grid_forget()

            self.data_lbl = []
            self.del_btn = []
            self.edit_btn = []
            cursor_obj2.execute("select * from rooms ORDER BY priority")
            # print(cursor_obj2)
            self.entry_1.config(state=NORMAL)
            self.entry_1.place_forget()
            self.entry_2.place_forget()
            self.entry_3.place_forget()
            self.rc_lbl.place_forget()
            self.cap_lbl.place_forget()
            self.pri_lbl.place_forget()
            self.edit_done_btn.place_forget()
            self.e = Label(box,width=20,text="Room Code",background="#ffffff",anchor=CENTER)
            self.e.grid(row=0,column=0)
            self.e = Label(box,width=20,text="Capacity",background="#ffffff",anchor=CENTER)
            self.e.grid(row=0,column=1)
            self.e = Label(box,width=20,text="Priority",background="#ffffff",anchor=CENTER)
            self.e.grid(row=0,column=2)
            i=1
            for room in cursor_obj2:
                del_btn = Button(
                    box,
                    text="Del",
                    bg="#000000",
                    fg = "#ffffff"
                )
                edit_btn = Button(
                    box,
                    text = "Edit",
                    bg = "#000000",
                    fg = "#ffffff"   
                )
                for col, data in enumerate(room):
                    data_lbl = Label(box,width=20,text=data,background="#ffffff",anchor=CENTER)
                    data_lbl.grid(row=i,column=col)
                    self.data_lbl.append(data_lbl)

                del_btn.config(command=lambda btn=del_btn, room_id=room[0]: delete_room(btn, room_id))
                edit_btn.config(command=lambda btn = edit_btn, room_id = room[0]: edit_room(btn,room_id))
                del_btn.grid(row=i, column=len(room))
                self.del_btn.append(del_btn)
                edit_btn.grid(row=i,column= len(room)+1)
                self.edit_btn.append(edit_btn)
                i=i+1
        
        def add_done():
            rc = self.entry_1.get()
            cap = self.entry_2.get()
            pri = self.entry_3.get()
            if rc=="" or cap == "" or pri=="":
                self.empty_lbl.place(x=153,y=300)
                print(rc,cap,pri)
            else:
                cursor_obj = con.cursor()
                cursor_obj.execute("INSERT INTO rooms(roomcode, capacity, priority) VALUES (%s, %s, %s)", (rc, cap, pri))
                con.commit()
                self.rc_lbl.place_forget()
                self.cap_lbl.place_forget()
                self.pri_lbl.place_forget()
                self.entry_1.place_forget()
                self.entry_2.place_forget()
                self.entry_3.place_forget()
                self.empty_lbl.place_forget()
                self.button_3.place_forget()
            refresh()

        # Function to delete a room from the database
        def delete_room(button, room_id):
            cursor_obj3 = con.cursor()
            cursor_obj3.execute("DELETE FROM rooms WHERE roomcode = %s", (room_id,))
            con.commit()
            cursor_obj3.close()
            # Remove the corresponding row and button from the UI
            button.grid_forget()
            # lbl.grid_forget()
            refresh()
        
        def edit_room(button,room_id):
            refresh()
            cursor_obj = con.cursor()
            self.entry_1.config(state="normal")
            self.entry_2.delete(0,'end')
            self.entry_1.delete(0,'end')
            self.entry_3.delete(0,'end')
            self.rc_lbl.place(x=153,y=325)
            self.entry_1.place(x=153,y=355,width=315,height=36)
            self.entry_1.insert(END,room_id)
            self.entry_1.config(state="readonly")
            self.cap_lbl.place(x=153,y=418)
            self.entry_2.place(x=153,y=448,width=315,height=36)
            cursor_obj.execute("SELECT capacity from rooms where roomcode = %s",(room_id,))
            con.commit()
            cap = cursor_obj.fetchall()
            self.entry_2.insert(END,cap[0])
            self.pri_lbl.place(x=153,y=511)
            self.entry_3.place(x=153,y=541,width=315,height=36)
            cursor_obj.execute("SELECT priority from rooms where roomcode = %s",(room_id,))
            con.commit()
            pri = cursor_obj.fetchall()
            self.entry_3.insert(END,pri[0])
            self.button_3.place_forget()
            self.edit_done_btn.place(x=346,y=239)
            cursor_obj.close()

        def edit_done():
            self.entry_1.config(state="normal")
            cursor_obj = con.cursor()
            rc = self.entry_1.get()
            cap = self.entry_2.get()
            pri = self.entry_3.get()
            if cap=="" and pri == "":
                self.empty_lbl.place(x=153,y=300)
            elif cap != '' and pri == '':
                cursor_obj.execute("update rooms set capacity = %s where roomcode = %s",(cap,rc))
            elif cap == '' and pri != '':
                cursor_obj.execute("update rooms set priority = %s where roomcode = %s",(pri,rc))
            else:
                cursor_obj.execute("update rooms set priority = %s,capacity = %s where roomcode = %s",(pri,cap,rc))
            refresh()

        # s = Scrollbar(root)
        # s.pack(side=RIGHT,fill=Y)
        box = LabelFrame(
            root,
            height=200,
            bg="#ffffff",
            # xscrollcommand = s.set
        )
        #scrollbar
        box.place(x=570,y=130)
        # refresh()
        # s.config(command=box.yview)

        cursor_obj2 = con.cursor()
        print(cursor_obj2)
        cursor_obj2.execute("select * from rooms ORDER BY priority")
        # print(cursor_obj2)

        self.e = Label(box,width=20,text="Room Code",background="#ffffff",anchor=CENTER)
        self.e.grid(row=0,column=0)
        self.e = Label(box,width=20,text="Capacity",background="#ffffff",anchor=CENTER)
        self.e.grid(row=0,column=1)
        self.e = Label(box,width=20,text="Priority",background="#ffffff",anchor=CENTER)
        self.e.grid(row=0,column=2)
        i=1
        self.del_btn=[]
        self.data_lbl=[]
        self.edit_btn=[]
        for room in cursor_obj2:
            del_btn = Button(
                box,
                text="Del",
                bg="#000000",
                fg = "#ffffff",
                width=5
            )
            edit_btn = Button(
                box,
                text = "Edit",
                bg = "#000000",
                fg = "#ffffff",
                width=5
            )
            for col, data in enumerate(room):
                data_lbl = Label(box,width=20,text=data,background="#ffffff",anchor=CENTER)
                data_lbl.grid(row=i,column=col)
                self.data_lbl.append(data_lbl)
                del_btn.config(command=lambda btn=del_btn, room_id=room[0]: delete_room(btn, room_id))
                edit_btn.config(command=lambda btn = edit_btn, room_id = room[0]: edit_room(btn,room_id))

            # del_btn.config(command=lambda btn=del_btn, room_id=room[0],lbl=data_lbl: delete_room(btn, room_id,lbl))
            # del_btn.grid(row=i, column=len(room))
            # self.del_btn.append(del_btn)
            del_btn.grid(row=i,column = len(room))
            self.del_btn.append(del_btn)
            edit_btn.grid(row=i,column= len(room)+1)
            self.edit_btn.append(edit_btn)
            i=i+1
        # cursor_obj2.close()


        #Buttons
        self.back_button_image = PhotoImage(
            file=relative_to_assets("back_button.png"))
        self.back_button_image = self.back_button_image.subsample(2)
        self.back_button = Button(
            image = self.back_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goto_page(home),
            relief = FLAT
        )
        self.back_button.place(x=10,y=10)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            1142.0,
            541.0,
            image=self.image_image_1
        )
        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            818.0,
            359.0,
            image=self.image_image_2
        )


        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            323.0,
            359.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            143.0,
            134.0,
            anchor="nw",
            text="Manage Rooms",
            fill="#264EC9",
            font=("Lato Regular", 40 * -1)
        )

        self.canvas.create_rectangle(
            150.0,
            203.00000035671775,
            496.0,
            204.00003051757812,
            fill="#264EC9",
            outline=""
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: add_room(),
            relief="flat"
        )
        self.button_1.place(
            x=151.0,
            y=239.0,
            width=150.0,
            height=42.0
        )

        self.entry_1 = Entry(
            bd=0,
            bg="#ffffff",
            fg="#58585A",
            insertbackground='#58585A',
            # insertbackground='#ffffff',  # cursor color
            highlightthickness=0,
            font=("lato", 14)
        )
        # entry_1.place(x=1000,y=355,width=315,height=36)

        self.entry_2 = Entry(
            bd=0,
            bg="#ffffff",
            fg="#58585A",
            insertbackground='#58585A',
            # insertbackground='#ffffff',  # cursor color
            highlightthickness=0,
            font=("lato", 14)
        )

        self.entry_3 = Entry(
            bd=0,
            bg="#ffffff",
            fg="#58585A",
            insertbackground='#58585A',
            highlightthickness=0,
            font=("lato", 14)
        )

        self.done_image = PhotoImage(
            file=relative_to_assets("done_btn.png"))
        self.button_3= Button(
            image=self.done_image,
            highlightthickness=0,
            borderwidth=0,
            fg = "#ffffff",
            bg = "#000000",
            command=lambda: add_done()
        )

        self.edit_done_btn = Button(
            image=self.done_image,
            bg = "#58585A",
            fg = "#000000",
            highlightthickness=0,
            borderwidth=0,
            command=lambda: edit_done()
        )

class arrange(Frame):
    def __init__(self):
        super().__init__()


        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alham\Downloads\navi\navi\assets\arrange")
        
        self.file_path = ""
        self.date_ses = []
        # self.subs = []
        # self.sub_count = []
        # self.room_cap = []

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        def goto_page(frame):
            frame()
            arrange.destroy(self)
        
        def clear_files():
            self.session_table.place_forget()
            cursor_obj1 = con.cursor()
            cursor_obj1.execute("DELETE FROM all_fields")
            # cursor_obj1.execute("DELETE FROM seats")
            con.commit()
            cursor_obj1.close()
            # self.file_entry.config(text="")
            # self.file_entry.insert(END,"")
            self.file_entry.delete(0,END)

        def clear_seats():
            self.session_table.place_forget()
            cursor_obj1 = con.cursor()
            cursor_obj1.execute("DELETE FROM seats")
            con.commit()
            cursor_obj1.close()
            
        def choose_button():
            refresh()
            f_path = askopenfilename(initialdir=r"C:\Users\alham\Downloads",
            title="Select File", filetypes=(("Excel Files","*.xlsx*"),("All Files","*.*"),("Excel Files","*.xls*")))
            self.file_chosen_lbl.place(x = 570,y = 270)
            self.file_entry.place(x=570,y=300,width=500,height=35)
            if(f_path==''):
                self.file_entry.delete(0,END)
                self.file_entry.insert(END,"No file Chosen")
            else:
                self.file_entry.delete(0,END)
                self.file_entry.insert(END,f_path)
                self.file_path = f_path
        
        def read_file(f_path):
            if f_path != '':
                self.df1 = pd.read_excel(f_path,header=None)
                # self.df2 = self.df1[[0,1,2,5,6,8]].head(5)
                # print(self.df2.to_string(index=False,header=False))
                self.df2 = self.df1[[0,1,2,5,6,8,4]]
                cursor_obj = con.cursor()
                for i in self.df2.index:
                    values = tuple(self.df2.loc[i, [0, 1, 2, 5, 6, 8, 4]].values)
                    if pd.isnull(values[4]):
                        continue  # Skip inserting rows with NaT values
                    values = list(values)
                    if values[4] == 'Exam Date':
                        continue
                    # date_str = str(values[4])  # Convert date value to string
                    values[4] = pd.to_datetime(values[4],format='%d-%m-%Y')
                    # values[4] = pd.to_datetime(values[4])
                    values = tuple(values)
                    cursor_obj.execute("INSERT INTO all_fields(name,ktu_id,dept,subject,date,session,slot) VALUES (%s, %s, %s, %s, %s, %s, %s)", values)
                    con.commit()
                cursor_obj.close()

        def view_session():
            refresh()
            self.session_table.delete(*self.session_table.get_children()) #Clearing The table
            cursor_obj = con.cursor()
            cursor_obj.execute("select distinct date,session from all_fields order by date desc")
            con.commit()
            # value = []
            for ses in cursor_obj:
                value = []
                for data in ses:
                    value.append(data)
                self.session_table.insert(parent='',index=0,values = value)
            self.f.place(
                x=620,
                y=200,
                # height=330
            )
        
        def select_rec(e):
            self.date_ses = []
            selected = self.session_table.focus()
            values = self.session_table.item(selected,'values')
            # print(values[0])
            self.date_ses = values
            print(self.date_ses)


        def arrange_seats(self):
            cursor = con.cursor()
            cursor.execute("SELECT roomcode, capacity FROM rooms ORDER BY priority")
            con.commit()
            rooms = cursor.fetchall()
            assigned_ktu_ids = set()
            assigned_sub = set()
            sub_list = list()
            room = {}

            for r,c in rooms:
                room[r]=False

            for roomcode, capacity in rooms:
                seat_numbers = []
                rem_cap = capacity

                cursor.execute("SELECT subject FROM all_fields WHERE date = %s AND session = %s GROUP BY subject ORDER BY COUNT(*) DESC", self.date_ses)
                # con.commit()
                subjects = cursor.fetchall()

                for sub_num, sub in enumerate(subjects):
                    if sub not in assigned_sub:
                        cursor.execute("SELECT ktu_id FROM all_fields WHERE subject = %s AND date = %s AND session = %s", (sub, self.date_ses[0], self.date_ses[1]))
                        # con.commit()
                        students = cursor.fetchall()
                        sub_list.append([stu[0] for stu in students])
                        assigned_sub.add(sub)

                i=0
                sublist1 = sub_list[0]
                if 1<len(sub_list):
                    sublist2 = sub_list[1]
                    i=i+1
                else:
                    sublist2 = []
                while i < len(sub_list):
                    for student1, student2 in zip(sublist1, sublist2):
                        if rem_cap <= 0:
                            room[roomcode]=True
                            break
                        if student1 not in assigned_ktu_ids:
                            seat_numbers.append(student1)
                            rem_cap -= 1
                            assigned_ktu_ids.add(student1)
                        if rem_cap <= 0:
                            room[roomcode]=True
                            break
                        if student2 not in assigned_ktu_ids:
                            seat_numbers.append(student2)
                            rem_cap -= 1
                            assigned_ktu_ids.add(student2)
                    if len(sublist1) > len(sublist2):
                        i=i+1
                        sublist1 = sublist1[len(sublist2):]
                        if i < len(sub_list):
                            sublist2 = sub_list[i]
                        else:
                            sublist2 = []
                    elif len(sublist2) > len(sublist1):
                        i=i+1
                        sublist2 = sublist2[len(sublist1):]
                        if i<len(sub_list):
                            sublist1 = sub_list[i]
                        else:
                            sublist1=[]
                if not room[roomcode]:
                    for n,sub in enumerate(subjects):
                        cursor.execute("SELECT ktu_id FROM all_fields WHERE subject = %s AND date = %s AND session = %s", (sub, self.date_ses[0], self.date_ses[1]))
                        con.commit()
                        students = cursor.fetchall()
                        for stu in students:
                            if rem_cap <= 0:
                                room[roomcode]=True
                                break
                            if stu[0] not in assigned_ktu_ids:
                                seat_numbers.append(stu[0])
                                assigned_ktu_ids.add(stu[0])
                                rem_cap-=1

                for x,s_id in enumerate(seat_numbers):
                # x,s_id = enumerate(seat_numbers)
                    print("Room:", roomcode, ":", x+1,s_id)
                    cursor.execute("INSERT into seats values(%s,%s,%s,%s,%s)",(s_id,x+1,roomcode,self.date_ses[0],self.date_ses[1]))

        def refresh():
            self.file_entry.place_forget()
            self.file_chosen_lbl.place_forget()
            self.f.place_forget()

        self.canvas = Canvas(
            bg = "#2148C0",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(
            500.0,
            541.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            640.0,
            359.0,
            image=self.image_image_2
        )

        self.file_chosen_lbl = Label(
            text="File Chosen",
            bg = "#E4FCFF",
            # bg= "#ffffff",
            fg = "#484646",
            font=("Lato Regular", 18 * -1)
        )

        self.file_entry = Entry(
            bd=3,
            bg="#ffffff",
            fg="#58585A",
            insertbackground='#58585A',
            # insertbackground='#ffffff',  # cursor color
            highlightthickness=0,
            relief=GROOVE,
            font=("lato", 14)
        )
        # self.file_entry.place(x=150,y=300,width=400,height=35)

        self.canvas.create_text(
            143.0,
            134.0,
            anchor="nw",
            text="Arrange Seats",
            fill="#264EC9",
            font=("Lato Regular", 40 * -1)
        )

        self.canvas.create_rectangle(
            150.0,
            203.00000035671775,
            496.0,
            204.00003051757812,
            fill="#264EC9",
            outline=""
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_image_1 = self.button_image_1.subsample(2)
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: choose_button(),
            relief="flat"
        )
        self.button_1.place(
            x=150.0,
            y=300.0,
            width=280.0,
            height=42.0
        )

        self.add_data_btn_image = PhotoImage(
            file=relative_to_assets("add_data_btn.png"))
        self.add_data_btn_image = self.add_data_btn_image.subsample(2)
        self.add_data_btn = Button(
            image=self.add_data_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda : read_file(self.file_path)
        )
        self.add_data_btn.place(
            x = 150,
            y = 365,
            width = 280,
            height = 42
        )

        self.erase_btn_image = PhotoImage(
            file=relative_to_assets("erase_button.png"))
        # self.erase_btn_image = self.erase_btn_image.subsample(2)
        self.clear_button=Button(
            image=self.erase_btn_image,
            bg="#000000",
            fg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clear_files(),
            relief=FLAT

        )
        self.clear_button.place(
            x=150,
            y=235,
            # width=280,
            # height=42
        )

        self.session_btn_image = PhotoImage(
            file=relative_to_assets("session_btn.png"))
        self.session_btn_image = self.session_btn_image.subsample(2)
        self.session_btn = Button(
            image=self.session_btn_image,
            bg="#000000",
            fg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: view_session(),
            relief=FLAT
        )
        self.session_btn.place(
            x=150,
            y=430,
            width=279,
            height=42
        )

        self.arrange_btn_image = PhotoImage(
            file=relative_to_assets("arrange_btn.png"))
        self.arrange_btn_image = self.arrange_btn_image.subsample(2)
        self.arrange_btn = Button(
            image=self.arrange_btn_image,
            bg="#000000",
            fg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: arrange_seats(self),
            relief=FLAT
        )
        self.arrange_btn.place(
            x=150,
            y=495,
            width=279,
            height=42
        )

        self.erase_seat_btn_image = PhotoImage(
            file=relative_to_assets("erase_seat_btn.png"))
        self.erase_seat_btn_image = self.erase_seat_btn_image.subsample(2)
        self.erase_seat_btn = Button(
            image=self.erase_seat_btn_image,
            bg="#000000",
            fg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clear_seats(),
            relief=FLAT
        )
        self.erase_seat_btn.place(
            x=150,
            y=560,
            width=279,
            height=42
        )

        self.back_button_image = PhotoImage(file=relative_to_assets("back_button.png"))
        self.back_button_image = self.back_button_image.subsample(2)
        self.back_button = Button(
            image = self.back_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goto_page(home),
            relief = FLAT
        )
        self.back_button.place(x=10,y=10)
        self.f = Frame(root)
        self.session_table = Treeview(self.f,columns = ("date","session"),show='headings',height=15)
        self.vscroll = Scrollbar(
            self.f,
            orient="vertical",
            command=self.session_table.yview
        )
        self.session_table.pack(side="left",fill = 'x')
        self.vscroll.pack(side = 'right',fill = 'x')
        self.session_table.configure(yscrollcommand=self.vscroll.set)
        self.session_table.heading('date',text = 'Date')
        self.session_table.heading('session',text = 'Session')

        self.session_table.bind("<ButtonRelease-1>",select_rec)

class view_seats(Frame):
    def __init__(self):
        super().__init__()
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alham\Downloads\navi\navi\assets\view")

        self.date_ses = []

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        def goto_page(frame):
            frame()
            self.date_ses=[]
            view_seats.destroy(self)

        def select_rec(e):
            selected = self.session_table.focus()
            values = self.session_table.item(selected,'values')
            # print(values[0])
            self.date_ses = values
            print(self.date_ses)

        def view_arr():
            self.sf.place_forget()
            print("\nView Button\n")
            cursor = con.cursor()
            if self.date_ses:
                self.empty_table_label.place_forget()
                self.sf.place(x=530,y=200,width=620)
                cursor.execute("SELECT ktu_id,seatnum,room FROM seats WHERE date = %s and session = %s",(self.date_ses[0],self.date_ses[1]))
                con.commit()
                # print(cursor.fetchall())
                data = cursor.fetchall()
                if data:
                    self.create_file_btn.place(x=250,y=560)
                    for i in data:
                        print(i,"\n")
                        value = list()
                        for j in i:
                            value.append(j)
                        self.seat_table.insert(parent='',index=0,values = value)
                    cursor.close()
                else:
                    self.sf.place_forget()
                    self.empty_table_label.place(x=530,y=200)

        # def create_file():
        #     query = "select * from seats"
        
        self.canvas = Canvas(
            bg = "#2148C0",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            1142.0,
            541.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            640.0,
            359.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            160.0,
            127.0,
            anchor="nw",
            text="View  Arrangements",
            fill="#264EC9",
            font=("Lato Regular", 40 * -1)
        )

        self.canvas.create_rectangle(
            154.0,
            189.999946504283,
            1116.0,
            191.00003051757812,
            fill="#264EC9",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("back_button.png"))
        self.button_image_1 = self.button_image_1.subsample(2)
        self.button_1 = Button(
            image=self.button_image_1,
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goto_page(home),
            relief="flat"
        )
        self.button_1.place(
            x=10.0,
            y=10.0,
        )

        self.view_btn_image = PhotoImage(
            file=relative_to_assets("view_btn.png"))
        self.view_btn_image = self.view_btn_image.subsample(2)
        self.view_btn = Button(
            image=self.view_btn_image,
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: view_arr(),
            relief="flat"
        )
        self.view_btn.place(x=160,y=560)

        self.empty_table_label = Label(
            text = "NO ASSIGNMENTS FOUND",
            bg="#E4FCFF",
            fg = "#484646",
            font=("Lato Regular", 18 * -1)
        )

        self.create_file_btn = Button(
            bg="#ffffff",
            fg="#000000",
            text="Create File",
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: view_arr(),
            relief="flat"
        )
        # self.create_file_btn.place(x=250,y=560)

        self.f = Frame(root)
        self.session_table = Treeview(self.f,columns = ("date","session"),show='headings',height=15)
        self.vscroll = Scrollbar(
            self.f,
            orient="vertical",
            command=self.session_table.yview
        )
        self.session_table.pack(side="left",fill = 'x')
        self.vscroll.pack(side = 'right',fill = 'x')
        self.session_table.configure(yscrollcommand=self.vscroll.set)
        self.session_table.heading('date',text = 'Date')
        self.session_table.heading('session',text = 'Session')
        self.f.place(x=153,y=200,width = 350)

        self.session_table.delete(*self.session_table.get_children()) #Clearing The table
        cursor_obj = con.cursor()
        cursor_obj.execute("select distinct date,session from all_fields order by date desc")
        con.commit()
        # value = []
        for ses in cursor_obj:
            value = []
            for data in ses:
                value.append(data)
            self.session_table.insert(parent='',index=0,values = value)
        self.session_table.bind("<ButtonRelease-1>",select_rec)

        self.sf = Frame(root)
        self.seat_table = Treeview(self.sf,columns = ("ktu_id","seat_num","room_id"),show='headings',height=15)
        self.vscroll2 = Scrollbar(
            self.sf,
            orient="vertical",
            command=self.seat_table.yview
        )
        self.seat_table.pack(side="left",fill = 'x')
        self.vscroll2.pack(side = 'right',fill = 'x')
        self.seat_table.configure(yscrollcommand=self.vscroll2.set)
        self.seat_table.heading('ktu_id',text = 'Student')
        self.seat_table.heading('seat_num',text = 'Seat')
        self.seat_table.heading('room_id',text = 'Room')

loginScreen()
root.resizable(False,False)
root.mainloop()