from room import Room
from player import Player
from item import Item
import argparse

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
    'graveyard': Room("Graveyard", "This is where people go to when they die. Are you next?")
}

items = {
    'shovel': Item('shovel', 'Used for digging. Perhaps your own grave')
}

# Assigned item to a room
room['outside'].add_item(items['shovel'])


# Link rooms together
# I modified this to make it work with my class structure. Not sure how to get this to work another way.

room['outside'].n_to = room['foyer']
room['outside'].s_to = room['graveyard']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to =room['treasure']
room['treasure'].s_to = room['narrow']
room['graveyard'].n_to = room['outside']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Jason', room['outside'])

# Colors for colored folk
print("\033[1;36;40m \n")


# Write a loop that:
#
# * Prints the current room name - done
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f'Your location: {player.current_room.name}. \nDescription: {player.current_room.description}.')
    print('This room contains: ')
    if len(player.current_room.items) == 0:
        print('no items')
    else:
        for item in player.current_room.items:
            print(f'{item.name}')
    userInput = input('Which way would you like to move <n, s, e, w> or <q> to quit: ').lower().split(' ')
    
    if len(userInput) > 2 or len(userInput) < 1:
        print('Invalid input. Enter 1 or 2 arguments')
        continue

    if len(userInput) == 1:
        cmd = userInput[0]
        try:
            if cmd == 'n':
                player.current_room = player.current_room.n_to
                print(f'You move north into {player.current_room} \n' )
            elif cmd == 's':
                player.current_room = player.current_room.s_to
                print(f'You move south into {player.current_room} \n')
            elif cmd == 'e':
                player.current_room = player.current_room.e_to
                print(f'You move east into {player.current_room} \n')
            elif cmd == 'w':
                player.current_room = player.current_room.w_to
                print(f'You move west into {player.current_room} \n')
            elif cmd == 'inventory':
                player.inventory()
            elif cmd == 'q':
                print('Thanks for playing! See you in the next adventure! \n')
                break
        except:
            print('\n You cannot move any further in the chosen direction! Pick a different way to go.')

    if len(userInput) == 2:
        cmd = userInput[0]
        choice = userInput[1]
        stuff = player.current_room.items

        if cmd == 'take':
            for items in stuff:
                if choice == getattr(items, 'name').lower():
                    player.add_item(items)
                    player.current_room.remove_item(items)
                    print(f'You grabbed the {items}')
                elif choice != getattr(items, "name").lower():
                            print("Already gone 🤦‍♀️")
                else:
                    print(f"\t There is nothing to get.")

        if cmd == 'drop':
            for items in player.items:
                if choice == getattr(items, 'name').lower():
                    player.drop_item(items)
