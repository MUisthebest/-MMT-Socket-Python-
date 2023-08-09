from tkinter import *
from define import *
from tkinter import scrolledtext
from tkinter import font
import os

from app import App

mainClient = Tk() 

app = App(mainClient)

fontWord = font.Font(family = "Terminal", size = 10)

def scr_window():
    my_scr = Toplevel(mainClient)
    my_scr.geometry("700x600")
    my_scr.configure(bg = COLOUR_BACKGROUND)
    my_scr.title('View Screen')
    my_scr.resizable(False, False)
    label = Label(my_scr,text = "",width = 70, height = 30)
    label.place(relx = 0.08, rely = 0.1 )
    buton1 = Button(my_scr,text = 'Chụp',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord, width = 8, height = 16)
    buton2 = Button(my_scr,text = 'Lưu',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 8, height = 8)
    buton1.place(x = 600, y = 65 )
    buton2.place(x = 600, y = 380 )

def kst_window():
    my_kst = Toplevel(mainClient)
    my_kst.geometry("700x550")
    my_kst.configure(bg = COLOUR_BACKGROUND)
    my_kst.title('Keystroke')
    my_kst.resizable(False, False)
    buton1 = Button(my_kst,text = 'Hook',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 6, height = 2).grid(column = 0, row = 20, sticky = N)
    buton2 = Button(my_kst,text = 'Unhook',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 6, height = 2).grid(column = 1, row = 20, sticky = N)
    buton3 = Button(my_kst,text = 'In phím',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 6, height = 2).grid(column = 2, row = 20, sticky = N)
    buton4 = Button(my_kst,text = 'Xóa',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 6, height = 2).grid(column = 3, row = 20, sticky = N)
    my_kst.columnconfigure(0,weight=1)
    my_kst.columnconfigure(1,weight=1)
    my_kst.columnconfigure(2,weight=1)
    my_kst.columnconfigure(3,weight=1)
    txt = scrolledtext.ScrolledText(my_kst,width=65,height=25)
    txt.place(relx = 0.1, rely = 0.2)


def pcs_window():
    my_pcs = Toplevel(mainClient)
    my_pcs.geometry("750x650")
    my_pcs.configure(bg = COLOUR_BACKGROUND)
    my_pcs.title('process')
    my_pcs.resizable(False, False)
    buton1 = Button(my_pcs,text = 'Kill',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 4, height = 2).grid(column = 0, row = 20, sticky = N)
    buton2 = Button(my_pcs,text = 'Lưu',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 4, height = 2).grid(column = 1, row = 20, sticky = N)
    buton3 = Button(my_pcs,text = 'Xóa',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 4, height = 2).grid(column = 2, row = 20, sticky = N)
    buton4 = Button(my_pcs,text = 'Start',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 4, height = 2).grid(column = 3, row = 20, sticky = N)
    my_pcs.columnconfigure(0,weight=1)
    my_pcs.columnconfigure(1,weight=1)
    my_pcs.columnconfigure(2,weight=1)
    my_pcs.columnconfigure(3,weight=1)
    txt = scrolledtext.ScrolledText(my_pcs,width=40,height=20)
    txt.place(relx = 0.2, rely = 0.2)    

mainClient.columnconfigure(0, weight = 1)
mainClient.columnconfigure(1, weight = 1)
mainClient.columnconfigure(2, weight = 1)
mainClient.rowconfigure(0, weight = 1)
mainClient.rowconfigure(1, weight = 1)
mainClient.rowconfigure(2, weight = 1)
mainClient.rowconfigure(3, weight = 1)

entryBox = Entry(mainClient, bg = "#E9F4EE", fg = "#000000", font = fontWord, justify = LEFT, bd = 15, width = 82)
entryBox.grid(row = 0, column = 0, columnspan = 2, sticky = E)

buttonConnect = Button(mainClient, text = "Connect", font = fontWord, width = 20, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 50, pady = 15)
buttonConnect.grid(row = 0, column = 2)

buttonProcess = Button(mainClient, text = "Process Running", font = fontWord, width = 20, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = pcs_window(), padx = 50, pady = 150)
buttonProcess.grid(row = 1, column = 0, rowspan = 3)

buttonApp = Button(mainClient, text = "App Running", font = fontWord, width = 26, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 20, pady = 33)
buttonApp.grid(row = 1, column = 1, sticky = 'EW')

buttonTurnOff = Button(mainClient, text = "Turn-Off\n\nComputer", font = fontWord, width = 15, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 10, pady = 33)
buttonTurnOff.grid(row = 2, column = 1, sticky = W)

buttonCap = Button(mainClient, text = "Print\n\nScreen", font = fontWord, width = 15, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = scr_window(), padx = 10, pady = 33)
buttonCap.grid(row = 2, column = 1, sticky = E)

buttonRegistry = Button(mainClient, text = "Fix Registry", font = fontWord, width = 26, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 20, pady = 33)
buttonRegistry.grid(row = 3, column = 1, sticky = 'EW')

buttonKeyStroke = Button(mainClient, text = "Keystroke", font = fontWord, width = 20, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = kst_window(), padx = 50, pady = 95)
buttonKeyStroke.grid(row = 1, column = 2, rowspan = 2)

buttonExit = Button(mainClient, text = "Exit", font = fontWord, width = 20, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 50, pady = 30)
buttonExit.grid(row = 3, column = 2)


mainClient.mainloop()
