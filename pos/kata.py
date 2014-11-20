

class TPV():
    def __init__(self, warehouse):
        self.warehouse = warehouse

    def buy(self, prod, qty):
        if not self.warehouse.check_exists(prod):
            return "KO"
        if qty <= self.warehouse.check_stock(prod):
            return "OK"

        return "KO"
