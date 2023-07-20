# Goal: “Create a Budget class that can instantiate objects based on different budget categories
# like food, clothing, and entertainment.
# These objects should allow for depositing and withdrawing funds from each category,
# as well computing category balances and transferring balance amounts between categories”

class budget:
    def __init__(self, category:str , balance = 0):
        self.category = category
        self.balance = balance

    def deposit(self, amount: int):
        self.fund += amount
        print(f"You have deposited £{amount} into {self.name}")
        print(f"New Balance: £{self.balance}")

    def get_balance(self):
        print(F"Balance of {self.name}: £{self.balance}")

    def withdraw(self, amount: int):
        if amount > self.balance:
            print("Insufficent Funds")
            print(f"Balance of {self.name}: £{self.balance}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn £{amount} from {self.name}")
            print(f"Balance for {self.name}: £{self.balance}")

Food = budget("Food",250)
Food.get_balance()
Food.deposit(100)
Food.withdraw(100)
