# Goal: “Create a Budget class that can instantiate objects based on different budget categories
# like food, clothing, and entertainment.
# These objects should allow for depositing and withdrawing funds from each category,
# as well computing category balances and transferring balance amounts between categories”

class budget:
    def __init__(self):
        self.catergories = {}
        #Using a dictionary to store the categories so they can be a key to the balances

    def add_category(self, category_name, initial_balance = 0):
        if category_name not in self.catergories:
            self.catergories[category_name] = initial_balance
            print(f"{category_name} created")

    def deposit(self, category_name, amount):
        if category_name in self.catergories:
            self.catergories[category_name] += amount
            print(f" Successfully deposited £{amount} for {category_name}")

    def withdraw(self, category_name, amount):
        if category_name in self.catergories:
            if self.catergories[category_name] >= amount:
                self.catergories[category_name] -= amount
                print(f" Successfully withdrew £{amount} from {category_name}")
            else:
                print("Insufficent Funds")

    def show_balance(self, category_name):
        if category_name in self.categories:
            print(f"There is £{self.categories[category_name]} in {category_name}")







