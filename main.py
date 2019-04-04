import machine, item, collector
from tkinter import *

machine1 = machine.Machine(1)
machine1.snacks[30].add_item(item.Item("Cola"))
machine1.snacks[31].add_item(item.Item("Cola"))
machine1.snacks[32].add_item(item.Item("Cola"))
machine1.snacks[33].add_item(item.Item("Cola"))
machine1.snacks[34].add_item(item.Item("Cola"))


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
        self.blank1_lbl = Label(self, text = "\t")
        self.blank1_lbl.grid(row = 0, column = 0, sticky=W)

        self.inst_lbl = Label(self, text = "VENDING MACHINE\n")
        self.inst_lbl.grid(row = 0, column = 1, columnspan = 2, sticky = W)

        # utwórz etykietę do kodu
        self.pw_lbl = Label(self, text = "KOD: ")
        self.pw_lbl.grid(row = 1, column = 2, sticky = W)
        # utwórz widżet Entry do przyjęcia hasła
        self.code_ent = Entry(self)
        self.code_ent.grid(row = 1, column = 3, sticky = W)

        # utwórz przycisk 'Akceptuj'
        self.submit_bttn = Button(self, text = "Accept", command = self.get_item)
        self.submit_bttn.grid(row = 1, column = 2, sticky = W)


        self.first_shelf = Label(self, text = "30\n" + str(machine1.snacks[30]))
        self.first_shelf.grid(row = 1, column = 0, sticky = W)

        self.second_shelf = Label(self, text = "31\n" + str(machine1.snacks[31]))
        self.second_shelf.grid(row = 2, column = 0, sticky = W)

        self.third_shelf = Label(self, text = "32\n" + str(machine1.snacks[32]))
        self.third_shelf.grid(row = 3, column = 0, sticky = W)

        self.fourth_shelf = Label(self, text = "33\n" + str(machine1.snacks[33]))
        self.fourth_shelf.grid(row = 4, column = 0, sticky = W)

        self.fifth_shelf = Label(self, text = "34\n" + str(machine1.snacks[34]))
        self.fifth_shelf.grid(row = 5, column = 0, sticky = W)

    def update_widgets(self):
        self.first_shelf = Label(self, text = "30\n" + str(machine1.snacks[30]))
        self.second_shelf = Label(self, text = "31\n" + str(machine1.snacks[31]))
        self.third_shelf = Label(self, text = "32\n" + str(machine1.snacks[32]))
        self.fourth_shelf = Label(self, text = "33\n" + str(machine1.snacks[33]))
        self.fifth_shelf = Label(self, text = "34\n" + str(machine1.snacks[34]))


    def get_item(self):
        kod = self.code_ent.get()
        machine1.snacks[int(kod)].buy_item()
        self.update_widgets()
        print(machine1.snacks[30])

root = Tk()
root.title("Vending Machine ")
root.geometry("500x450")

app = Application(root)

root.mainloop()
