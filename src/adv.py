from room import Room
from player import Player
from item import Item
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


# Creating Items
life = Item("Life", "Take it. Always take it. Maybe you'll need an extra life in the future levels")
food = Item("Food", "Help to increase your energy")
drink = Item("Drink", "Every person need some water")
light = Item("Light", "Some rooms are so dark. You'll probably need it")
knife = Item("Knife", "Helps you to cut ropes")
sword = Item("Sword", "You have some treasures? Probably you need to be able to protect yourself")
coin = Item("Coin", "Just simply your money. You can buy really cool stuff for it")
diamond = Item("Diamond", "You can sell it for extra money")
keys = Item("Keys", "Can open any door")

room["outside"].items = [life, coin]
room["foyer"].items = [light, sword]
room["overlook"].items = [food, drink, knife]
room["narrow"].items = []
room["treasure"].items = [keys, diamond]

# Main

# Make a new player object that is currently in the 'outside' room.

Player1 = Player("lonely_wolf", room['outside'])

print(" ")
print(Player1)

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
    print("")
    print(location_text)
    print("")
    print("""Please choose what do you want to do. Your options are: 
        1. n => go to the North; 
        2. s => go to the South; 
        3. w => go to the West; 
        4. e => go to the East; 
        5. see items => lets you to see the items in the current room;
        6. get [Item] OR take [Item] => lets you to add the item to your 
           inventory (for example: get food, take keys);
        7. drop [Item] => lets you to leave the item in current room 
           (for example: drop cigarette); 
        8. i OR inventory => lets you to see the items you have
        9. q => quit the game. """)
    user_choice = input("What do you want to do? ").lower().split(" ")

    # Shorter way
    # if user_choice in {'n', 's','e', 'w'}:
    #     if hasattr(Player1.current_room, f'{user_choice}_to'):
    #         Player1.current_room = getattr(Player1.current_room, f'{user_choice}_to')
    
    if(len(user_choice) == 1):
        if(user_choice[0] == "n"):
            if(Player1.current_room.n_to == ""):
                print("")
                print("""Sorry, there is no room there. Read description of the room carefully 
                    and try to use different dirrection""")
            else:
                Player1.current_room = Player1.current_room.n_to
                Player1.current_room.show_items()

        if(user_choice[0] == "s"):
            if(Player1.current_room.s_to == ""):
                print("")
                print("""Sorry, there is no room there. Read description of the room carefully 
                    and try to use different dirrection""")
            else:
                Player1.current_room = Player1.current_room.s_to
                Player1.current_room.show_items()
        
        if(user_choice[0] == "w"):
            if(Player1.current_room.w_to == ""):
                print("")
                print("""Sorry, there is no room there. Read description of the room carefully 
                    and try to use different dirrection""")
            else:
                Player1.current_room = Player1.current_room.w_to
                Player1.current_room.show_items()

        if(user_choice[0] == "e"):
            if(Player1.current_room.e_to == ""):
                print("")
                print("""Sorry, there is no room there. Read description of the room carefully 
                    and try to use different dirrection""")
            else:
                Player1.current_room = Player1.current_room.e_to
                Player1.current_room.show_items()

        if(user_choice[0] == "i" or user_choice[0] == "inventory"):
            Player1.show_inventory()

        if(user_choice[0] == "q"):
            break

    elif(len(user_choice) == 2):
        if(user_choice[0] == "get" or user_choice[0] == "take"):
            has_item = [item for item in Player1.current_room.items if item.name.lower() == user_choice[1]]
            if(len(has_item) > 0):
                Player1.add_to_inventory(has_item[0])
                Player1.current_room.remove_item(has_item[0])
                Player1.inventory[len(Player1.inventory) -1].on_take()
            else:
                print("")
                print("There is no such item. You can use command 'see items' to check the available one")

        if(user_choice[0] == "drop"):
            item_to_drop = [item for item in Player1.inventory if item.name.lower() == user_choice[1]]
            if(len(item_to_drop) > 0):
                Player1.remove_from_inventory(item_to_drop[0])
                Player1.current_room.add_item((item_to_drop[0]))
                Player1.current_room.items[len(Player1.current_room.items) - 1].on_drop()
            else:
                print("")
                print("You can't drop what you don't have. Use the command 'i' or 'inventory' to see what items you have ")

        if(user_choice[0] == "see" and user_choice[1] == "items"):
                Player1.current_room.show_items()