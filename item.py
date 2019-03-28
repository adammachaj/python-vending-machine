class Item(object):
    """Snack"""

    code_number = 30

    def __init__(self, id_snack, name = "<name>", price = 2.0, code = code_number):
        self.id_snack = id_snack
        self.name = name
        self.price = price
        self.code = code
        Item.code_number += 1

    def __str__(self):
        rep = "ID: " + str(self.id_snack) + "\t" + self.name + "\tCena: " + str(self.price) + "\tKod: " + str(self.code)
        return rep
