from define import *

class App():
    def __init__(self, ROOT) -> None:
        ROOT.geometry('650x400')
        ROOT.title('Main Menu')
        ROOT['background'] = COLOUR_BACKGROUND
        ROOT.resizable(False, False)