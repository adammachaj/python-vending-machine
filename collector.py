import item


class Collector(item.Item):
    """Soda collector"""

    def __init__(self, code, price = 2.0):
        self.code = code
        self.price = price
        self.quantity = 5
        self.items = []

    def __str__(self):
        if not self.items:
            rep = "<empty>" + "\tCena: " + str(self.price)
        else:
            rep = str(self.items[0]) + "   Cena: " + str(self.price)
        return rep

    def add_item(self, i):
        if len(self.items) < self.quantity:
            self.items.append(i)
        else:
            print("Not enough slots in collector")

    def remove_items(self):
        self.items.clear()

    def get_item(self):
        if self.items[0] == None:
            return "No sodas here"
        else:
            return self.items[0].name

    def get_price(self):
        return self.price

    def buy_item(self):
        if not self.items:
            return "No sodas here"
        else:
            #print(self.items[0])
            #self.items.pop(0)
            return self.items.pop(0)
