### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item, amount_needed in ingredients.items():
            if self.machine_resources[item] < amount_needed:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("How many dollars?: ")) * 1.0
        half_dollars = int(input("How many half dollars?: ")) * 0.5
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05
        return dollars + half_dollars + quarters + nickels

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Not enough money, sorry! Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

def main():
    machine = SandwichMachine(resources)

    while True:
        choice = input("What would you like? (small/medium/large/off): ").lower()

        if choice == "off":
            print("Turning off the machine.")
            break
        elif choice in recipes:
            sandwich = recipes[choice]
            if machine.check_resources(sandwich["ingredients"]):
                inserted_coins = machine.process_coins()
                if machine.transaction_result(inserted_coins, sandwich["cost"]):
                    machine.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please select small, medium, large, off.")


if __name__ == "__main__":
    main()