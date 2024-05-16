from prettytable import PrettyTable
from VendingScreen import VendingScreenClass

class CartClass:
    item_dict = {}
    item = ""
    quantity = 0

    def __init__(self, item_dict):
        self.item_dict = item_dict

    def add_to_cart(self, item, quantity):

        if(item == "1"):
            item = "Pepsi"
            self.item_dict.update({item: quantity})
            return True
        elif(item == "2"):
            item = "Coke"
            self.item_dict.update({item: quantity})
            return True
        elif(item == "3"):
            item = "Mineral water"
            self.item_dict.update({item: quantity})
            return True
        else:
            return False


    def check_cart_empty(self):
        if(len(self.item_dict) != 0):
            return 1
        else:
            return 0

    def print_cart(self):
        print("In your cart : ")

        vending_machine_cart = PrettyTable(["Item","Quantity","Total Price"])

        #O(n)
        for p_item, p_quantity in self.item_dict.items():
            if(p_item.lower() == "pepsi"):
                price = 4
            if(p_item.lower() == "coke"):
                price = 3
            if(p_item.lower() == "mineral water"):
                price = 2

            vending_machine_cart.add_row([p_item, p_quantity, int(p_quantity) * int(price)])
            # print(p_item, " - ", p_quantity)
        
        print(vending_machine_cart, "\n")
        total = self.total_price()
        print("Total : RM", total, "\n")


    # Kene tengok balik code
    def total_price(self):
        total = 0
        
        #O(n)
        for p_item, p_quantity in self.item_dict.items():
            if(p_item.lower() == "pepsi"):
                price = 4
            if(p_item.lower() == "coke"):
                price = 3
            if(p_item.lower() == "mineral water"):
                price = 2

            total = total + int(p_quantity) * int(price)

        return total

        