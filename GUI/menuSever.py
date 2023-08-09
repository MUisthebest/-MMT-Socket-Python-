from tkinter import *
from tkinter import font
from define import *

menuSever = Tk()

fontWord = font.Font(family = "Times New Roman", size = 10)

def menuSeverSetup ():
    menuSever.geometry("200x150")
    menuSever.title('Sever')
    menuSever['background'] = COLOUR_BACKGROUND
    menuSever.resizable(False, False)
    buttonOpen = Button(menuSever, text = 'Open Sever', bg = COLOUR_BUTTON, fg = COLOUR_FONT, font = fontWord, activeforeground = COLOUR_AFTER, width = 10, padx = 10, pady = 15)
    buttonOpen.place(relx = 0.5, rely = 0.5, anchor = CENTER) 


menuSeverSetup()

menuSever.mainloop()
