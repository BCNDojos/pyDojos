from store import Store

class POS(object):
    def __init__(self, prices = None):
        self.scanned = []
        self.prices = prices

    def scan(self, code, quantity):
        self.scanned.append((code, quantity))
        store = Store()
        store.lock(code, quantity)

    def get_line(self, product):
        return product[0], product[1], self.prices[product[0]], self.prices[product[0]] * product[1]

    def list(self):
        if self.prices is None:
            return self.scanned
        return [self.get_line(product) for product in self.scanned]