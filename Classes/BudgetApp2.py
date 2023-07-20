# Goal: “Create a Budget class that can instantiate objects based on different budget categories
# like food, clothing, and entertainment.
# These objects should allow for depositing and withdrawing funds from each category,
# as well computing category balances and transferring balance amounts between categories”

class budget:
    def __init__(self, name:str , balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount
        print(f"You have deposited £{amount} into {self.name}")
        print(f"New Balance: £{self.balance}")

    def get_balance(self):
        print(F"Balance of {self.name}: £{self.balance}")

    def withdraw(self, amount: int):
        if amount > self.balance:
            print("Insufficent Funds")
            print(f"Balance for {self.name}: £{self.balance}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn £{amount} from {self.name}")
            print(f"New Balance: £{self.balance}")

    def transfer(self, amount, other_name):
        if self.name == other_name:
            if amount > self.balance:
                print("Insufficent Funds")
            if amount <= self.balance:
                self.balance -= amount
                other_name.balance += amount
                print(f"£{amount} was transferred to {other_name} from {self.name}")
                print(f"{self.name} balance: £{self.balance}")
                print(f"{other_name} balance: £{other_name.balance}")

Food = budget("Food",250)
Food.get_balance()
Food.deposit(100)
Food.withdraw(100)
Food.withdraw(300)
