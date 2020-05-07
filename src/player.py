# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.add_item(item)

    def inventory(self):
        if len(self.items) == 0:
            print('You have no items')
        for item in self.items:
            print(f'You have {item.name}')
    

    def __str__(self):
        return f"My name is {self.name}. I am in {self.current_room}. I am holding {self.items} items."
        


