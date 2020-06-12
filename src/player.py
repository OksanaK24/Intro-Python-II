# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, nickname, current_room):
        self.nickname = nickname
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'Hello, {self.nickname}. Welcome to the game. Your current room is {self.current_room}'

    def show_inventory(self):
        if len(self.inventory) > 0: 
            print("")
            print(f'You have these items: ')
            index = 1
            for item in self.inventory:
                print(f' {index}. {item.name} : {item.description} ')
                index += 1
        else:
            print("")
            print(f" You don't have any items ")

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)
