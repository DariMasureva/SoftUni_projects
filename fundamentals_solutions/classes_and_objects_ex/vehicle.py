class Vehicle:
    def __init__(self, type:str, model:str, price:int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money:int, owner:str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif money < self.price and self.owner is None:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None
            return ""

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.type} is owned by: {self.owner}"

