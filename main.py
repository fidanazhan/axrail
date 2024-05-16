from VendingScreen import VendingScreenClass
from Cart import CartClass
from Payment import PaymentClass
import time

# Start here
def main():

    screen = 1
    input_value = str("Start")

    cart = CartClass({})

    print('\nPress q to exit\n')
    # print("")
    while(input_value != "q"):

        
        print("---------------------------------------------------------------------------------------------------------------\n")
        if(cart.check_cart_empty()):
            cart.print_cart()

        print("\n")


        if(screen == 1):
            VendingScreenClass.main_screen()
            input_value = str(input("What do you want to drink (Please insert number): "))

            if(input_value.lower() == "q"):
                break

            quantity_value = str(input("How many do you want : "))

            if(quantity_value.lower() == "q"):
                break

            # Check whether user put invalidate input
            check_ = cart.add_to_cart(input_value, quantity_value)
            if(check_):
                screen = 2
                continue
            else:
                screen = 1

        if(screen == 2):
            VendingScreenClass.confirmation_screen()
            confirmation_value = str(input("y/n : "))

            if(confirmation_value.lower() == "y"):
                screen = 3
            elif(confirmation_value.lower() == "n"):
                screen = 1
            elif(confirmation_value.lower() == "q"):
                break

            # print("Screen : ", screen)

        if(screen == 3):

            total = cart.total_price()
            VendingScreenClass.payment_screen(total)
            
            payment_input = str(input("How much do you want to paid : "))

            payment = PaymentClass(int(float(payment_input)), int(total))
            balance = int(payment.count_balance())

            print("Balance : ", balance)

            if(balance > 0):
                payment.notes_balance()
                screen = 4
            else:
                print("\nYOUR MONEY IS NOT ENOUGHT PLEASE INPUT BACK YOUR MONEY\n")
                screen = 3

        if(screen == 4):
            VendingScreenClass.thankyou_screen()
            cart = CartClass({})
            time.sleep(5)
            screen = 1

        print("")


        

if __name__=="__main__": 
    main() 

