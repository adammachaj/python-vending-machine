class Coin(object):
    """Coins"""

    COINS = {"1 gr" : 0.01, "2 gr" : 0.02, "5 gr" : 0.05,
             "10 gr" : 0.1, "20 gr" : 0.2, "50 gr" : 0.5,
             "1 zl" : 1.0, "2 zl" : 2.0, "5 zl" : 5.0}

    def __init__(self, coin_id):
        self.coin_id = coin_id
        self.value = self.COINS[self.coin_id]

    def __str__(self):
        rep = str(self.value)
        return rep
