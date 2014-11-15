

class TPV():
    def __init__(self, warehouse):
        self.warehouse = warehouse

    def buy(self, prod, qty):
        ok = self.warehouse.check_exists(prod)
        ok = ok and (qty <= self.warehouse.check_stock(prod))
        return "OK" if ok else "KO"
