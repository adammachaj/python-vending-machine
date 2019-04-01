class Item(object):
    """Snack"""

    def __init__(self, name = "<name>"):
        self.name = name

    def __str__(self):
        rep = self.name
        return rep
