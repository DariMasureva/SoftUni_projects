class Inventory:
    def __init__(self, __capacity:int):
        self.capacity = __capacity
        self.items = []

    def add_item(self, item:str):
        if len(self.items) < self.capacity:
            self.items.append(item)
            return ""
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity - len(self.items)}"


