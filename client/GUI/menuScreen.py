from tkinter import *
from tkinter import scrolledtext
from tkinter import font
from tkinter import ttk
import tkinter as tk
from tkinter import Toplevel, Label, Button, PhotoImage
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText

import os
import time
try:
    from . import communicate
    from .define import *
    from .app import App
except:
    import communicate
    from define import *
    from app import App


mainclient = None
fontWord = None


class MyStruct:
    def __init__(self, string1, string2, string3):
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3

pcs_list = []
app_list = []

   

def click_button(s):
    communicate.command = s

# Điều kiện của KILL

def notice4(root):
    my_not4 = Toplevel(root)
    my_not4.geometry("250x250")
    my_not4.configure(bg = COLOUR_BACKGROUND)
    my_not4.title('')
    l1 = Label(my_not4,text = 'Đã diệt proccess',bg = COLOUR_BACKGROUND,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)

def notice5(root):
    my_not5 = Toplevel(root)
    my_not5.geometry("250x250")
    my_not5.configure(bg = COLOUR_BACKGROUND)
    my_not5.title('')
    l1 = Label(my_not5,text = 'Không tồn tại proccess',bg = COLOUR_BACKGROUND,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)

# Điều kiện của Start

def notice6(root):
    my_not6 = Toplevel(root)
    my_not6.geometry("250x250")
    my_not6.configure(bg = COLOUR_BACKGROUND)
    my_not6.title('')
    l1 = Label(my_not6,text = 'Đã bật proccess',bg = COLOUR_BACKGROUND,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)


def kill(root,listbox_1,listbox_2,listbox_3,txt):
    if listbox_1.size() == 0:
        return
    get_id = txt.get()
    items = listbox_1.get(1, tk.END)
    for item in items:
       if get_id == item:
           notice4(root)
           index = items.index(item)
           listbox_1.delete(index+1)
           listbox_2.delete(index+1)
           listbox_3.delete(index+1)
           
def start(listbox_1,listbox_2,listbox_3,txt):
    if listbox_1.size() == 0:
         return
    get_id = txt.get()
    if get_id == "Haaland":
        listbox_1.insert(tk.END,get_id)
        listbox_2.insert(tk.END,get_id)
        listbox_3.insert(tk.END,get_id)

    
def kill_window(root,listbox_1,listbox_2,listbox_3):
    my_kll = Toplevel(root)
    my_kll.geometry("280x60")
    my_kll.configure(bg = COLOUR_BACKGROUND)
    my_kll.title('Kill')
    txt = Entry(my_kll,width=30)
    txt.place(x=1, y=10)
    txt.focus()
    Button(my_kll, text="Kill",width=8,command = lambda: kill(root,listbox_1,listbox_2,listbox_3,txt)).place(x=200, y=10)

    
    
def start_window(root,listbox_1,listbox_2,listbox_3):
    my_sta = Toplevel(root)
    my_sta.geometry("280x60")
    my_sta.configure(bg = COLOUR_BACKGROUND)
    my_sta.title('Start')
    txt = Entry(my_sta,width=30)
    txt.place(x=1, y=10)
    txt.focus()
    Button(my_sta, text = "Start", width = 8,command = lambda: start(listbox_1,listbox_2,listbox_3,txt)).place(x = 200, y = 10)

def do_kill(s,root,listbox_1,listbox_2,listbox_3):
    click_button(s)
    kill_window(root,listbox_1,listbox_2,listbox_3)        

def do_start(s,root,listbox_1,listbox_2,listbox_3):
    click_button(s)
    start_window(root,listbox_1,listbox_2,listbox_3)

def do_view(s,root,listbox_1,listbox_2,listbox_3):
    click_button(s)
    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "Data.txt")
    if communicate.command ==  "Xem":
       with open(img_path, 'r') as file:
          lines = file.readlines()
          for line in lines:
            values = line.strip().split(',')
            if len(values) == 3:
               my_struct = MyStruct(values[0], values[1], values[2])
               pcs_list.append(my_struct)
               listbox_1.insert(tk.END,my_struct.string1)
               listbox_2.insert(tk.END,my_struct.string2)
               listbox_3.insert(tk.END,my_struct.string3)

def do_clear(s,root,listbox_1,listbox_2,listbox_3):
    click_button(s)
    listbox_1.delete(1, tk.END)
    listbox_2.delete(1, tk.END)
    listbox_3.delete(1, tk.END)
    
    
def displayImage(my_scr):
    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "tempData/tempImage.png")

    # Open and resize the image using Pillow
    new_width = 490
    new_height = 450
    with Image.open(img_path) as img:
        img = img.resize((new_width, new_height))

    # Convert PIL image to PhotoImage
    img_tk = ImageTk.PhotoImage(img)

    label = Label(my_scr, image=img_tk, width=new_width, height=new_height)
    label.image = img_tk  # this is to prevent garbage collection of the img_tk object
    label.place(relx=0.08, rely=0.1)

#Khi nào merge được connection sẽ dùng để check kết nối   
def notice1():
    my_not1 = Toplevel(mainClient)
    my_not1.geometry("250x250")
    my_not1.configure(bg = COLOUR_BACKGROUND)
    my_not1.title('')
    l1 = Label(my_not1,text = 'Chưa kết nối đến server',bg = COLOUR_BACKGROUND,fg = '#272829',activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)


    
def notice2():
    my_not2 = Toplevel(mainClient)
    my_not2.geometry("250x250")
    my_not2.configure(bg = COLOUR_BACKGROUND)
    my_not2.title('')
    l1 = Label(my_not2,text = 'Lỗi kết nối đến server',bg = COLOUR_BACKGROUND,fg = '#272829',activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)



def notice3():
    my_not3 = Toplevel(mainClient)
    my_not3.geometry("250x250")
    my_not3.configure(bg = COLOUR_BACKGROUND)
    my_not3.title('')
    l1 = Label(my_not3,text = 'Kết nối đến server thành công',bg = COLOUR_BACKGROUND,fg = '#272829',activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)    

def scr_window():
    #if communicate.status_connection == 0:
    #    notice1()
    #    return
    notice3()
    my_scr = Toplevel(mainClient)
    my_scr.geometry("700x600")
    my_scr.configure(bg = COLOUR_BACKGROUND)
    my_scr.title('Server Screen')
    my_scr.resizable(False, False)
    communicate.src_screen = my_scr

    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "tempData/tempImage.png")
    img = PhotoImage(file = img_path)

    img_width = img.width()
    img_height = img.height()

    label = Label(my_scr, image = img, width = img_width, height = img_height)
    label.image = img
    label.place(relx = 0.08, rely = 0.1 )

    label = Label(my_scr, width = 70, height= 30)
    label.place(relx = 0.08, rely = 0.1 )

    buton1 = Button(my_scr,text = 'Chụp',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord, width = 8, height = 16, command = lambda: click_button("screenshot"))
    buton2 = Button(my_scr,text = 'Lưu',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 8, height = 8, command = lambda: click_button("saveimage"))
    buton1.place(x = 600, y = 65 )
    buton2.place(x = 600, y = 380 )



def kst_window():
    #if communicate.status_connection == 0:
    #   notice1()
    #return
    notice3()
    my_kst = Toplevel(mainClient)
    my_kst.geometry("750x500")
    my_kst.configure(bg = COLOUR_BACKGROUND)
    my_kst.title('Keystroke')
    my_kst.resizable(False, False)
    frame1 = ttk.Frame(my_kst)
    frame1.pack(side="top", pady=20)
    button1 = ttk.Button(frame1, text="Hook", width=20, command=lambda: click_button("hook"))
    button2 = ttk.Button(frame1, text="Unhook", width=20, command=lambda: click_button("unhook"))
    button3 = ttk.Button(frame1, text="In phím", width=20, command=lambda: click_button("sendkeylogger"))
    button4 = ttk.Button(frame1, text="Xóa", width=20, command=lambda: click_button("deletecontentkeylogger"))
    button_list = [button1, button2, button3, button4]
    for i in range(len(button_list)):
        button_list[i].pack(side="left", padx=15)
    frame2 = ttk.Frame(my_kst)
    frame2.pack(side="top",pady=15)
    txt = Listbox(frame2,width=105,height=25)
    txt.pack()

def pcs_window():
    #if communicate.status_connection == 0:
    #   notice1()
    #return
    my_pcs = Toplevel(mainClient)
    my_pcs.geometry("750x500")
    my_pcs.configure(bg = COLOUR_BACKGROUND)
    my_pcs.title('process')
    my_pcs.resizable(False, False)
    frame1 = ttk.Frame(my_pcs)
    frame1.pack(side="top", pady=20)
    # Tạo listbox và đặt chúng ngang hàng nhau trong scrolledtext của frame 2
    frame2 = ttk.Frame(my_pcs)
    frame2.pack(side="top")
    listbox_frame2 = tk.Listbox(frame2)
    frame2 = tk.Frame(my_pcs)
    scrolled_text = scrolledtext.ScrolledText(frame2,height =50)
    scrolled_text.pack()
    listbox_1 = tk.Listbox(scrolled_text,height =50)
    listbox_2 = tk.Listbox(scrolled_text,height =50)
    listbox_3= tk.Listbox(scrolled_text,height =50)
    listbox_1.insert(tk.END, "ID Proccess")
    listbox_2.insert(tk.END, "Name Proccess")
    listbox_3.insert(tk.END, "Count Thread")
    listbox_1.focus_set()
    listbox_2.focus_set()
    listbox_3.focus_set()
    listbox_1.pack(side=tk.LEFT)
    listbox_2.pack(side=tk.LEFT)
    listbox_3.pack(side=tk.LEFT)
    frame2.pack(side="top", pady=10)
    button1 = ttk.Button(frame1, text="Kill", width=20,  command = lambda: do_kill("Kill",frame1,listbox_1,listbox_2,listbox_3))
    button2 = ttk.Button(frame1, text="Xem", width=20, command = lambda: do_view("Xem",frame1,listbox_1,listbox_2,listbox_3))
    button3 = ttk.Button(frame1, text="Xóa", width=20, command = lambda: do_clear("Xóa",frame1,listbox_1,listbox_2,listbox_3))
    button4 = ttk.Button(frame1, text="Start", width=20, command = lambda: do_start("Start",frame1,listbox_1,listbox_2,listbox_3))
    button_list = [button1, button2, button3, button4]
    for i in range(len(button_list)):
        button_list[i].pack(side="left", padx=15)
    # Chạy chương trình
    my_pcs.mainloop()



def app_window():
    #if communicate.status_connection == 0:
    #   notice1()
    #return
    my_app = Toplevel(mainClient)
    my_app.geometry("750x500")
    my_app.configure(bg = COLOUR_BACKGROUND)
    my_app.title('listApp')
    my_app.resizable(False, False)
    frame1 = ttk.Frame(my_app)
    frame1.pack(side="top", pady=20)
    frame2 = ttk.Frame(my_app)
    frame2.pack(side="top")
    listbox_frame2 = tk.Listbox(frame2)
    frame2 = tk.Frame(my_app)
    scrolled_text = scrolledtext.ScrolledText(frame2,height =50)
    # Tạo listbox và đặt chúng ngang hàng nhau trong scrolledtext của frame 2
    listbox_1 = tk.Listbox(scrolled_text,height =50)
    listbox_2 = tk.Listbox(scrolled_text,height =50)
    listbox_3= tk.Listbox(scrolled_text,height =50)
    listbox_1.insert(tk.END, "ID Application")
    listbox_2.insert(tk.END, "Name Application")
    listbox_3.insert(tk.END, "Count Thread")
    listbox_1.focus_set()
    listbox_2.focus_set()
    listbox_3.focus_set()
    listbox_1.pack(side=tk.LEFT)
    listbox_2.pack(side=tk.LEFT)
    listbox_3.pack(side=tk.LEFT)
    frame2.pack(side="top", pady=10)
    scrolled_text.pack()
    button1 = ttk.Button(frame1, text="Kill", width=20,  command = lambda: do_kill("Kill",frame1,listbox_1,listbox_2,listbox_3))
    button2 = ttk.Button(frame1, text="Xem", width=20,command = lambda: do_view("Xem",frame1,listbox_1,listbox_2,listbox_3))
    button3 = ttk.Button(frame1, text="Xóa", width=20)
    button4 = ttk.Button(frame1, text="Start", width=20, command = lambda: do_start("Start",frame1,listbox_1,listbox_2,listbox_3))
    button_list = [button1, button2, button3, button4]
    for i in range(len(button_list)):
        button_list[i].pack(side="left", padx=15)
    # Chạy chương trình
    my_app.mainloop()

def on_combobox_changed(event):
        selected_choice = combobox.get()
        if selected_choice == choices[0]:
            print('In')
        elif selected_choice == choices[1]:
            print('Lưu')
        elif selected_choice == choices[2]:
            print('Xóa')

def print_string():
        selected_option = combo_box.get()
        print("In chuỗi:", selected_option)

def save_string():
        selected_option = combo_box.get()
        # Lưu chuỗi vào file hoặc database
        print("Lưu chuỗi:", selected_option)

def delete_string():
        selected_option = combo_box.get()
        # Xóa chuỗi khỏi file hoặc database
        print("Xóa chuỗi:", selected_option)

 
def rgt_window():
    my_rgt = Toplevel(mainClient)
    my_rgt.geometry("550x550")
    my_rgt.configure(bg = COLOUR_BACKGROUND)
    my_rgt.title('Registry')
    my_rgt.resizable(False, False) 
    # Tạo frame 1
    frame1 = ttk.Frame(my_rgt)
    frame1.pack(side="top", pady=5)

    textbox1 = ttk.Entry(frame1)
    textbox1.pack(side="left", padx=10, pady=10)
    textbox1.configure(width = 50) 

    button_browser = ttk.Button(frame1, text="Browser")
    button_browser.pack(side="left", padx=10, pady=10)

    # Tạo frame 2
    frame2 = ttk.Frame(my_rgt)
    frame2.pack(side="top",pady= 5)

    txt = scrolledtext.ScrolledText(frame2,height = 8)
    txt.pack(side="left")
    txt.configure(width = 38) 

    button_send_content = ttk.Button(frame2, text="Gửi nội dung")
    button_send_content.pack(side="left", padx=10, pady=10)
    

    # Tạo frame 3
    frame3 = ttk.Frame(my_rgt)
    frame3.pack(side="top")

    label_text = ttk.Label(frame3, text="Sửa Giá Trị Trực Tiếp --------------------------------------------------------------")
    label_text.pack(padx=2, pady=15)
    

    # Tạo frame 4

    frame4 = ttk.Frame(my_rgt)
    frame4.pack(side="top",pady=5)

    # Tạo combobox
    combobox = tk.StringVar(frame4)
    combobox.set("Chọn tác vụ")  # Giá trị mặc định
        
    # Tạo danh sách các lựa chọn
    choices = ["Get Value      ", "Creat Key      ", "Delete Value      ","Create Key      ","Delete Key      "]

    

    # Hàm xử lý khi người dùng thay đổi giá trị của combobox


    # Tạo combobox và gắn sự kiện cho nó
    combobox_widget = tk.OptionMenu(frame4 , combobox, *choices, command=on_combobox_changed)
    combobox_widget.configure(width = 63) 
    combobox_widget.pack(pady=10)

    # Tạo Frame 5
    frame5 = ttk.Frame(my_rgt)
    frame5.pack(side="top", pady=5)

    # Thêm Textbox vào Frame 1
    textbox1 = ttk.Entry(frame5)
    textbox1.pack(padx=10, pady=10)
    textbox1.configure(width = 66) 

    # Tạo Frame 6
    frame6 = ttk.Frame(my_rgt)
    frame6.pack(side="top", pady=5)

    # Thêm Textbox vào Frame 2 (cách đều nhau)
    textbox2 = ttk.Entry(frame6)
    textbox3 = ttk.Entry(frame6)
    combobox = tk.StringVar(frame6)
    textbox2.pack(side="left", padx=10)
    textbox3.pack(side="left", padx=10)
    combobox.set("Chọn tác vụ")  # Giá trị mặc định

    # Tạo danh sách các lựa chọn
    choices = ["String      ", "Binary    ", "DWORD      ","QWORD     ","Mute String   "]


    # Hàm xử lý khi người dùng thay đổi giá trị của combobox


    # Tạo combobox và gắn sự kiện cho nó
    combobox_widget = tk.OptionMenu(frame6 , combobox, *choices, command=on_combobox_changed)
    combobox_widget.configure(width = 10) 
    combobox_widget.pack(side="left", padx=10)


    # Tạo Frame 7
    frame7 = ttk.Frame(my_rgt)
    frame7.pack(side="top", pady=5)
        
    listbox = tk.Listbox(frame7)
    listbox.configure(width = 69, height = 8) 
    listbox.pack()





def get_ip(entryBox):
    ip = entryBox.get()
    communicate.status_connection = 1
    communicate.ipHost = ip

def check_valid_ip(ip):
    return True
    # Check if the IP contains only digits and dots
    return all(c.isdigit() or c == '.' for c in ip) 

def validate_input(char):
    return True
    # Allow only numbers and dots (for IP address)
    if char.isdigit() or char == '.':
        return True
    else:
        return False




def draw ():
    mainClient.columnconfigure(0, weight = 1)
    mainClient.columnconfigure(1, weight = 1)
    mainClient.columnconfigure(2, weight = 1)
    mainClient.rowconfigure(0, weight = 1)
    mainClient.rowconfigure(1, weight = 1)
    mainClient.rowconfigure(2, weight = 1)
    mainClient.rowconfigure(3, weight = 1)

    entryBox = Entry(mainClient, bg = "#E9F4EE", fg = "#000000", font = fontWord, justify = LEFT, bd = 15, width = 82) #validate = "key", validatecommand=(mainClient.register(validate_input), "%S")
    entryBox.grid(row = 0, column = 0, columnspan = 2, sticky = E)

    buttonConnect = Button(mainClient, text = "Connect", font = fontWord, width = 20, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 50, pady = 15, command=lambda: get_ip(entryBox))
    buttonConnect.grid(row = 0, column = 2)
    buttonProcess = Button(mainClient, text = "Process Running", font = fontWord, width = 20, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = lambda: pcs_window(), padx = 50, pady = 150)
    buttonProcess.grid(row = 1, column = 0, rowspan = 3)
    buttonApp = Button(mainClient, text = "App Running", font = fontWord, width = 26, bg = COLOUR_BUTTON, fg = COLOUR_FONT, command = lambda: app_window(), padx = 20, pady = 33)
    buttonApp.grid(row = 1, column = 1, sticky = 'EW')
    buttonTurnOff = Button(mainClient, text = "Turn-Off\n\nComputer", font = fontWord, width = 15, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 10, pady = 33)
    buttonTurnOff.grid(row = 2, column = 1, sticky = W)
    buttonCap = Button(mainClient, text = "Print\n\nScreen", font = fontWord, width = 15, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = lambda: scr_window(), padx = 10, pady = 33)
    buttonCap.grid(row = 2, column = 1, sticky = E)
    buttonRegistry = Button(mainClient, text = "Fix Registry", font = fontWord, width = 26, bg = COLOUR_BUTTON, fg = COLOUR_FONT, command = lambda: rgt_window(), padx = 20, pady = 33)
    buttonRegistry.grid(row = 3, column = 1, sticky = 'EW')
    buttonKeyStroke = Button(mainClient, text = "Keystroke", font = fontWord, width = 20, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = lambda: kst_window(), padx = 50, pady = 95)
    buttonKeyStroke.grid(row = 1, column = 2, rowspan = 2)
    buttonExit = Button(mainClient, text = "Exit", font = fontWord, width = 20, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 50, pady = 30)
    buttonExit.grid(row = 3, column = 2)
    mainClient.mainloop()


def on_closing():
    # This function will be executed when the close button is clicked
    communicate.command = "QUIT"

    # You can add any custom cleanup operations or other logic here

    # Close the window
    mainClient.quit()  # Quit the mainloop


def run_GUI():
    global mainClient, fontWord
    mainClient = Tk() 
    app = App(mainClient)
    fontWord = font.Font(family = "Times New Roman", size = 10)
    mainClient.protocol("WM_DELETE_WINDOW", on_closing)
    draw()
    # def is_mainClient_open():
    # print(is_mainClient_open())
    

if __name__ == '__main__':
    run_GUI()
