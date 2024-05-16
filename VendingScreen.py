from VendingItem import VendingItemClass

class VendingScreenClass:

    @staticmethod
    def main_screen():
        print("Welcome To Our Vending Machine\n")
        pepsi = VendingItemClass("1 - Pepsi", 4)
        coke = VendingItemClass("2 - Coke", 3)
        mineral_water = VendingItemClass("3 - Mineral Water", 2)

        pepsi.display()
        coke.display()
        mineral_water.display()

    @staticmethod
    def confirmation_screen():
        print("\nDo you want proceed to payment now?\n")

    @staticmethod
    def thankyou_screen():
        print("\nThank you for using our vending machine.\n")

    @staticmethod
    def payment_screen(total_price):
        print("\nHere is your total ", total_price ,"\n")