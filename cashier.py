class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        # Process the coin inputs from the customer.
        print("Please insert coin payment: ")
        total = int(input("Quarters? ($0.25) ")) * 0.25
        total += int(input("Dimes? ($0.10) ")) * 0.10
        total += int(input("Nickels? ($0.05) ")) * 0.05
        total += int(input("Pennies? ($0.01) ")) * 0.01
        return total

    def transaction_result(self, cost, payment):
        # Is the payment successful/unsuccessful?
        if payment >= cost:
            change = round(payment - cost, 2)
            print(f"Thank you! Here is ${change} in change!")
            return True
        else:
            print("Sorry! That's not enough money!")
            return False
