from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog



class Application():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1000x600')
        self.root.resizable(width=True, height=True)
        self.root.title('Box Manager')

        self.root.mainloop()

if __name__ == "__main__":
    app = Application()