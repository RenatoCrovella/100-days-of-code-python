from item import Item

class Inventory:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.slots = []

    def add_item(self, name_item):
        for item in self.slots:
            if item.name == name_item:
                item.quantity += 1
                return True
        if len(self.slots) < self.capacity:
            self.slots.append(Item(name_item))
            return True
        return False

    def remove_item(self, name_item):
        for item in self.slots:
            if item.name == name_item:
                item.quantity -= 1
                if item.quantity <= 0:
                    self.slots.remove(item)
                return True
        return False