from prettytable import PrettyTable

class PaymentClass:
    paid = 0
    cost = 0

    def __init__(self, paid, cost):
        self.paid = paid
        self.cost = cost

    def count_balance(self):
        balance = self.paid - self.cost 
        return balance
    
    def notes_balance(self):
        money_notes = [100, 50, 20, 10, 5, 1]
        notes_balance_dict = {}

        balance = self.count_balance()

        for note in money_notes:
            
            if(balance % note != 0):
                balance_note = balance / note
                balance = balance % note

                notes_balance_dict.update({note: int(balance_note)})

                # print("Balancev (func1) : ", balance, ", Notes : ", note, ", Balance Note : ", int(balance_note))
            elif(balance % note == 0):
                balance_note = balance / note
                balance = balance % note
                notes_balance_dict.update({note: int(balance_note)})

                # print("Balance (func2) : ", balance, ", Notes : ", note, ", Balance Note : ", int(balance_note))

        vending_machine_cart = PrettyTable(["Notes","Quantity"])

        for notes, n_quantity in notes_balance_dict.items():
            vending_machine_cart.add_row([notes, n_quantity])

        print(vending_machine_cart)