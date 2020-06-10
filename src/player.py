# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, nickname, current_room):
        self.nickname = nickname
        self.current_room = current_room

    def __str__(self):
        return f'Hello, {self.nickname}. Welcome to the game. Your current room is {self.current_room} '