class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__ (self):
        print(f' {self.name} ')

    def on_take(self):
        print("")
        print(f'You have picked up {self.name} ')

    def on_drop(self):
        print("")
        print(f'You just dropped {self.name} ')