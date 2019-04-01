import item

class Collector(item.Item):
    """Soda collector"""

    def __init__(self, code, price = 2.0):
        self.code = code
        self.price = price
        self.quantity = 10
        self.items = []

    def __str__(self):
        rep = "Name: " + str(self.items[0]) + "\tCena: " + str(self.price)
        return rep

    def add_item(self, i):
        if self.quantity < 11:
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
