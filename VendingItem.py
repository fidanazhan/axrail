class VendingItemClass:
    name = ""
    price = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name + " : RM" + str(self.price))

