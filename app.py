from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter import Frame



class Application():
    def __init__(self):
        self.root = Tk()
        self.initUI()
    
    def initUI(self):
        # Set general geometry
        self.root.geometry('1000x600')
        self.root.resizable(width=False, height=False)
        self.root.title('Box Manager')
        # leftpanel
        leftpanel = Frame(self.root, width=200, height=590, highlightbackground="gray", highlightcolor="gray", highlightthickness=3, bd=0)
        leftpanel.config(relief="sunken")
        leftpanel.pack(side=LEFT)
        leftpanel.place(x=5, y=5)

        self.users_button = ttk.Button(leftpanel , text="Registrar Usuario",command=self.root.destroy)
        self.users_button.place(x=0,y=0, width=195, height=50)
        self.membership_button = ttk.Button(leftpanel, text="Registrar Afiliación", command=self.root.destroy)
        self.membership_button.place(x=0,y=50, width=195, height=50)
        self.payment_button = ttk.Button(leftpanel, text="Registrar Pago", command=self.root.destroy)
        self.payment_button.place(x=0,y=100, width=195, height=50)

        #rightpanel
        rightpanel = Frame(self.root, width=785, height=590, highlightbackground="gray", highlightcolor="gray", highlightthickness=1, bd=0)
        rightpanel.pack(side=RIGHT)
        rightpanel.place(x=210, y=5)
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()