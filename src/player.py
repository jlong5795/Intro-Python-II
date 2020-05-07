# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def move(self, destination):
        self.location = destination

    def __str__(self):
        return f"My name is {self.name}. I am in {self.current_room}. I am holding {self.items} items."
        


