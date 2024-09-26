# main (Assignment 1).py
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    print("Welcome to the Christofu's Sandwich Maker!")

    # Print the sandwich sizes.
    size = input("What size sandwich would you like? (small / medium / large): ")

    if size in recipes:
        sandwich = recipes[size]["ingredients"]
        cost = recipes[size]["cost"]

        # Check resources.
        if sandwich_maker_instance.check_resources(sandwich):
            # Process payment.
            payment = cashier_instance.process_coins()
            if cashier_instance.transaction_result(cost, payment):
                # Make the sandwich.
                sandwich_maker_instance.make_sandwich(sandwich)
        else:
            print("Unfortunately we can't make that sandwich. I apologize.")
    else:
        print("That sandwich size does not exist, sorry!")


if __name__ == "__main__":
    main()

