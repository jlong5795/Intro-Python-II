from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
# I modified this to make it work with my class structure. Not sure how to get this to work another way.

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to ='treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Jason', 'outside')

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
    print(f'Your location: {player.current_room}. \n Description: {room[player.current_room].description}')
    userInput = input('Which way would you like to move <n, s, e, w> or <q> to quit: ')
    
    try:
        if userInput == 'n':
            player.current_room = room[player.current_room].n_to
            print(f'You move north into {player.current_room} \n' )
        elif userInput == 's':
            player.current_room = room[player.current_room].s_to
            print(f'You move south into {player.current_room} \n')
        elif userInput == 'e':
            player.current_room = room[player.current_room].e_to
            print(f'You move east into {player.current_room} \n')
        elif userInput == 'w':
            player.current_room = room[player.current_room].w_to
            print(f'You move west into {player.current_room} \n')
        elif userInput == 'q':
            print('Thanks for playing! See you in the next adventure! \n')
            break
    except:
        print('\n You cannot move any further in the chosen direction! Pick a different way to go.')