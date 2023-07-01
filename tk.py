from tkinter import Tk

def no_tk_popup_window():
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()