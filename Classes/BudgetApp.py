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

    def deposit(self, category_name, amount):
        if category_name in self.catergories:
            self.catergories[category_name] += amount

    def withdraw(self, category_name, amount):
        if category_name in self.catergories:
            if self.catergories[category_name] >= amount:
                self.catergories[category_name] -= amount
            else:
                print("Insufficent Funds")
    




