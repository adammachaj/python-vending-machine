from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        print(f'app: {type(self)}')

    def create_widgets(self):
        self.code_lbl = Label(self, text="asdasd", font=("Arial Bold", 15))
        # self.code_lbl.grid(row=0, column=0, columnspan=10)
        self.app = Keyboard(self)

    def change_value(self, number):
        self.code_lbl["text"] += number
        if self.code_lbl["text"] == "123":
            print("correct")

    def cancel_value(self):
        text = self.code_lbl["text"]
        self.code_lbl["text"] = text[:-1]


class Keyboard(Frame):
    def __init__(self, master):
        print(f'master: {type(master)}')
        Frame.__init__(self, master)
        print(f'self.master: {type(self.master)}')
        self.wig = Toplevel(self.master)
        print(f'new: {type(self.wig)}')
        self.wig.button = Button(self, text="Button 2", width=25, command=lambda: self.master.change_value("1"))
        print(type(self.wig.button.master))

        self.wig.grid()
        # self.master = master
        # self.newWindow = Toplevel(self.master)
        # self.frame = Frame(self.master)
        # self.one = Button(self.frame, text=" 1 ", font=("Arial Bold", 15),
        #                   command=lambda: self.master.change_value("1"))
        # self.one.grid(row=3, column=0)
        # self.frame.pack()


def main():
    root = Tk()
    root.title("Vending Machine ")
    root.geometry("500x450")
    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
