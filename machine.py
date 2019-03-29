import item, collector, coin

class Machine(object):
    """Vending machine"""

    ITEMS = [item.Item(1, "Pepsi"), item.Item(2, "Cola"), item.Item(3, "Sprite")]
    snacks = {}
    coins = {"1 gr" : 5, "2 gr" : 5, "5 gr" : 5,
             "10 gr" : 5, "20 gr" : 5, "50 gr" : 5,
             "1 zl" : 5, "2 zl" : 5, "5 zl" : 5}


    def __init__(self):
        self.snacks = {n : collector.Collector(n) for n in range(30, 35)}

        self.coins =   {coin.Coin("1 gr") : 5, coin.Coin("2 gr") : 5,coin.Coin("5 gr") : 5,
                        coin.Coin("10 gr"): 5, coin.Coin("20 gr") : 5,coin.Coin("50 gr") : 5,
                        coin.Coin("1 zl"): 5,coin.Coin("2 zl") : 5,coin.Coin("5 zl") : 5}

        self.money_in = {"1 gr" : 0, "2 gr" : 0, "5 gr" : 0,
                            "10 gr" : 0, "20 gr" : 0, "50 gr" : 0,
                             "1 zl" : 0, "2 zl" : 0, "5 zl" : 0}
        self.sum = 0

    def __str__(self):
        rep = "Sodas:\n" + str(self.snacks) + "\nCoins:\n" + str(self.coins)
        return rep

    def insert_coin(self, coin_id):
        return (coin_id, coin.Coin.COINS[coin_id])

    def buy(self):
        while True:
            coin_id = input("Coin: ")
            current_coin = self.insert_coin(coin_id)
            print(current_coin)
            self.money_in[coin_id] += 1
            print(self.money_in)
            self.sum += coin.Coin.COINS[coin_id]
            print(self.sum)

