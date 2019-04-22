import machine, item, collector, coin
from tkinter import *

machine1 = machine.Machine(1)
machine1.snacks[30].add_item(item.Item("Cola"))
machine1.snacks[31].add_item(item.Item("Pepsi"))
machine1.snacks[32].add_item(item.Item("Fanta"))
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
        self.bought_lbl = Label(self, text="<empty>", font=("Arial Bold", 15))
        self.bought_lbl.grid(row=7, column=0, columnspan = 3)

        self.code_lbl = Label(self, text="", font=("Arial Bold", 30))
        self.code_lbl.grid(row=1, column=0, columnspan = 3, rowspan=2)

        "numbers"
        self.one = Button(self, text=" 1 ", font=("Arial Bold", 15), command=lambda: self.change_value("1"))
        self.one.grid(row=3, column=0)
        self.two =  Button(self, text=" 2 ", font=("Arial Bold", 15), command=lambda: self.change_value("2"))
        self.two.grid(row=3, column=1)
        self.three = Button(self, text=" 3 ", font=("Arial Bold", 15), command=lambda: self.change_value("3"))
        self.three.grid(row=3, column=2)
        self.one = Button(self, text=" 4 ", font=("Arial Bold", 15), command=lambda: self.change_value("4"))
        self.one.grid(row=4, column=0)
        self.two =  Button(self, text=" 5 ", font=("Arial Bold", 15), command=lambda: self.change_value("5"))
        self.two.grid(row=4, column=1)
        self.three = Button(self, text=" 6 ", font=("Arial Bold", 15), command=lambda: self.change_value("6"))
        self.three.grid(row=4, column=2)
        self.one = Button(self, text=" 7 ", font=("Arial Bold", 15), command=lambda: self.change_value("7"))
        self.one.grid(row=5, column=0)
        self.two = Button(self, text=" 8 ", font=("Arial Bold", 15), command=lambda: self.change_value("8"))
        self.two.grid(row=5, column=1)
        self.three = Button(self, text=" 9 ", font=("Arial Bold", 15), command=lambda: self.change_value("9"))
        self.three.grid(row=5, column=2)
        self.zero = Button(self, text=" 0 ", font=("Arial Bold", 15), command=lambda: self.change_value("0"))
        self.zero.grid(row=6, column=1)

        """accept"""
        self.submit_bttn = Button(self, text = "Accept", font=("Arial Bold", 15), bg="green", fg="black", command = self.get_item)
        self.submit_bttn.grid(row = 2, column = 3, sticky = W)

        """cancel"""
        self.cancel = Button(self, text=" C ", font=("Arial Bold", 15), bg="orangered3", fg="black", command=self.cancel_value)
        #Aviable in late 2019
        # self.cancel = Button(self, text=" C ", command=lambda: self.code_lbl["text"] = self.code_lbl["text"][:-1])
        self.cancel.grid(row=6, column=2)

        self.first_shelf = Label(self, text = "30\n" + str(machine1.snacks[30]), font=("Arial Bold", 15))
        self.first_shelf.grid(row = 1, column = 6, columnspan = 4, rowspan=2)
        self.second_shelf = Label(self, text = "31\n" + str(machine1.snacks[31]), font=("Arial Bold", 15))
        self.second_shelf.grid(row = 3, column = 6, columnspan = 4, rowspan=2)
        self.third_shelf = Label(self, text = "32\n" + str(machine1.snacks[32]), font=("Arial Bold", 15))
        self.third_shelf.grid(row = 5, column = 6, columnspan = 4, rowspan=2)
        self.fourth_shelf = Label(self, text = "33\n" + str(machine1.snacks[33]), font=("Arial Bold", 15))
        self.fourth_shelf.grid(row = 7, column = 6, columnspan = 4, rowspan=2)
        self.fifth_shelf = Label(self, text = "34\n" + str(machine1.snacks[34]), font=("Arial Bold", 15))
        self.fifth_shelf.grid(row = 9, column = 6, columnspan = 4, rowspan=2)

        money = 0 / 10
        self.credit = Label(self, text = str(money), font=("Arial Bold", 15))
        self.credit.grid(row = 2, column = 13, columnspan = 2)

        self.onegr = Button(self, text=" 1gr ", font=("Arial Bold", 15), command=lambda: self.add_coin("1 gr"))
        self.onegr.grid(row=3, column=13, columnspan = 1)
        self.twogr =  Button(self, text=" 2gr ", font=("Arial Bold", 15), command=lambda: self.add_coin("2 gr"))
        self.twogr.grid(row=3, column=14, columnspan = 1)
        self.fivegr = Button(self, text=" 5gr ", font=("Arial Bold", 15), command=lambda: self.add_coin("5 gr"))
        self.fivegr.grid(row=3, column=15, columnspan = 1)
        self.tengr = Button(self, text=" 10gr ", font=("Arial Bold", 15), command=lambda: self.add_coin("10 gr"))
        self.tengr.grid(row=4, column=13, columnspan = 1)
        self.twgr =  Button(self, text=" 20gr ", font=("Arial Bold", 15), command=lambda: self.add_coin("20 gr"))
        self.twgr.grid(row=4, column=14, columnspan = 1)
        self.fifgr = Button(self, text=" 50gr ", font=("Arial Bold", 15), command=lambda: self.add_coin("50 gr"))
        self.fifgr.grid(row=4, column=15, columnspan = 1)
        self.onez = Button(self, text=" 1zl ", font=("Arial Bold", 15), command=lambda: self.add_coin("1 zl"))
        self.onez.grid(row=5, column=13, columnspan = 1)
        self.twoz = Button(self, text=" 2zl ", font=("Arial Bold", 15), command=lambda: self.add_coin("2 zl"))
        self.twoz.grid(row=5, column=14, columnspan = 1)
        self.fivz = Button(self, text=" 5zl ", font=("Arial Bold", 15), command=lambda: self.add_coin("5 zl"))
        self.fivz.grid(row=5, column=15, columnspan = 1)

    def add_coin(self, value):
        money = float(self.credit["text"])
        machine1.money_in[value] += 1
        value = coin.Coin.COINS[value]
        self.credit["text"] = round((money + value), 2)

    def change_value(self, number):
        self.code_lbl["text"] += number
        if self.code_lbl["text"] == "123":
            print("correct")

    def cancel_value(self):
        text = self.code_lbl["text"]
        self.code_lbl["text"] = text[:-1]

    def update_widgets(self):
        self.first_shelf["text"] = "30\n" + str(machine1.snacks[30])
        self.second_shelf["text"] = "31\n" + str(machine1.snacks[31])
        self.third_shelf["text"] = "32\n" + str(machine1.snacks[32])
        self.fourth_shelf["text"] = "33\n" + str(machine1.snacks[33])
        self.fifth_shelf["text"] = "34\n" + str(machine1.snacks[34])

    def get_item(self):
        self.update_widgets()
        kod = int(self.code_lbl.cget("text"))

        if float(self.credit["text"]) >= machine1.snacks[kod].get_price():
            bought_item = machine1.snacks[kod].buy_item()
            self.code_lbl["text"] = ""
            self.bought_lbl["text"] = bought_item
            self.update_widgets()
            self.change()

        else:
            pass

    def change(self):

        for i in machine1.money_in:
            machine1.coins[i] += machine1.money_in[i]

            for j in machine1.money_in:
                machine1.money_in[j] = 0



root = Tk()
root.title("Vending Machine ")
root.geometry("600x450")

app = Application(root)

root.mainloop()
