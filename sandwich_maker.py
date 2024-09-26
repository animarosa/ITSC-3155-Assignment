class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, sandwich):
        # Checks if there are enough resources to make the sandwich.
        for ingredient, amount in sandwich.items():
            if self.resources[ingredient] < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich):
        # Make the sandwich and deduct resources from stock.
        for ingredient, amount in sandwich.items():
            self.resources[ingredient] -= amount
        print("Here is your sandwich. Enjoy!")
