from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

Player1 = Player("lonely_wolf", room['outside'])

print(Player1)
# print(room['outside'].n_to.description)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    location_text = f'You are in {Player1.current_room.name}: {Player1.current_room.description} '
    print(location_text)
    print("""Please choose where do you want to go. Your options are: 
        1. n => to go to the North; 
        2. s => to go to the South; 
        3. w => to go to the West; 
        4. e => to go to the East; 
        5. q => to quit the game. """)
    user_movement = input("Where do you want to go? ")

    if(user_movement == "n"):
        if(Player1.current_room.n_to == ""):
            print("""Sorry, there is no room there. Read description of the room carefully 
                and try to use different dirrection""")
        else:
            Player1.current_room = Player1.current_room.n_to
            print(f'Right now you are in {Player1.current_room} ')

    if(user_movement == "s"):
        if(Player1.current_room.s_to == ""):
            print("""Sorry, there is no room there. Read description of the room carefully 
                and try to use different dirrection""")
        else:
            Player1.current_room = Player1.current_room.s_to
            print(f'Right now you are in {Player1.current_room} ')
    
    if(user_movement == "w"):
        if(Player1.current_room.w_to == ""):
            print("""Sorry, there is no room there. Read description of the room carefully 
                and try to use different dirrection""")
        else:
            Player1.current_room = Player1.current_room.w_to
            print(f'Right now you are in {Player1.current_room} ')

    if(user_movement == "e"):
        if(Player1.current_room.e_to == ""):
            print("""Sorry, there is no room there. Read description of the room carefully 
                and try to use different dirrection""")
        else:
            Player1.current_room = Player1.current_room.e_to
            print(f'Right now you are in {Player1.current_room} ')

    if(user_movement == "q"):
        break