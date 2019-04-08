"""https://likegeeks.com/python-gui-examples-tkinter-tutorial/"""

from tkinter import *


class Application(Frame):
    """"""

    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Utwórz widżety typu Button, Text i Entry . """
        # utwórz etykietę z instrukcją

        self.code_lbl = Label(self, text="")
        self.code_lbl.grid(row=0, column=0, columnspan = 10)

        """numbers"""
        self.one = Button(self, text=" 1 ", command=lambda: self.change_value("1"))
        self.one.grid(row=3, column=0)
        self.two =  Button(self, text=" 2 ", command=lambda: self.change_value("2"))
        self.two.grid(row=3, column=1)
        self.three = Button(self, text=" 3 ", command=lambda: self.change_value("3"))
        self.three.grid(row=3, column=2)
        self.one = Button(self, text=" 4 ", command=lambda: self.change_value("4"))
        self.one.grid(row=4, column=0)
        self.two =  Button(self, text=" 5 ", command=lambda: self.change_value("5"))
        self.two.grid(row=4, column=1)
        self.three = Button(self, text=" 6 ", command=lambda: self.change_value("6"))
        self.three.grid(row=4, column=2)
        self.one = Button(self, text=" 7 ", command=lambda: self.change_value("7"))
        self.one.grid(row=5, column=0)
        self.two = Button(self, text=" 8 ", command=lambda: self.change_value("8"))
        self.two.grid(row=5, column=1)
        self.three = Button(self, text=" 9 ", command=lambda: self.change_value("9"))
        self.three.grid(row=5, column=2)
        self.zero = Button(self, text=" 0 ", command=lambda: self.change_value("0"))
        self.zero.grid(row=6, column=1)
        """cancel"""
        self.cancel = Button(self, text=" C ", bg="orangered3", fg="black", command=self.cancel_value)
        #Aviable in late 2019
        # self.cancel = Button(self, text=" C ", command=lambda: self.code_lbl["text"] = self.code_lbl["text"][:-1])
        self.cancel.grid(row=6, column=2)

    def change_value(self, number):
        self.code_lbl["text"] += number
        if self.code_lbl["text"] == "123":
            print("correct")

    def cancel_value(self):
        text = self.code_lbl["text"]
        self.code_lbl["text"] = text[:-1]




root = Tk()
root.title("Vending Machine ")
root.geometry("500x450")

app = Application(root)

root.mainloop()
