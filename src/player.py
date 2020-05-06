# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, level, hp, current_room, items):
        self.name = name
        self.level = level
        self.hp = hp
        self.current_room = current_room
        self.items = items

    def addItem(self, item):
        self.items.append(item)

    def move(self, destination):
        self.location = destination

    def changeHp(self, change):
        self.hp = self.hp + change

    def __str__(self):
        return f"My name is {self.name}. I am level {self.level}. My HP is {self.hp}. I am in {self.current_room}. I am holding {self.items} items."


